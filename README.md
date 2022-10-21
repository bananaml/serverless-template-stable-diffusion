
# 🍌 Banana Serverless

This repo gives a basic framework for serving Stable Diffusion in production using simple HTTP servers.

## Instant Deploy
Stable Diffusion is now available as a prebult model on Banana! [See how to deploy Stable Diffusion in seconds](https://docs.banana.dev/banana-docs/core-concepts/inference-server/1-click-deploy).


# Quickstart

If you want to customize beyond the prebuilt model:

**[Follow the quickstart guide in Banana's documentation to use this repo](https://docs.banana.dev/banana-docs/quickstart).** 

*(choose "GitHub Repository" deployment method)*

### Additional Steps (outside of quickstart guide)

1. Create your own private repo and copy the files from this template repo into it. You'll want a private repo so that your huggingface keys are secure.
2. Create huggingface account to get permission to download and run [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) text-to-image model.
  - Accept terms and conditions for the use of the v1-4 [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
3. Edit the `dockerfile` in your forked repo with `ENV HF_AUTH_TOKEN=your_auth_token`


# Helpful Links
Understand the 🍌 [Serverless framework](https://docs.banana.dev/banana-docs/core-concepts/inference-server/serverless-framework) and functionality of each file within it.

Generalize this framework to [deploy anything on Banana](https://docs.banana.dev/banana-docs/resources/how-to-serve-anything-on-banana).


<br>

## Use Banana for scale.
