import streamlit as st

st.set_page_config(
    page_title="AI Life Coach",
    page_icon='💬',
    layout='wide'
)

st.header("AI Life Coach built using Langchain and Streamlit")
st.write("""
[![view source code ](https://img.shields.io/badge/GitHub%20Repository-gray?logo=github)](https://github.com/anujanand6/ai-life-coach-langchain)
""")

st.write("""
         Welcome to AI Life Coach! 

         Here are a few coaches catering to different use cases:
         
         - **Fitness Health Coach**: A coach that plans your workouts, builds diet plans and helps you achieve your overall physical health goals.
         
         To explore sample usage of each coach, please navigate to the corresponding coach on the side.
""")