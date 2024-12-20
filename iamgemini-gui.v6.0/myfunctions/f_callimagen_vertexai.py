import streamlit as st
import os
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai 
from google.cloud import aiplatform
from vertexai.preview.vision_models import Image, ImageGenerationModel
from vertexai.vision_models import ImageTextModel, Image
from PIL import Image
from io import BytesIO
import uuid

@st.cache_resource
def f_init_vertexai():
    #export GCP_PROJECT='work-mylab-machinelearning'    #Change this
    #export GCP_REGION='us-central1'                    #If you change this, make sure the region is supported.
    vPROJECT_ID = os.environ.get('GCP_PROJECT')         #Your Google Cloud Project ID
    vLOCATION = os.environ.get('GCP_REGION')            #Your Google Cloud Project Region
    vertexai.init(project=vPROJECT_ID, location=vLOCATION)
    print(f"Vertex AI SDK version: {aiplatform.__version__}")

def f_callimagen_createimage(vPrompt: str):
    #model = ImageGenerationModel.from_pretrained("imagegeneration@005")
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
    #model = ImageGenerationModel.from_pretrained("imagen-3.0-fast-generate-001")
    response = model.generate_images(prompt=vPrompt, number_of_images=4
                                    # ,seed=1,negative_prompt=""
                                    )
    fileid = str(uuid.uuid4())
    response[0].save(location="./temp_donotdelete/{}1.png".format(fileid), include_generation_parameters=True)
    response[1].save(location="./temp_donotdelete/{}2.png".format(fileid), include_generation_parameters=True)
    response[2].save(location="./temp_donotdelete/{}3.png".format(fileid), include_generation_parameters=True)
    response[3].save(location="./temp_donotdelete/{}4.png".format(fileid), include_generation_parameters=True)
    return fileid

def f_callimagen_delete_local_image(vFileId: str):
    try:
       os.remove("./temp_donotdelete/{}1.png".format(vFileId))
       os.remove("./temp_donotdelete/{}2.png".format(vFileId))
       os.remove("./temp_donotdelete/{}3.png".format(vFileId))
       os.remove("./temp_donotdelete/{}4.png".format(vFileId))
       success = True
    except FileNotFoundError:
       print("Error: File not found")
       success = False
    else:
       print("File deleted successfully")
    return success

def f_callimagen_editimage(vPrompt: str) -> str:
    model = ImageGenerationModel.from_pretrained("imagegeneration")
    base_img=Image.load_from_file(location='./gen-img1.png')
    images = model.edit_image(base_image=base_img, prompt="pop art style",
    # Optional:
    seed=1,
    guidance_scale=20,
    number_of_images=2
    )
    images[0].save(location="./edit-img1.png")
    images[1].save(location="./edit-img2.png")

def f_callimagen_decribeimage(vPrompt: str) -> str: #I think it is better use gemini rather than this
    model = ImageTextModel.from_pretrained("imagetext@001")
    source_image = Image.load_from_file(location='./gen-img1.png')
    captions = model.get_captions(
        image=source_image,
        # Optional:
        number_of_results=2,
        language="en",
    )
    print(captions)
    return(captions)

def f_callimagen_askimage(vPrompt:str) -> str: #I think it is better use gemini rather than this
    model = ImageTextModel.from_pretrained("imagetext@001")
    source_image = Image.load_from_file(location='./gen-img1.png')
    answers = model.ask_question(
        image=source_image,
        question="What breed of dog is this a picture of?",
        # Optional:
        number_of_results=2,
    )
    print(answers)
    return(answers)

if __name__ == "__main__":
    f_init_vertexai()

#Test the Functions
#f_callgemini_vertexai_vision("")