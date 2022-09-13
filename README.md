
# 🍌 Banana Serverless

This repo gives a basic framework for serving Stable Diffusion in production using simple HTTP servers.

## Extra Quickstart:
Stable Diffusion is now avaiable as an instant deploy template on Banana!

Log into the App, click "New Model", and then "deploy from a template".

## Quickstart:

If you want to customize beyond the one click template:

1. Create your own private repo and copy the files from this template repo into it. You'll want a private repo so that your huggingface keys are secure.
2. Create huggingface account to get permission to download and run [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) text-to-image model.
  - Accept terms and conditions for the use of the v1-4 [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4)
3. Edit the `dockerfile` in your forked repo with `ENV HF_AUTH_TOKEN=your_auth_token`
4. Edit the repo with any customizations you may want, and push those to main.
5. Log in to the [Banana App](https://app.banana.dev)
6. Select your customized repo for deploy!

It'll then be built from the dockerfile, optimized, then deployed on our Serverless GPU cluster and callable with any of our SDKs:

- [Python](https://github.com/bananaml/banana-python-sdk)
- [Node JS / Typescript](https://github.com/bananaml/banana-node-sdk)
- [Go](https://github.com/bananaml/banana-go)

You can monitor buildtime and runtime logs by clicking the logs button in the model view on the [Banana Dashboard](https://app.banana.dev)

<br>

## Use Banana for scale.
