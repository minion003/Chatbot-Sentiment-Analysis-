import openai
from openai import OpenAI
from typing import Optional

openai.api_key=('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')

client=OpenAI()
def get_api_response(prompt:str) -> Optional[str]==None :
    text:Optional[str]=None
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['USER','ASSISTANT']
        )
        print(response)
    except Exception as e:
        print("ERROR: ",e)

prompt="USER: HI there\n\nASSISTANT:Hi! How can I assist you today?"       
get_api_response(prompt)