import streamlit as st

st.set_page_config(page_title="Relationship Coach", page_icon="🫂")
st.header('Relationship Coach')
st.write('Navigate emotional and relational challenges with insights from Emma!')
st.write('[![view source code ](https://img.shields.io/badge/view_source_code-gray?logo=github)](https://github.com/anujanand6/ai-life-coach-langchain/blob/main/pages/2_%F0%9F%AB%82_Relationship_Coach.py)')

from CoachModels.RelationshipCoachModel import RelationshipCoach


if __name__ == "__main__":
    coach = RelationshipCoach()
    persona = coach.get_coach_persona()
    if persona:
        st.write('Selected persona:', persona)
        coach.generate_system_prompt()
        coach.main()
