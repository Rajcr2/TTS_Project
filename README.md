# Text-to-Speech Project

## Introduction

This is my Internship project. Where we can pass a text to a XTTS_V2 pre-trained model then it will convert it into a speech to a specific voice given by us which in the .wav format.
So, Lets see.

XTTS Model (Download Link) -> [https://huggingface.co/coqui/XTTS-v2/tree/main)]

### Prerequisites
To run this project, you need to install the following libraries:
### Required Libraries

- **Python 3.9.0+**
- **TTS**: This NLP toolkit consist of comprehensive libraries which work with human language data.
- **PyTorch**: Consist of tools, libraries which are used to train and deploy machine learning model.
- **TorchVison and TorchAudio**: Flask is a lightweight and flexible web framework for Python, designed to make it easy to build web applications quickly.
- **Transformers**

Other Utility Libraries : **soundfile**, **datasets**.

### Installation

   ```
   pip install TTS
   pip install torch==2.1.0
   pip install torchvision==0.16.0
   pip install torchaudio==2.1.0
   pip install transformers
   pip install soundfile
   pip install datasets
   ```

### Procedure

1.   Create new directory **'TTS_Project'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv tts
   ```

  Now, activate this **'tts'** venv.
  
4.   Clone this Repository :

   ```
   git clone https://huggingface.co/coqui/XTTS-v2
   ```
   By cloning this it will download "XTTS_V2 Model" with the help of which we will convert out Text into Speech.

5.   Now, Install all mentioned required libraries in your environment.
6.   After, that Run **'tts.py'** file from Terminal. To train the model.
   ```
   python tts.py
   ```

### Output

After Running this file you will get output message.
     **'Speech synthesis complete and saved to output.wav'**

![image](https://github.com/user-attachments/assets/b1efcc67-a8a3-4444-8952-5f8235a8737e)

### Conclusion

So, this is very basic tts_project like a one text data you can pass a paragraph as well or set of Multiple sentences using SQLite.
For that stay tuned.





