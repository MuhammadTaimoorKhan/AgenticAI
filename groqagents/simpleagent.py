from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

#tool
def sum(a,b):
    return a+b


tools = [
    {
        "type":"function",
        "function":{
            "name":"sum",
            "description":"This is a python function which perform addition of two numbers",
            "parameters":{
                "type":"object",
                "properties":{
                    "a":{"type":"integer","description":"a is the first value and must be a integer"},
                    "b":{"type":"integer","description":"b is the second value and must be a integer"}
                },
                "required":["a","b"]
            }
        }
    }
]
import json
def get_response(user_query):
    message = [
        {"role":"system","content":"You are an helpful ai assistant, your job is to answer user queries, your name is Taimuu"},
        {"role":"user","content":user_query}
    ]
    response = client.chat.completions.create(
      model="llama-3.3-70b-versatile",
      messages=message,
      tools=tools,
      tool_choice="auto"
    )
    tool_call = response.choices[0].message.tool_calls
    if tool_call:
        arguments = tool_call[0].function.arguments
        argument = json.loads(arguments)
        name = tool_call[0].function.name
        if name == "sum": 
            result = sum(**argument)
            return result
    return response.choices[0].message.content
response = get_response("what is the sum of 2 3 5")
print(response)