import streamlit as st 
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import Annotated
from langchain_core.prompts import HumanMessagePromptTemplate
from prompt import user_prompt
from dotenv import load_dotenv
load_dotenv()


class Message(BaseModel):
    description : str = Field(..., description="this is a description of users mood and feeling.")

class Mood(BaseModel):
    mood : str = Field( ..., description="this is a mood of user, like happy, sad, angry, etc.")
    intensity : int = Field(..., description="this is an intensity of users mood from 1 to 10.")
    suggestions : str = Field(..., description="this is a suggestions for user based on their mood and feelings. suggest some activities or ways to improve their mood.suggest in detail.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0.2
)

structured_llm = llm.with_structured_output(Mood)




st.set_page_config(page_title="Mood Tracker", page_icon=":smiley:", layout="wide")
st.title("Mood Tracker")

st.write("This app helps you track your mood and provides insights based on your feelings.")
user_message : Annotated[Message, Field(description="User's mood and feelings description")]  = st.chat_input("How are you feeling today?", key="user_input")

prompt = f"""
{user_prompt}

user message:
{user_message}

"""
container = st.container()

with container:
    if user_message is not None:
        st.write("### Analyzing your mood...")
        st.write(user_message)
        output = structured_llm.invoke( prompt )
        st.write("### Inferred Mood:")
        st.write(f"**Mood:** {output.mood}")
        st.write(f"**Intensity:** {output.intensity}")
        st.write(f"**Suggestions:** {output.suggestions}")
        st.write("---")