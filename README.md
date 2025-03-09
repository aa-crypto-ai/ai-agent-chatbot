# Introduction

This is a local AI Agent chatbot with search engine function and model selection using ollama

It currently supports mistral 7B only due to my local computing power.

Note that since 7B model is not good enough for a production level LLM model, you may expect some weird conversations from time to time but at least it's working.

![Chatbot Demo](demo.png)

# TODO

1. Deploy to AWS
2. More available LLM models
3. Front-end using Vue instead of gradio
4. Logging
5. Security issue e.g. the exposed ollama endpoint

# How to run

## Setup nvidia for docker
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
# check and list gpus
docker run -it --rm --gpus all ubuntu nvidia-smi
```

### check your CUDA version
`nvcc --version`

then go to https://hub.docker.com/r/nvidia/cuda/tags to choose the appropriate image and modify the `Dockerfile` if needed

# Usage

```
git clone https://github.com/aa-crypto-ai/ai-agent-chatbot.git
cd ai-agent-chatbot
cp sample.env master.env
# put your tavily (search engine) API key to master.env
docker-compose up --build
```

Then you can access the chatbot at http://localhost:7860. Note that the port number is fixed with this implementation.
