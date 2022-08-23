# Must use a Cuda version 11+
FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git

# Install python packages
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# We add the banana boilerplate here
ADD server.py .

# Add your model weight files 
# (in this case we have a python script)

#Alternative to using build args, you can put your token in the next line
#ENV HF_AUTH_TOKEN={token}
ARG HF_AUTH_TOKEN
ADD download.py .
RUN python3 download.py


# Add your custom app code, init() and inference()
ADD app.py .

EXPOSE 8000

ENV HF_AUTH_TOKEN=$HF_AUTH_TOKEN
CMD python3 -u server.py
