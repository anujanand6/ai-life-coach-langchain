import streamlit as st

st.set_page_config(page_title="Fitness Coach", page_icon="🏃🏽")
st.header('Fitness Coach')
st.write('Ask Rocky anthying related to fitness such as creating workout plans, meal plans, and much more!')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/anujanand6/ai-life-coach-langchain/blob/main/pages/1_%F0%9F%8F%83%F0%9F%8F%BD_Fitness_Coach.py)')

from CoachModels import FitnessCoach

if __name__ == "__main__":
    coach = FitnessCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write('Selected persona:', persona)
        coach.generate_system_prompt()
        coach.main()
