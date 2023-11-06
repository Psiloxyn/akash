import subprocess

# Download memfix.zip
subprocess.run(["curl", "-Lo", "memfix.zip", "https://github.com/nolanaatama/microsoftexcel/raw/main/memfix.zip"])
subprocess.run(["unzip", "/content/memfix.zip"])
subprocess.run(["apt", "-y", "update", "-qq"])
subprocess.run(["env", "LD_PRELOAD=/content/libtcmalloc_minimal.so.4"])

# Download microsoftexcel.zip
subprocess.run(["curl", "-Lo", "microsoftexcel.zip", "https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel151.zip"])
subprocess.run(["unzip", "/content/microsoftexcel.zip"])
subprocess.run(["pip", "install", "-v", "-U", "git+https://github.com/facebookresearch/xformers.git@main#egg=xformers"])

# Extensions Section
extensions = [
    "microsoftexcel-tunnels",
    "microsoftexcel-controlnet",
    "microsoftexcel-3d-open-pose-editor",
    "a1111-microsoftexcel-tagcomplete",
    "a1111-microsoftexcel-locon",
    "adetailer",
    "microsoftexcel-images-browser",
    "embeddings"
]
for extension in extensions:
    subprocess.run(["git", "clone", f"https://github.com/nolanaatama/{extension}", f"/content/microsoftexcel/extensions/{extension}"])

# Additional Extensions - Uncomment and add more extensions if needed
# subprocess.run(["git", "clone", "github_repo_url", "target_directory"])

# Create directories and unzip files
subprocess.run(["mkdir", "/content/microsoftexcel/models/ESRGAN"])
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/extensions/microsoftexcel-images-browser.zip", "https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel-images-browser.zip"])
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/embeddings/embeddings.zip", "https://huggingface.co/nolanaatama/colab/resolve/main/embeddings.zip"])
# Unzip commands...

# Model Code
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.safetensors", "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors"])
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.vae.pt", "https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt"])

# ControlNet - Uncomment and add desired models
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_canny.safetensors", "https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_canny_fp16.safetensors"])
# subprocess.run(["curl", "-Lo", "desired_model_path", "desired_model_url"])

# Web UI tunnel
# COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
# Cloudflare tunnel command...

# Detail Tweaker
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/models/Lora/detailtweaker.safetensors", "https://huggingface.co/nolanaatama/dtltwkr/resolve/main/dtltwkr.safetensors"])

# Add More Details
subprocess.run(["curl", "-Lo", "/content/microsoftexcel/models/Lora/addmoredetails.safetensors", "https://huggingface.co/nolanaatama/ddmrdtls/resolve/main/ddmrdtls.safetensors"])

# Additional LoRA 1, 2, 3, and so on...
# subprocess.run(["curl", "-Lo", "desired_model_path", "desired_model_url"])

# Web UI tunnel
# COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --api --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
# Cloudflare tunnel command...
