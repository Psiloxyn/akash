curl -Lo memfix.zip https://github.com/nolanaatama/microsoftexcel/raw/main/memfix.zip
unzip /content/memfix.zip
apt -y update -qq
env LD_PRELOAD=/content/libtcmalloc_minimal.so.4

curl -Lo microsoftexcel.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel151.zip
unzip /content/microsoftexcel.zip
pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers

# Extensions Section
git clone https://github.com/nolanaatama/microsoftexcel-tunnels /content/microsoftexcel/extensions/microsoftexcel-tunnels
git clone https://github.com/nolanaatama/microsoftexcel-controlnet /content/microsoftexcel/extensions/microsoftexcel-controlnet
git clone https://github.com/fkunn1326/openpose-editor /content/microsoftexcel/extensions/openpose-editor
git clone https://github.com/nolanaatama/microsoftexcel-3d-open-pose-editor /content/microsoftexcel/extensions/microsoftexcel-3d-open-pose-editor
git clone https://github.com/nolanaatama/a1111-microsoftexcel-tagcomplete /content/microsoftexcel/extensions/a1111-microsoftexcel-tagcomplete
git clone https://github.com/nolanaatama/a1111-microsoftexcel-locon /content/microsoftexcel/extensions/a1111-microsoftexcel-locon
# Additional Extensions
#  After Detailer
# git clone https://github.com/Bing-su/adetailer /content/microsoftexcel/extensions/adetailer
# git clone https://huggingface.co/Bingsu/adetailer /content/microsoftexcel/models/adetailer
# Deforum
# git clone https://github.com/nolanaatama/microsoftexcel-deforum /content/microsoftexcel/extensions/microsoftexcel-deforum
# Mov2mov
# git clone https://github.com/nolanaatama/microsoftexcel-mov2mov /content/microsoftexcel/extensions/microsoftexcel-mov2mov
# roop
# git clone https://github.com/nolanaatama/microsoftexcel-roop /content/microsoftexcel/extensions/microsoftexcel-roop
# SuperMerger
# git clone https://github.com/nolanaatama/microsoftexcel-supermerger /content/microsoftexcel/extensions/microsoftexcel-supermerger
# TemporalKit
# git clone https://github.com/CiaraStrawberry/TemporalKit /content/microsoftexcel/extensions/TemporalKit
# Ultimate SD Upscale
# git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/microsoftexcel/extensions/ultimate-upscale-for-automatic1111

mkdir /content/microsoftexcel/models/ESRGAN
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-images-browser.zip https://huggingface.co/nolanaatama/colab/resolve/main/microsoftexcel-images-browser.zip
curl -Lo /content/microsoftexcel/embeddings/embeddings.zip https://huggingface.co/nolanaatama/colab/resolve/main/embeddings.zip
curl -Lo /content/microsoftexcel/models/ESRGAN/upscalers.zip https://huggingface.co/nolanaatama/colab/resolve/main/upscalers.zip
cd /content/microsoftexcel/extensions
unzip /content/microsoftexcel/extensions/microsoftexcel-images-browser.zip
cd /content/microsoftexcel/embeddings
unzip /content/microsoftexcel/embeddings/embeddings.zip
cd /content/microsoftexcel/models/ESRGAN
unzip /content/microsoftexcel/models/ESRGAN/upscalers.zip
rm upscalers.zip
cd /content

# Model Code
curl -Lo /content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.safetensors https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix2/AbyssOrangeMix2_hard.safetensors
curl -Lo /content/microsoftexcel/models/Stable-diffusion/abyssorangemix2.vae.pt https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt

# ControlNet
# Remove '#' from the beginning of the line(s) below to download the selected ControlNet model(s)
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11e_sd15_ip2p.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11e_sd15_shuffle.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_canny.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_canny_fp16.safetensors
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11f1p_sd15_depth.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_depth_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_inpaint.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_lineart.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_lineart_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_mlsd.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_normalbae.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_openpose.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_openpose_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_scribble.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_scribble_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_seg.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_seg_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15_softedge.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15_softedge_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11p_sd15s2_lineart_anime.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/control_v11f1e_sd15_tile.safetensors https://huggingface.co/nolanaatama/models/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_canny_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_canny_sd14v1.pth
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_color_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_color_sd14v1.pth
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_depth_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_depth_sd14v1.pth
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_keypose_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_keypose_sd14v1.pth
curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_openpose_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_openpose_sd14v1.pth
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_seg_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_seg_sd14v1.pth
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_sketch_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_sketch_sd14v1.pth
# curl -Lo /content/microsoftexcel/extensions/microsoftexcel-controlnet/models/t2iadapter_style_sd14v1.pth https://huggingface.co/nolanaatama/models/resolve/main/t2iadapter_style_sd14v1.pth
rm microsoftexcel.zip
cd /content/microsoftexcel

# Web UI tunnel
# COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
# Use this command below to use cloudflare tunnel
# COMMANDLINE_ARGS="--disable-safe-unpickle --no-half-vae --xformers --enable-insecure-extension --gradio-queue --cloudflared" REQS_FILE="requirements.txt" python launch.py

# Copy the LoRA code from other LoRA setup (download the setup file after editing the LoRA code cell to avoid repeat input for next session)
# How-to download the setup file: Click 'File' menu -> 'Download' -> 'Download .ipynb'
# Load LoRA from Google Drive: https://youtu.be/G1QZfAPUMaM

# Detail Tweaker
curl -Lo /content/microsoftexcel/models/Lora/detailtweaker.safetensors https://huggingface.co/nolanaatama/dtltwkr/resolve/main/dtltwkr.safetensors

# Add More Details
curl -Lo /content/microsoftexcel/models/Lora/addmoredetails.safetensors https://huggingface.co/nolanaatama/ddmrdtls/resolve/main/ddmrdtls.safetensors

# Additional LoRA 1
# curl ...

# Additional LoRA 2
# curl ...

# Additional LoRA 3
# curl ...

# ...

# Web UI tunnel
COMMANDLINE_ARGS="--share --disable-safe-unpickle --no-half-vae --xformers --api --enable-insecure-extension --gradio-queue" REQS_FILE="requirements.txt" python launch.py
# Use this command below to use cloudflare tunnel
COMMANDLINE_ARGS="--disable-safe-unpickle --no-half-vae --xformers --api --enable-insecure-extension --gradio-queue --cloudflared" REQS_FILE="requirements.txt" python launch.py
