import streamlit as st
import base64
from myfunctions.f_callstorage_utility import f_upload_image_tocloudstorage
from myfunctions.f_callgemini_vertexai import f_callgemini_vertexai_vision

st.header('🖼️ Analyze :red[Image] using :blue[Gemini] by :green[_Google_]', divider="rainbow")
st.write("Unleash the power of AI to unlock the hidden stories within your images. Introducing Gemini, a cutting-edge AI tool from Google that delves beyond pixels to uncover profound insights and reveal what words alone cannot express. Elevate your understanding of your images and discover new possibilities with the unparalleled power of AI analysis.")

tab1, tab2  = st.tabs(["Create Description of an Image", "Ask Questions about the Image"])

with tab1:
    st.subheader("Create Description of an Image.")  
    st.write("""
Upload a JPG, JPEG, or PNG image and receive a comprehensive, text-based account of its contents, tailored to capture key elements and nuances. Uncover hidden insights and enhance your understanding of visual data with the power of AI.""")
    st.caption("You can find a sample file from here: https://www.google.com - _(Right Click and select 'Save Link As...')_")  

    vFileExplainChosen = False
    vUploadedFile = st.file_uploader(
        "Choose a JPG, JPEG, PNG file (max 10 MB): \n\n", 
        accept_multiple_files=False, 
        key="vUploadedFile",
        type=["jpg", "jpeg", "png"])

    if vUploadedFile is not None:  # Check if a file has been uploaded
        file_size = len(vUploadedFile.getvalue())  # Now it's safe to call getvalue()
        if file_size > 10 * 1024 * 1024:  # Check file size
            st.error("File size exceeds 10 MB limit. Please upload a smaller file.")
        else:
            if vUploadedFile.type in ['image/png', 'image/jpeg']:
                vFileContent = base64.b64encode(vUploadedFile.read()).decode('utf-8')
                image_display = f'<img src="data:{vUploadedFile.type};base64,{vFileContent}" width="600">'
                st.markdown(image_display, unsafe_allow_html=True)
                st.write("File name of image file :", vUploadedFile.name  )
                vFileExplainChosen = True
            else:
                st.error("Unsupported file type. Please upload a JPG, JPEG, PNG file.")
    else:
        st.info("if you don't have a file to upload, you can download a sample file that is given above.")

    #Explain the Image
    vButtonPrompt = st.button("Explain the Image", type="primary", key="vButtonPrompt")
    vPrompt = """Composition: Describe the overall layout of the image, including the arrangement of objects, use of space, and any dominant lines or shapes.
Objects and Characters: Identify and describe the key objects and characters in the image, their appearance, relationships, and any symbolism they might represent.
Colors and Lighting: Analyze the use of color and lighting in the image, how they contribute to the mood and atmosphere, and any symbolic meaning they might hold.
Emotions and Themes: Discuss the emotions and themes evoked by the image, drawing connections to historical or cultural context, personal experiences, or broader philosophical ideas.
Style and Technique: If relevant, analyze the artist's style and techniques, how they contribute to the overall effect of the image, and any art historical references or movements it might evoke.
"""
    vPrompt += """
Please provide a comprehensive, text-based account of its contents, tailored to capture key elements and nuances relevant in relevent domains. 
Uncover hidden insights and enhance your understanding of visual data with the power of AI. Explain it with chain of thought and logic.
    """

    if vButtonPrompt and vPrompt and vFileExplainChosen:
        with st.spinner("Generating your Answer based on your Question about the Image..."):
            try:
                vFileLocation = f_upload_image_tocloudstorage(vUploadedFile)
                response = f_callgemini_vertexai_vision(vPrompt, vFileLocation)
                if response:
                    st.write("Your Result is:")
                    st.success(response)
                    st.balloons()
            except Exception as e:
                st.error(f"Sorry there are no results available for this question, please ask another question. The questions is not a clear prompt to understand or has responsible AI rules enforced by the model. Follow the sample prompt above as a guidance.")
                #st.error("Something went wrong. Please try again.")
                #st.error(e)
    else:
        st.warning("Please upload your document first before clicking on the Submit button.")

with tab2:
    #Ask Questions about the Image
    st.subheader("Ask Follow Up Questions to the Image.")  
    st.write("""
Get insights from your images with AI-powered follow-up questions. Simply upload a JPG, JPEG, or PNG image and ask your question about it. Our AI will analyze the image and generate follow-up questions, helping you uncover hidden information and gain a deeper understanding of the image/visual data that you've uploaded.
             """)
    st.caption("You can find a sample file from here: https://www.google.com - _(Right Click and select 'Save Link As...')_")  

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

    vSampleQuestion = "You are a media expert, please answer the question about the image based on your persona. Here is the question: What are the relevant insights that I can get from this image for my role?"
    vPromptAsk = st.text_area("Enter your Question about the Image, ensure you ask a question that is relevant to the image. You can delete the example question in the text box and enter your own question.", value=vSampleQuestion, key="vPromptAsk", height=200)
    vButtonAskQuestion = st.button("Ask your Question", type="primary", key="vButtonAskQuestion")
    if vButtonAskQuestion and vPromptAsk and vFileAskChosen:
        with st.spinner("Generating your Answer based on your Question about the image..."):
            try:
                vAskFileLocation = f_upload_image_tocloudstorage(vAskUploadedFile)
                response = f_callgemini_vertexai_vision(vPromptAsk, vAskFileLocation)
                if response:
                    st.write("Your Result is:")
                    st.success(response)
                    st.balloons()    
            except Exception as e:
                st.error(f"Sorry there are no results available for this question, please ask another question. The questions is not a clear prompt to understand or has responsible AI rules enforced by the model. Follow the sample prompt above as a guidance.")
    else:
        st.warning("Please ensure you already uploaded your document and entered your question before clicking on the Submit button.")
        vStatusFileUploaded = False