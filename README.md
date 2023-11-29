# Caption Generator App  
  
Intelligent System for generating captions from uploaded images  

## ML Operations:  

1) Dataset  
COCO - Common objects in conext (Microsoft)  
https://cocodataset.org/#home  

2) DL Model  
Visual Encoder-Decoder Model (ViT + GPT-2)  
Link: https://huggingface.co/docs/transformers/v4.29.1/en/model_doc/vision-encoder-decoder#transformers.VisionEncoderDecoderModel  

![vision-encoder-decoder](https://github.com/HoltechHard/app_captionAI/assets/35493202/73fe6cc2-2741-4b20-838d-ec5e05821338)

Description:  
The Visual Encoder-Decoder Model can be used when system provides image as input and request a text as ouput:  
IMAGE ==> TENSOR EMBEDDING ==> TEXT  
Step 01: Pretrained transformer-based vision model ==> this is the encoder (ViT)  
takes the IMAGE ==> TENSOR EMBEDDING  
Step 02: Pretrained language model ==> this is the decoder (GPT-2)  
takes the TENSOR EMBEDDING ==> TEXT  

## Development Operations:  

In development of CaptionGeneratorApp was used the next technologies:
* Frontend: HTML + CSS + JQuery  
* Backend: Python + Django  
* Database: Postgres  
* ML-modeling: PyTorch  

## Database Model:  
  
![image](https://github.com/HoltechHard/CaptionGeneratorApp/assets/35493202/f3fc069a-311e-4da7-9ef9-d384ed39a4b6)  
  
