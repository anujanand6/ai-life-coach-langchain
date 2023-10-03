import utils
import streamlit as st
from streaming import StreamHandler

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from config import OPENAI_MODEL_CONFIG
from promptTemplates import relationship_template

st.set_page_config(page_title="Relationship Coach", page_icon="🫂")
st.header('Relationship Coach')
st.write('Navigate emotional and relational challenges with insights from Emma!')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/anujanand6/ai-life-coach-langchain/blob/main/pages/2_%F0%9F%AB%82_Relationship_Coach.py)')

class RelationshipCoach:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = OPENAI_MODEL_CONFIG['model_name']
        self.temp = OPENAI_MODEL_CONFIG['temperature']
    
    @st.cache_resource
    def setup_chain(_self):
        memory = ConversationBufferMemory()
        llm = ChatOpenAI(
            model_name=_self.openai_model, 
            temperature=_self.temp, 
            streaming=True
            )
        chain = ConversationChain(
            llm=llm, 
            prompt=relationship_template, 
            memory=memory, 
            verbose=True
            )
        return chain
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = RelationshipCoach()
    obj.main()
