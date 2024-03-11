import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
html_code = """
    I am Gemini: Where humans and AI join forces. Bridging the gap between human ingenuity and AI's boundless potential. I am Gemini fosters a collaborative environment where both can amplify each other's strengths. Unleash the power of this partnership and unlock possibilities never thought imaginable.
    """

def run():
    st.set_page_config(page_icon="static/usd.ico")
    st.markdown(vNoLabel, unsafe_allow_html=True)
    st.header('🥷 :red[I am Gemini]-v2 - ":blue[Human-AI] :green[Collaboration]"', divider="rainbow")
    st.caption("[https://iamgemini.priyambodo.com] | [https://iamrich.priyambodo.com] | [https://iamtelco.priyambodo.com]")
    st.write(html_code)
   
    st.markdown(
        """
        **👈 Select the menu from the sidebar** to start your experience. 
        """
    )
    st.image("static/iamgemini.jpg", width=700)
    #st.sidebar.success("Select the use cases that you would like to see above.")
    st.write("_(The logo image above is created by Google AI using Imagen 2 model.)_")

    st.write("""
    <div style="text-align:center;padding:1em 0;"> 
        <table style="width: 100%;">
        <tr>
            <th style="color: gray; text-align: left;">Current local time in</th>
            <th style="text-align: left;">Jakarta, Indonesia</th>
        </tr>
        <tr>
            <td colspan="2">
            <iframe src="https://www.zeitverschiebung.net/clock-widget-iframe-v2?language=en&size=medium&timezone=Asia%2FJakarta" width="100%" height="115" frameborder="0" seamless></iframe>
            </td>
        </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        This application is maintained by <b>Doddi Priyambodo</b> (priyambodo@google.com | doddi@bicarait.com)   
        App Name & latest Version: <b>IamTelco-v1.0</b>
        """, unsafe_allow_html=True
    )
    
if __name__ == "__main__":
    run()
