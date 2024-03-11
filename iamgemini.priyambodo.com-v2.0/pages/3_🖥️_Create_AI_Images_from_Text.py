import streamlit as st
import time
from myfunctions.f_callimagen_vertexai import f_callimagen_createimage, f_callimagen_delete_local_image

st.header('🖥️ Create :red[Image] using :blue[Imagen 2] by :green[_Google_]', divider="rainbow")
st.write("Imagen 2, a powerful AI tool from Google, to unleash your creativity and generate unique images. With just a few words, you can bring your imagination to life, exploring artistic styles and creating visuals that were once impossible. So, dive into the world of AI-powered art and let Imagen 2 be your canvas.")

tab1, tab2  = st.tabs(["Create Image from Text (Free Prompt)", "Sample prompts for your inspiration"])

with tab1:
    #Ask Questions about the Image
    st.subheader("Create Image from Text (Free Prompt).")  
    st.write("""
            Simply write your prompt and get your image.
             """)
    st.caption("You can read the detail of the Google Imagen 2 model from here: https://deepmind.google/technologies/imagen-2/ ")  
    st.write("Sample Prompt: _A beautiful ice princess with silver hair, fantasy concept art style_")
    columns = st.columns(4)
    with columns[0]:
        st.image("./static/princess1.jpg")
    with columns[1]:
        st.image("./static/princess2.jpg")
    with columns[2]:
        st.image("./static/princess3.jpg")
    with columns[3]:
        st.image("./static/princess4.jpg")
    with st.expander("These are few prompts that you can use to get started:"):
        st.caption("""
        - A deliciuos bowl of pho from Vietnam. \n
        - A modern house on a coastal cliff, sunset, reflections in the water, bright stylized architectural magazine photo. \n
        - A studio portrait of a man with a grizzly beard eating a sandwich with his hands, dramatic skewed angles, photography, film noir. \n
        - A bottle of fresh apple juice with the word "Chilla" written on it, on a beautiful beach. Advertisement. \n
        - An abstract logo representing intelligence for an enterprise AI platform, "I am Gemini" written under the logo. 
        """)

    vSampleQuestion = "A delicious food of gado-gado from indonesia."
    vPromptFree = st.text_area("Enter your prompt here.", 
                               value=vSampleQuestion, key="vPromptFree", height=100)
    vButtonFree = st.button("Create your image", type="primary", key="vButtonFree")
    if vButtonFree and vPromptFree:
        with st.spinner("Generating your image based on your prompt..."):
            try:
                response = f_callimagen_createimage(vPromptFree)
                if response:
                    st.write("Congratulations! Your process is completed. Here are the results:")
                    time.sleep(5)
                    columns = st.columns(2)
                    with columns[0]:
                        st.image("./temp_donotdelete/{}1.png".format(response))
                        st.image("./temp_donotdelete/{}3.png".format(response))
                    with columns[1]:
                        st.image("./temp_donotdelete/{}2.png".format(response))
                        st.image("./temp_donotdelete/{}4.png".format(response))
                    time.sleep(5)
                    if f_callimagen_delete_local_image(response):
                        st.success("Your image is successfully deleted in cache after you generated.")
                        st.balloons()    
            except Exception as e:
                if f_callimagen_delete_local_image(response):
                    st.success("You can save the image to your local machine/gadget. Your image is successfully deleted in cache after you generated. ")
                st.error(f"Sorry there are no results available for this question, please ask another question. The questions is not a clear prompt to understand or has responsible AI rules enforced by the model. Follow the sample prompt above as a guidance.")
                #Check the sample prompt above.")
                #st.error(e)
    else:
        st.warning("Please ensure you already uploaded your image and entered your prompt before clicking on the Submit button.")    

with tab2:
    st.subheader("Sample prompts for your inspiration.")  
    st.write("""
            Simply write your prompt and get your image.
             """)
    st.caption("You can read the detail of the Google Imagen 2 model from here: https://deepmind.google/technologies/imagen-2/ ")  
    st.write("""
                - a deliciuos bowl of pho from Vietnam. \n
                - A beautiful ice princess with silver hair, fantasy concept art style. \n
                - A raccoon wearing formal clothes, wearing a top hat. Oil painting in the style of Vincent Van Gogh. \n
                - A mosaic-inspired portrait of a person formed by a collection of small, colorful tiles. \n
                - A modern house on a coastal cliff, sunset, reflections in the water, bright stylized architectural magazine photo. \n
                - Isometric 3d rendering of a car driving in the countryside surrounded by trees, bright colors, puffy clouds overhead. \n
                - A studio portrait of a man with a grizzly beard eating a sandwich with his hands, dramatic skewed angles, photography, film noir. \n
                - A bottle of fresh apple juice with the word "Doddi" written on it, on a beautiful beach. Advertisement. \n
                - A cup of coffee with the word "Google" written on its side, sitting on a wooden tabletop. Next to the cup of yogurt is a plate with toast and a glass of orange juice. \n
                - A clean minimal emblem style logo for an ice cream shop, cream background. \n
                - An abstract logo representing intelligence for an enterprise AI platform, "Vertex AI" written under the logo. \n
            """)