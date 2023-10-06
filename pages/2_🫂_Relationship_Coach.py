import utils
import streamlit as st
from streaming import StreamHandler

st.set_page_config(page_title="Relationship Coach", page_icon="🫂", layout="wide")
st.header("Relationship Coach")
st.write("Navigate emotional and relational challenges with insights from Emma!")

from CoachModels.BaseCoachModel import BaseCoachModel
class RelationshipCoach(BaseCoachModel):
    def __init__(self):
        self.coach_type = "relationship_coach"
        super().__init__(self.coach_type)
        
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain(self.prompt_template)
        user_query = st.chat_input(placeholder=f"Ask me anything related to {self.get_placeholder_msg()}!")
        if user_query:
            utils.display_msg(user_query, "user")
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    coach = RelationshipCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write("Your coach persona:", persona)
        coach.generate_system_prompt()
        coach.main()
