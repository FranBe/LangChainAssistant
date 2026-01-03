##########################################################
#
#
##########################################################

#-----------------       Libraries       -----------------

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os


#------------------     API KEY     ----------------------

# Necessary to get the API KEY
load_dotenv()

# Getting the API key string from file
gem_key = os.getenv("GEM_API_KEY")

print(gem_key)

print(type(gem_key))

#------------------     LLM     ----------------------

## LLM
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gem_key,
    temperature = 0.5
)


#-----------------       Program       -----------------


print("Write 'exit' to get out of here!")
while True:
    # Your turn
    user_input = input("You: ")

    # Exit chat
    if user_input == "exit":
        print("Thanks for talking with me!")     
        break
    
    # Interacting and getting response
    llm_input = [{"role":"user","content":user_input}]

    llm_response = llm.invoke(llm_input).content

    print(llm_response)

