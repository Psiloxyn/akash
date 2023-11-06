#!/bin/bash

# Define a function containing the commands
execute_commands() {
    # Download memfix.zip
    curl -Lo memfix.zip https://github.com/nolanaatama/microsoftexcel/raw/main/memfix.zip
    unzip /content/memfix.zip
    apt -y update -qq
    env LD_PRELOAD=/content/libtcmalloc_minimal.so.4

    # Download microsoftexcel.zip
    curl -Lo microsoftexcel.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel151.zip
    unzip /content/microsoftexcel.zip
    pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers

    # Extensions Section
    git clone https://github.com/nolanaatama/microsoftexcel-tunnels /content/microsoftexcel/extensions/microsoftexcel-tunnels
    git clone https://github.com/nolanaatama/microsoftexcel-controlnet /content/microsoftexcel/extensions/microsoftexcel-controlnet
    # (Rest of the extensions...)

    # Unzip files and setup directories
    mkdir /content/microsoftexcel/models/ESRGAN
    curl -Lo /content/microsoftexcel/extensions/microsoftexcel-images-browser.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel-images-browser.zip
    # (Unzip commands...)

    # Model Code
    curl -Lo /content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.safetensors https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors
    curl -Lo /content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.vae.pt https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt
    # (Other model-related commands...)

    # ControlNet
    # (ControlNet commands...)

    # Web UI tunnel
    COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --api --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
    # (Cloudflare tunnel command...)

    # Detail Tweaker
    curl -Lo /content/microsoftexcel/models/Lora/detailtweaker.safetensors https://huggingface.co/nolanaatama/dtltwkr/resolve/main/dtltwkr.safetensors

    # Add More Details
    curl -Lo /content/microsoftexcel/models/Lora/addmoredetails.safetensors https://huggingface.co/nolanaatama/ddmrdtls/resolve/main/ddmrdtls.safetensors

    # Additional LoRA 1
    # (Additional LoRA commands...)

    # Web UI tunnel
    COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --api --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
    # (Cloudflare tunnel command...)
}

# Call the function
execute_commands
