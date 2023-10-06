import utils
import streamlit as st
from streaming import StreamHandler

st.set_page_config(page_title="Fitness Coach", page_icon="🏃🏽", layout='wide')
st.header("Fitness Coach")
st.write("Ask Rocky anything related to fitness such as creating workout plans, meal plans, and much more!")

from CoachModels.BaseCoachModel import BaseCoachModel
class FitnessCoach(BaseCoachModel):
    def __init__(self):
        self.coach_type = "fitness_coach"
        super().__init__(self.coach_type)

    @utils.enable_chat_history
    def run(self):
        chain = self._setup_chain(self.prompt_template)
        user_query = st.chat_input(placeholder=f"Ask me anything related to {self._get_placeholder_msg()}!")
        if user_query:
            utils.display_msg(user_query, "user")
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    coach = FitnessCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write("Your coach persona:", persona)
        coach.generate_system_prompt()
        coach.run()
