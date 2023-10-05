import streamlit as st

st.set_page_config(page_title="Fitness Coach", page_icon="🏃🏽", layout='wide')
st.header('Fitness Coach')
st.write('Ask Rocky anything related to fitness such as creating workout plans, meal plans, and much more!')

from CoachModels.FitnessCoachModel import FitnessCoach

if __name__ == "__main__":
    coach = FitnessCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write('Your coach persona:', persona)
        coach.generate_system_prompt()
        coach.main()
