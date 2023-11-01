# -*- coding: utf-8 -*-
"""Oobabooga Text WebgenUI

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kn5fHJjxv6qSMggMVCeqs18JKd1KDOKN

# oobabooga/text-generation-webui

After running both cells, a public gradio URL will appear at the bottom in a few minutes. You can optionally generate API links.

* Project page: https://github.com/oobabooga/text-generation-webui
* Gradio server status: https://status.gradio.app/
"""

# Commented out IPython magic to ensure Python compatibility.
# #@title 1. Keep this tab alive to prevent Colab from disconnecting you { display-mode: "form" }
# 
# #@markdown Press play on the music player that will appear below:
# %%html
# <audio src="https://oobabooga.github.io/silence.m4a" controls>

# Commented out IPython magic to ensure Python compatibility.
#@title 2. Launch the web UI

#@markdown If unsure about the branch, write "main" or leave it blank.

import torch
from pathlib import Path

if Path.cwd().name != 'text-generation-webui':
  print("Installing the webui...")

  !git clone https://github.com/oobabooga/text-generation-webui
#   %cd text-generation-webui

  torver = torch.__version__
  print(f"TORCH: {torver}")
  is_cuda118 = '+cu118' in torver  # 2.1.0+cu118
  is_cuda117 = '+cu117' in torver  # 2.0.1+cu117

  textgen_requirements = open('requirements.txt').read().splitlines()
  if is_cuda117:
      textgen_requirements = [req.replace('+cu121', '+cu117').replace('+cu122', '+cu117').replace('torch2.1', 'torch2.0') for req in textgen_requirements]
  elif is_cuda118:
      textgen_requirements = [req.replace('+cu121', '+cu118').replace('+cu122', '+cu118') for req in textgen_requirements]
  with open('temp_requirements.txt', 'w') as file:
      file.write('\n'.join(textgen_requirements))

  !pip install -r extensions/api/requirements.txt --upgrade
  !pip install -r temp_requirements.txt --upgrade

  print("\033[1;32;1m\n --> If you see a warning about \"previously imported packages\", just ignore it.\033[0;37;0m")
  print("\033[1;32;1m\n --> There is no need to restart the runtime.\n\033[0;37;0m")

  try:
    import flash_attn
  except:
    !pip uninstall -y flash_attn

# Parameters
model_url = "https://huggingface.co/TheBloke/Mythalion-13B-GPTQ" #@param {type:"string"}
branch = "" #@param {type:"string"}
command_line_flags = "--n-gpu-layers 128 --load-in-4bit --use_double_quant" #@param {type:"string"}
api = True #@param {type:"boolean"}

if api:
  for param in ['--api', '--public-api']:
    if param not in command_line_flags:
      command_line_flags += f" {param}"

model_url = model_url.strip()
if model_url != "":
    if not model_url.startswith('http'):
        model_url = 'https://huggingface.co/' + model_url

    # Download the model
    url_parts = model_url.strip('/').strip().split('/')
    output_folder = f"{url_parts[-2]}_{url_parts[-1]}"
    branch = branch.strip('"\' ')
    if branch.strip() != '':
        output_folder += f"_{branch}"
        !python download-model.py {model_url} --branch {branch}
    else:
        !python download-model.py {model_url}
else:
    output_folder = ""

# Start the web UI
cmd = f"python server.py --share"
if output_folder != "":
    cmd += f" --model {output_folder}"
cmd += f" {command_line_flags}"
print(cmd)
!$cmd