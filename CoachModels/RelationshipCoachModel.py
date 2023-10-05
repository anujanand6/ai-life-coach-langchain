import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from config import OPENAI_MODEL_CONFIG, COACH_CONFIG
from prompt_templates import format_system_prompt


class RelationshipCoach:
    def __init__(self):
            self.coach_type = "relationship_coach"
            utils.configure_openai_api_key()
            self.openai_model = OPENAI_MODEL_CONFIG['model_name']
            self.temp = COACH_CONFIG[self.coach_type]['model_temperature']
    
    def setup_chain(_self, _prompt_template):
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
            "Before we begin, please choose the persona of the coach from the options given below. \
                Once chosen, the persona cannot be modified.", 
            self.get_persona_options(), 
            index=None
            )
        return self.selected_persona

    def get_persona_options(self):
        return COACH_CONFIG[self.coach_type]['persona_options']

    def get_placeholder_msg(self):
        return COACH_CONFIG[self.coach_type]['placeholder_msg']

    def generate_system_prompt(self):
        self.prompt_template = format_system_prompt(self.coach_type, self.selected_persona)
        pass

    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain(self.prompt_template)
        user_query = st.chat_input(placeholder=f"Ask me anything related to {self.get_placeholder_msg()}!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})