import streamlit as st

st.set_page_config(page_title="Relationship Coach", page_icon="🫂", layout='wide')
st.header('Relationship Coach')
st.write('Navigate emotional and relational challenges with insights from Emma!')

from CoachModels.RelationshipCoachModel import RelationshipCoach


if __name__ == "__main__":
    coach = RelationshipCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write('Your coach persona:', persona)
        coach.generate_system_prompt()
        coach.main()
