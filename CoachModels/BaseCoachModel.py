import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from config import OPENAI_MODEL_CONFIG, COACH_CONFIG
from prompt_templates import format_system_prompt

# TODO: Cache resources for each user
# TODO: Add capability for user to add personas and traits

class BaseCoachModel:
    def __init__(self, coach_type):
            self.coach_type = coach_type
            utils.configure_openai_api_key()
            self.openai_model = OPENAI_MODEL_CONFIG['model_name']
            self.temp = COACH_CONFIG[self.coach_type]['model_temperature']
    
    def _setup_chain(_self, _prompt_template):
        memory = ConversationBufferMemory()
        llm = ChatOpenAI(
            model_name=_self.openai_model, 
            temperature=_self.temp, 
            streaming=True
            )
        chain = ConversationChain(
            llm=llm, 
            prompt=_prompt_template, 
            memory=memory, 
            verbose=True
            )
        return chain
        
    def get_coach_persona(self):
        self.selected_persona = st.selectbox(
            "Before we begin, please choose the persona of the coach from the options given. \
                Once chosen, the persona cannot be modified.", 
            self._get_persona_options(), 
            index=None
            )
        return self.selected_persona
    
    def generate_system_prompt(self):
        self.prompt_template = format_system_prompt(self.coach_type, self.selected_persona)
        pass

    def _get_persona_options(self):
        return COACH_CONFIG[self.coach_type]['persona_options']

    def _get_placeholder_msg(self):
        return COACH_CONFIG[self.coach_type]['placeholder_msg']

    def run(self):
      pass