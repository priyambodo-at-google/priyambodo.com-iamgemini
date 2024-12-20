import streamlit as st
st.set_page_config(page_icon="image/usd.ico")
vNoLabel = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
html_code = """
    Boost your efficiency and unlock new possibilities with I am Gemini, the cutting-edge AI Application. Leveraging the power of Google Cloud Generative AI and Gemini technology.
    """
with st.sidebar:
   st.success("Choose the menu that you would like to explore above 👆")
   st.info("app version: IamGemini v2.0-STABLE")
   st.image("static/doddihead.png", width=200)
   st.error("This application is created and maintained by Doddi Priyambodo, with the help of Chisiella Alzena A.P.")

def run():
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.write("# About IamGemini")
    st.subheader("//powered by Google Cloud Generative AI!")
    st.write(html_code)
    st.write(
        """
        **This is the Technical Architecture** of IamGemini Application: 
        """
    )
    st.image("static/iamrich-arch.png")
    st.caption("the diagram is built with https://googlecloudcheatsheet.withgoogle.com/architecture")

    st.markdown("---")    

if __name__ == "__main__":
    run()