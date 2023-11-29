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
The Visual Encoder-Decoder Model can be used to initialize an image-to-text model with:  
Step 01: Pretrained transformer-based vision model ==> this is the encoder (ViT)  
Step 02: Pretrained language model ==> this is the decoder (GPT-2)  
