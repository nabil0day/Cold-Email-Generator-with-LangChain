# import os
# from constants import openai_key
# from langchain.llms import OpenAI
# import streamlit as st

# from langchain import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.chains import SequentialChain 

# from langchain.memory import ConversationBufferMemory

# os.environ["OPENAI_API_KEY"]=openai_key

# #streamlit framwork

# st.title('Celebity Search Assistant')
# input_text = st.text_input('Search the topic you want')

# #Prompt Template 1
# first_input_prompt = PromptTemplate(
#     input_variables=['name'],
#     Template="Tell me about celebrity{name}"
# )

# #Memory
# person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
# dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
# descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')



# llm = OpenAI(temperature=0.8)
# chain = LLMChain(
#     llm=llm, Prompt = first_input_prompt, verbose=True,output_key='person', memory=person_memory
#     )


# #Prompt Template 2
# second_input_prompt = PromptTemplate(
#     input_variables=['person'],
#     Template="When was {person} born"
# )


# chain2 = LLMChain(
#     llm=llm, Prompt = second_input_prompt, verbose=True,output_key='dob', memory=dob_memory
#     )

# #Prompt Template 3
# third_input_prompt = PromptTemplate(
#     input_variables=['dob'],
#     Template="Mentioned 3 major events happened around {dob}in the world"
# )
# chain3 = LLMChain(
#     llm=llm, Prompt = third_input_prompt, verbose=True,output_key='description', memory=descr_memory
#     )

# ParentChain = SequentialChain(chains=[chain,chain2,chain3],input_variables= ['name'], output_variables = ['person','dob', 'description'], verbose=True)



# #OpenAI LLMS
# if input_text:
#     st.write(ParentChain({'name': input_text}))

#      with st.expander('Person Name'): 
#         st.info(person_memory.buffer)

#     with st.expander('Major Events'): 
#         st.info(descr_memory.buffer)