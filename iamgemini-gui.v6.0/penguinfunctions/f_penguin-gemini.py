import os
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting

def f_init_vertexai():
    vPROJECT_ID = os.environ.get('GCP_PROJECT')          #Your Google Cloud Project ID
    vLOCATION = os.environ.get('GCP_REGION')             #Your Google Cloud Project Region
    vertexai.init(project=vPROJECT_ID, location=vLOCATION)

def f_call_geminipro_text(vPrompt: str, vTemperature=0.9,vMax_output_tokens=8192,vTop_p=0.95,vTop_k=40) -> str:
    vPrompt = vPrompt.strip().replace('"',"").replace("\n", " ").replace("\r", " ")
    model = GenerativeModel(
        "gemini-1.5-pro-002",
    )
    responses = model.generate_content(
        vPrompt,
        generation_config=generation_config,
        safety_settings=safety_settings,
        #stream=True,
        stream=False,
    )
    generation_config = {
        "max_output_tokens": vMax_output_tokens,
        "temperature": vTemperature,
        "top_p": vTop_p,
        "top_k": vTop_k,
    }
    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]
    # if we are using stream process, then uncomment this
    # for response in responses:
    #     print(response.text, end="")    
    #     hasil = hasil + response.text
    # return hasil
    # if we are not using stream process, then uncomment this
    return(responses.text)        

def f_call_geminipro_image(vPrompt: str, vFileLocation, vTemperature=0.9,vMax_output_tokens=8192,vTop_p=0.95,vTop_k=40) -> str:
    vPrompt = vPrompt.strip().replace('"',"").replace("\n", " ").replace("\r", " ")
    model = GenerativeModel(
        "gemini-1.5-pro-002",
    )
    responses = model.generate_content(
        [
            Part.from_uri(
                vFileLocation, mime_type="image/jpeg"
            ),
            vPrompt,
        ],
        generation_config=generation_config,
        safety_settings=safety_settings,
        #stream=True,
        stream=False,
    )
    generation_config = {
        "max_output_tokens": vMax_output_tokens,
        "temperature": vTemperature,
        "top_p": vTop_p,
        "top_k": vTop_k,
    }
    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]
    # if we are using stream process, then uncomment this
    # for response in responses:
    #     print(response.text, end="")    
    #     hasil = hasil + response.text
    # return hasil
    # if we are not using stream process, then uncomment this
    return(responses.text)        


if __name__ == "__main__":
    f_init_vertexai()