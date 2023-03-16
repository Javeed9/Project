import streamlit as st    # for building the app UI


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

! git clone https://github.com/Javeed9/Project.git
!pip install llama-index
!pip install langchain

from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os
from IPython.display import Markdown, display

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 2000
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600 

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index.json')

    return index


        

def main():
    # Set the app title
    st.set_page_config(page_title='Psychological Counseling Chatbot')
    
    # Set the app heading
    st.title('Psychological Counseling Chatbot')
    
    # Add a brief description of the app
    st.write('This is a chatbot designed to act as a psychological counselor. Please enter your message in the text box below and the bot will respond.\n Enter i am satisifed with my care to stop')
    
    # Add a text input field for the user to enter their message
    user_input = st.text_input('Enter your message here:')
    
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    temp = "i am satisifed with my care"
    query = ""
    while query!=temp: 
        query = input("Prompt")
        response = index.query(query, response_mode="compact")
        st.write('Bot:', response.response)
    ask_ai()

os.environ["OPENAI_API_KEY"] = "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"
construct_index("/content/Project/data")
    
# Run the main function to start the Streamlit app
if __name__ == '__main__':
    main()
