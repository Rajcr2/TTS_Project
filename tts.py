# python version 3.9.6
# python --version
# python -m venv venv
# venv/Scripts/activate
# python.exe -m pip install --upgrade pip
# pip install TTS --cache-dir "D:/internship/tts_project/.cache"
# pip uninstall torch torchvision torchaudio
# pip install transformers datasets torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --cache-dir "D:/internship/tts_project/.cache"
# https://developer.nvidia.com/cuda-downloads
# pip install soundfile --cache-dir "D:/internship/tts_project/.cache"
# pip install deepspeed==0.10.3 --cache-dir "D:/internship/tts_project/.cache" optional


from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf  # To save the output as a wav file

# Step 1: Load the model configuration
config = XttsConfig()
config.load_json("C:/Users/Raj/Desktop/ML_Internship/TTS_Project/tts_config/XTTS-v2/config.json") 

# Step 2: Initialize the model
model = Xtts.init_from_config(config)

# Step 3: Load the pre-trained weights
model.load_checkpoint(config, checkpoint_dir="C:/Users/Raj/Desktop/ML_Internship/TTS_Project/tts_config/XTTS-v2", eval=True)

# Optional: If you have CUDA installed and want to use GPU, uncomment the line below
# model.cuda()

# Step 4: Synthesize the output
outputs = model.synthesize(
    "Hello, My Name is Raj Jangam and I am currently testing this Text-to-Speech Project. ",
    config,
    speaker_wav="ah_yes.wav",  # Replace with the correct path
    gpt_cond_len=3,
    language="en",
)

# Step 5: Save the synthesized speech to a wav file
output_wav = outputs['wav']
sf.write('output.wav', output_wav, config.audio.sample_rate)

print("Speech synthesis complete and saved to output.wav")