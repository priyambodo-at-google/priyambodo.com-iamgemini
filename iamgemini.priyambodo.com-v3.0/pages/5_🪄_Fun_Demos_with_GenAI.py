#importing all the library
#import os
import streamlit as st
import base64
from myfunctions.f_callstorage_utility import f_upload_image_tocloudstorage
from myfunctions.f_callgemini_vertexai import f_callgemini_vertexai_vision

# from vertexai.preview.generative_models import (Content,
#                                                 GenerationConfig,
#                                                 GenerativeModel,
#                                                 GenerationResponse,
#                                                 Image, 
#                                                 HarmCategory, 
#                                                 HarmBlockThreshold, 
#                                                 Part)
# import vertexai
# PROJECT_ID = os.environ.get('GCP_PROJECT') #Your Google Cloud Project ID
# LOCATION = os.environ.get('GCP_REGION')   #Your Google Cloud Project Region
# vertexai.init(project=PROJECT_ID, location=LOCATION)

# #loading the models
# @st.cache_resource
# def load_models():
#     text_model_pro = GenerativeModel("gemini-pro")
#     multimodal_model_pro = GenerativeModel("gemini-pro-vision")
#     return text_model_pro, multimodal_model_pro

# def get_gemini_pro_text_response( model: GenerativeModel,
#                                   contents: str, 
#                                   generation_config: GenerationConfig,
#                                   stream=True):
    
    
#     safety_settings={
#         HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
#         HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
#         HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
#         HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#     }
    
    
#     responses = model.generate_content(prompt,
#                                        generation_config = generation_config,
#                                        safety_settings=safety_settings,
#                                        stream=True)

#     final_response = []
#     for response in responses:
#         try:
#             # st.write(response.text)
#             final_response.append(response.text)
#         except IndexError:
#             # st.write(response)
#             final_response.append("")
#             continue
#     return " ".join(final_response)

    
# def get_gemini_pro_vision_response(model, prompt_list, generation_config={},  stream=True):
#     generation_config = {'temperature': 0.1,
#                          'max_output_tokens': 2048
#                          }
#     responses = model.generate_content(prompt_list,
#                                        generation_config = generation_config,stream=True)
#     final_response = []
#     for response in responses:
#         try:
#             final_response.append(response.text)
#         except IndexError: 
#             pass
#     return("".join(final_response))

#text_model_pro, multimodal_model_pro = load_models()

#Starting to build the application
st.header("🔆 Google :red[Gen AI] :blue[Personal & Fun] :green[Use Cases]", divider="rainbow")

tab1, tab2 = st.tabs(["Let's Learn about You", "Let's Fly and Explore"])

#Build the deck too
with tab1:

    #Ask Questions about the Image
    st.header("Let Gen AI understand about You.")  
    st.write("""
Get insights from your images with AI-powered follow-up questions. Simply take your picture to to the camera or upload a JPG, JPEG, or PNG image and ask your question about it. Our AI will analyze the image and generate follow-up questions, helping you uncover hidden information and gain a deeper understanding of the image/visual data that you've uploaded.
             """)

    st.subheader("Option 1: Take a picture of yourself.")  

    #create a streamlit photo capture using camera and store this to local folder
    vPictureTaken = st.camera_input("Please take a picture of yourself and upload it in the next step.")
    #st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")    
    if vPictureTaken is not None:
        #st.image(vPictureTaken)
        #bytes_data = vPictureTaken.getvalue()
        #st.write(type(bytes_data))    
        st.success("Thank you, picture is successfully taken. Please continue to analyze the image now")

    st.subheader("Option 2: Choose a picture from your computer.")  

    st.caption("Or, You can find a sample file and download it from here: ")
    st.caption(" - https://www.google.com - _(Right Click and select 'Save Link As...')_")  

    vFileAskChosen = False
    vAskUploadedFile = st.file_uploader(
        "Choose a JPG, JPEG, PNG file (max 10 MB): \n\n", 
        accept_multiple_files=False, 
        key="vAskUploadedFile",
        type=["jpg", "jpeg", "png"])

    if vAskUploadedFile is not None:  # Check if a file has been uploaded
        file_size = len(vAskUploadedFile.getvalue())  # Now it's safe to call getvalue()
        if file_size > 10 * 1024 * 1024:  # Check file size
            st.error("File size exceeds 10 MB limit. Please upload a smaller file.")
        else:
            if vAskUploadedFile.type in ['image/png', 'image/jpeg', 'image/heic']:
                vFileContent = base64.b64encode(vAskUploadedFile.read()).decode('utf-8')
                image_display = f'<img src="data:{vAskUploadedFile.type};base64,{vFileContent}" width="600">'
                st.markdown(image_display, unsafe_allow_html=True)
                st.write("File name of image file :", vAskUploadedFile.name )
                vFileAskChosen = True
            else:
                st.error("Unsupported file type. Please upload a JPG, JPEG, PNG file.")
    else:
        st.info("if you don't have a file to upload, you can download a sample file that is given above.")


    st.subheader("Final Step: Choose your source image and analyze it.")  

    vDefaultQuestion = """
Analyze the uploaded image for potential emotional states or personality cues, please try to be as accurate as possible but put the fun and informal tones in your explanation. 

Provide the results in a table format with the following columns:
* **Aspect:** (General Information, People Analysis, Emotion Analysis, Similar Artist, Symbolism Search)
* **Our Analysis:** 
* **AI Level of Confidence:** (Low, Medium, High)

(for the General Information aspect: try to analyze and explain as detail as possible about the image? Get the basics down! Tell me where and when this might be happening, and if there's anything interesting going on.) 

(for the People Analysis aspect:If there are people in the image, how many people and what are the gender and estimated age? Also brief physical descriptions (hair color, build))

(for the Emotion Analysis aspect: try to explain as You are a psychology expert, please answer the question about the image based on your persona. Here is the question: What is the emotion now? Why do you think so? Please elaborate more from a psychology point of view? You're the shrink now! What's the emotional vibe? Be specific, and don't be afraid to reference some psychology basics to back it up.)

(for the Similar Person aspect: try to explain as You are a people expert, please answer the question about the image based on your persona. Here is the question: Who is the similar famous person who looks like this person? Then briefly explain about the person, the jobs, and why he/she is famous.)

(for the Symbolism Search aspect: Look for any objects or details that might be symbolic.  Do they seem positive, negative, or maybe a bit of both? Tell me why!")

    """

    innertab1, innertab2 = st.tabs(["Analyze Image", "Custom Question"])

    with innertab1:
        vSource_control1 = st.radio("Select the source of the image: \n\n",["Option 1: Your Taken Picture","Option 2: Your Uploaded Image"],key="vSource_control1",horizontal=False)
        vFileToAnalyze = None
        if vSource_control1 == "Option 1: Your Taken Picture":
            vFileToAnalyze = vPictureTaken
        elif vSource_control1 == "Option 2: Your Uploaded Image":
            vFileToAnalyze = vAskUploadedFile
        vButtonAskQuestion1 = st.button("Analyze the image now", type="primary", key="vButtonAskQuestion1")
        if vButtonAskQuestion1 and vDefaultQuestion and vFileToAnalyze:
            with st.spinner("Generating your Answer based on your picture taken..."):
                try:
                    vAskFileLocation1 = f_upload_image_tocloudstorage(vFileToAnalyze)
                    response1 = f_callgemini_vertexai_vision(vDefaultQuestion, vAskFileLocation1)
                    if response1:
                        st.write("Your Result is:")
                        st.success(response1)
                        st.balloons()    
                except Exception as e:
                    st.error(f"Sorry there are no results available for this question, please ask another question. The questions is not a clear prompt to understand or has responsible AI rules enforced by the model. Follow the sample prompt above as a guidance.")
        else:
            st.warning("Please ensure you already take your picture or uploaded your image before clicking on the Submit button.")
            vStatusFileUploaded = False                
    with innertab2:
        vSource_control2 = st.radio("Select the source of the image: \n\n",["Option 1: Your Taken Picture","Option 2: Your Uploaded Image"],key="vSource_control2",horizontal=False)
        vFileToAnalyze = None
        if vSource_control2 == "Option 1: Your Taken Picture":
            vFileToAnalyze = vPictureTaken
        elif vSource_control2 == "Option 2: Your Uploaded Image":
            vFileToAnalyze = vAskUploadedFile
        vCustomQuestion = st.text_area("Enter your Question about the Image, ensure you ask a question that is relevant to the image. You can delete the example question in the text box and enter your own question.", value=vDefaultQuestion, key="vCustomQuestion", height=200)
        vButtonAskQuestion2 = st.button("Analyze the image now", type="primary", key="vButtonAskQuestion2")
        if vButtonAskQuestion2 and vCustomQuestion and vFileToAnalyze:
            with st.spinner("Generating your Answer based on your uploaded image and questions..."):
                try:
                    vAskFileLocation2 = f_upload_image_tocloudstorage(vFileToAnalyze)
                    response2 = f_callgemini_vertexai_vision(vCustomQuestion, vAskFileLocation2)
                    if response2:
                        st.write("Your Result is:")
                        st.success(response2)
                        st.balloons()    
                except Exception as e:
                    st.error(f"Sorry there are no results available for this question, please ask another question. The questions is not a clear prompt to understand or has responsible AI rules enforced by the model. Follow the sample prompt above as a guidance.")
        else:
            st.warning("Please ensure you already take your picture or uploaded your image before clicking on the Submit button.")
            vStatusFileUploaded = False                

with tab2:
    st.write("Hi, it is in progress now to put it in this page")
    st.write("meanwhile you can access https://travel-gemini-2zlauh7jea-as.a.run.app/")
    