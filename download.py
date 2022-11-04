# In this file, we define download_model
# It runs during container build time to get model weights built into the container

from diffusers import StableDiffusionPipeline
import os

def download_model():
    # do a dry run of loading the huggingface model, which will download weights at build time
    #Set auth token which is required to download stable diffusion model weights
    HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")

    model = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", 
        use_auth_token=HF_AUTH_TOKEN
    )

if __name__ == "__main__":
    download_model()
