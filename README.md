
# 🍌 Banana Serverless

This repo gives a basic framework for serving Stable Diffusion in production using simple HTTP servers.

NOTE: the template requires you to configure your huggingface auth key into it before it works. Read "Move to prod" below for instructions.

If you want to generalize this to deploy anything on Banana, [see the guide here](https://www.notion.so/banana-dev/How-To-Serve-Anything-On-Banana-125a65fc4d30496ba1408de1d64d052a).

## Quickstart:

The repo is already set up to run [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) text-to-image model.
1. Run `pip3 install -r requirements.txt` to download dependencies.
2. Set your Huggingface Auth Token as an environment variable `export HF_AUTH_TOKEN=your_auth_token`
3. Run `python3 server.py` to start the server.
4. Run `python3 test.py` in a different terminal session to test against it.

## Make it your own:

1. Edit `app.py` to load and run your model.
2. Make sure to test with `test.py`!
3. When ready to deploy:
  - add your HF_AUTH_TOKEN environment variable to the dockerfile, or [contact the Banana team](https://www.banana.dev/contact) to set it privately as a build arg.
  - edit `download.py` (or the `Dockerfile` itself) with scripts download your custom model weights at build time
  - edit `requirements.txt` with your pip packages. Don't delete the "sanic" line, as it's a banana dependency.

## Move to prod:

At this point, you have a functioning http server for your ML model. You can use it as is, or package it up with our provided `Dockerfile` and deploy it to your favorite container hosting provider!

If Banana is your favorite GPU hosting provider (and we sure hope it is), read on!

# 🍌

# Deploy to Banana Serverless:

Three steps:
1. Create your own copy of this template repo. Either:
- Click "Fork" on this repo (creates a public repo)
- Create your own repo and copy the template files into it (to create a private repo)

2. Install the [Banana Github App](https://github.com/apps/banana-serverless) to your new repo.

3. Login in to the [Banana Dashboard](https://app.banana.dev) and setup your account by saving your payment details and linking your Github.

From then onward, any pushes to the default repo branch (usually "main" or "master") trigger Banana to build and deploy your server, using the Dockerfile.
Throughout the build we'll sprinkle in some secret sauce to make your server extra snappy 🔥

It'll then be deployed on our Serverless GPU cluster and callable with any of our serverside SDKs:

- [Python](https://github.com/bananaml/banana-python-sdk)
- [Node JS / Typescript](https://github.com/bananaml/banana-node-sdk)
- [Go](https://github.com/bananaml/banana-go)

You can monitor buildtime and runtime logs by clicking the logs button in the model view on the [Banana Dashboard](https://app.banana.dev)

<br>

## Use Banana for scale.
