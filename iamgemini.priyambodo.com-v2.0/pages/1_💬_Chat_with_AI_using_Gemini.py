import streamlit as st
from myfunctions.f_callgemini_vertexai import f_callgemini_vertexai_text
import time

st.set_page_config(page_icon="image/usd.ico")

vNoLabel = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(vNoLabel, unsafe_allow_html=True)

def clear_chat():
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi..., I am a Gemini, a helpful chat bot. I can answer your question powered by Google Gen AI"}]

st.header("💬 :red[Ask] your :blue[Question] to :green[I am Gemini]", divider="rainbow")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I am Gemini. I can answer your question powered by Google Generative AI. You can ask me anything in your preferred language."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    context = """ ###You are "I am Gemini," a helpful AI chatbot powered by Google Generative AI.### 
    ##You are ready to engage in a conversation with a customer who has a question about any topic that customer wants to ask. 
    Provide a comprehensive, informative, and engaging response that addresses their needs and demonstrates your understanding of the topic. 
    Remember to maintain a friendly and helpful tone, adapt your language to the customer's level of expertise, and prioritize their satisfaction.##
    """
    context += "##Use the same language as the customer to respond to their question. Please answer this question based on the context given:##"
    prompt = context + prompt
    with st.spinner('Please wait for the answer from I am Gemini...'):
        try:
            response = f_callgemini_vertexai_text(prompt, vTemperature=0.9,vMax_output_tokens=1024,vTop_p=0.9,vTop_k=40) 
        except Exception as e:
            st.error(f"Sorry there are no results available for this question, please ask another question.")
            #st.error(e)

    msg = {"role": "assistant", "content": response}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").markdown(msg["content"])

if len(st.session_state.messages) > 1:
    st.button('Clear Chat', on_click=clear_chat)