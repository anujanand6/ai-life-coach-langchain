import streamlit as st


st.set_page_config(page_title="Docs", page_icon="📄")
st.title('Docs')
st.write('Some helpful documentation on the tools used to build this app')
st.subheader('Langchain')
st.write("""
        [Langchain](https://python.langchain.com/docs/get_started/introduction) is a powerful framework designed 
         to streamline the development of applications using Language Models (LLMs). It provides a comprehensive 
         integration of various components, simplifying the process of assembling them to create robust applications. 
         Leveraging the power of Langchain, the creation of chatbots becomes effortless.
         """)
st.subheader('OpenAI API')
st.write("""
        The [OpenAI API](https://platform.openai.com/docs/introduction) offers developers access to advanced language 
         models like GPT-3, enabling a myriad of applications from drafting content to coding assistance. With its 
         straightforward integration and scalable design, it caters to both small projects and enterprise solutions. 
         The API emphasizes safety by minimizing bias and allows users to customize interactions through tailored 
         prompts, ensuring dynamic and relevant outputs. This interface stands as a pivotal tool for harnessing the 
         latest in natural language processing advancements.
         """)
st.subheader('Steamlit')
st.write("""
        [Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy for developers to create 
         interactive web applications for machine learning and data science projects. Streamlit provides a rapid and 
         efficient way to convert data scripts into interactive web applications, making it popular among data scientists 
         and engineers who want to showcase their work or build prototypes without the overhead of full-stack development.
         """)