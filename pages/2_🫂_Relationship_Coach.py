import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from config import OPENAI_MODEL_CONFIG, COACH_CONFIG
from prompt_templates import format_system_prompt

st.set_page_config(page_title="Relationship Coach", page_icon="🫂")
st.header('Relationship Coach')
st.write('Navigate emotional and relational challenges with insights from Emma!')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/anujanand6/ai-life-coach-langchain/blob/main/pages/2_%F0%9F%AB%82_Relationship_Coach.py)')

class RelationshipCoach:

    def __init__(self):
        self.coach_type = 'relationship_coach'
        utils.configure_openai_api_key()
        self.openai_model = OPENAI_MODEL_CONFIG['model_name']
        self.temp = OPENAI_MODEL_CONFIG['temperature']
        self.persona_options = COACH_CONFIG[self.coach_type]['persona_options']
    
    @st.cache_resource
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
        self.selected_persona = st.selectbox('Choose your coach persona', self.persona_options, index=None)
        return self.selected_persona
    
    def generate_system_prompt(self):
        self.prompt_template = format_system_prompt(self.coach_type, self.selected_persona)
        pass
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain(self.prompt_template)
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = RelationshipCoach()
    persona = obj.get_coach_persona()
    if persona:
        st.write('Selected persona:', persona)
        obj.generate_system_prompt()
        obj.main()
