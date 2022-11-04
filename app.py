import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler, EulerAncestralDiscreteScheduler, EulerDiscreteScheduler, DDIMScheduler, PNDMScheduler
import base64
from io import BytesIO
import os

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")

    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=HF_AUTH_TOKEN).to("cuda")

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    negative_prompt = model_inputs.get('negative_prompt', None)
    height = model_inputs.get('height', 512)
    width = model_inputs.get('width', 512)
    num_inference_steps = model_inputs.get('num_inference_steps', 50)
    guidance_scale = model_inputs.get('guidance_scale', 7.5)
    num_images_per_prompt = model_inputs.get('num_images_per_prompt', 1)
    input_seed = model_inputs.get("seed", None)
    scheduler = model_inputs.get("diffusion", "k_euler_ancestral")
    
    # If "seed" is not sent, we won't specify a seed in the call
    generator = None
    if input_seed != None:
        generator = torch.Generator("cuda").manual_seed(input_seed)
    
    if prompt == None:
        return {'message': "No prompt provided"}

    # Setup custom scheduler
    model.scheduler = make_scheduler(scheduler)    
    
    # Run the model
    with autocast("cuda"):
        images = model(prompt,height=int(height),width=int(width),num_inference_steps=int(num_inference_steps),guidance_scale=float(guidance_scale),generator=generator,num_images_per_prompt=int(num_images_per_prompt),negative_prompt=negative_prompt).images
    
    images_base64 = []
    for image in images:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        images_base64.append(base64.b64encode(buffered.getvalue()).decode("utf-8"))

    return {"images_base64": images_base64}

# Define custom scheduler for the model
def make_scheduler(name):
    HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")

    if name == 'k_euler_ancestral':
        return EulerAncestralDiscreteScheduler.from_config("CompVis/stable-diffusion-v1-4", subfolder="scheduler", use_auth_token=HF_AUTH_TOKEN)

    if name == 'k_euler':
        return EulerDiscreteScheduler.from_config("CompVis/stable-diffusion-v1-4", subfolder="scheduler", use_auth_token=HF_AUTH_TOKEN)

    if name == 'ddim':
        return DDIMScheduler.from_config("CompVis/stable-diffusion-v1-4", subfolder="scheduler", use_auth_token=HF_AUTH_TOKEN)

    if name == 'pndm':
        return PNDMScheduler.from_config("CompVis/stable-diffusion-v1-4", subfolder="scheduler", use_auth_token=HF_AUTH_TOKEN)
        
    return LMSDiscreteScheduler.from_config("CompVis/stable-diffusion-v1-4", subfolder="scheduler", use_auth_token=HF_AUTH_TOKEN)