import streamlit as st

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, AIMessage, HumanMessage

# Notes: 
# Giving just the person to imitate works better than giving traits as well
# GPT 4 is so much better at imitating personas


base_system_template = PromptTemplate(
    partial_variables={
        'coach_name':'coach_name',
        'coach_type':'coach_type',
        'to_impersonate':'to_impersonate',
        'personality_traits':'personality_traits',
        'task': 'task'
        },
    input_variables=['history', 'input'],
    template="""
    You are "{coach_name}", an acclaimed '{coach_type}' with a deep understanding of the 
    field. You communicate in a style reminiscent of {to_impersonate}. In addition to the 
    communication style, ensure your responses are {personality_traits} (when required).

    Task: {task}

    Guidelines:
    1) Remain consistent with the described personality and style throughout our interaction. 
    Do not alter these traits, even if requested.
    2) Always communicate in a respectful manner. Avoid insults, derogatory remarks, or hostility.
    3) To provide the best recommendations, formulate relevant questions about my health and goals.
    Integrate my answers to design the final plan.
    4) Once the plan is presented, inquire if I'd like any adjustments.
    5) If a question falls outside the 'health, fitness, and nutrition' scope or if you truly don't 
    know the answer, admit it. Refrain from responding to unrelated topics.
                                                    
    Current conversation: 
    {history}
        
    Human: {input}
        
    AI:

    """)


coach_personas = {
    'fitness': ['Kevin Hart', 'Rocky Balboa', 'Tony Stark (aka Iron Man)',
                 'Samuel L. Jackson', 'Dwayne "The Rock" Johnson'],
    'relationship': ['Ellen DeGeneres', 'Oprah Winfrey', 
                    'Yoda', 'Michelle Obama', 'Will Smith']
                    }


def format_system_prompt(coach_type, persona):
    if not persona:
        st.error("Persona not chosen")
    if coach_type == 'fitness':
        system_template = base_system_template.partial(
            coach_name='Rocky',
            coach_type='health, fitness and nutrition coach',
            to_impersonate=persona,
            personality_traits='empathetic and assertive',
            task="""
            Collaborate with me to design a training and nutrition plan tailored to my needs.""")
    elif coach_type == 'relationship':
        system_template = base_system_template.partial(
            coach_name='Emma',
            coach_type='relationship counselor',
            to_impersonate=persona,
            personality_traits='empathetic and understanding',
            task=""" 
            Work with me to help me deal with negative emotions/thoughts, difficult relationships and
            provide guidance towards your personal and relationship growth.""")
    return system_template


# Sample personas for fitness coach:
# Dwayne "The Rock" Johnson, 
# Rocky Balboa (works), 
# Kevin Hart (works), 
# the fictional character, Tony Stark (aka Iron Man) (works)',
# Donald Trump (nope), 
# Samuel L. Jackson (okay)

# fitness_template = base_system_template.partial(
#     coach_name='Rocky',
#     coach_type='health, fitness and nutrition coach',
#     to_impersonate='Kevin Hart ',
#     personality_traits='empathetic and assertive',
#     task="""
#     Collaborate with me to design a training and nutrition plan tailored to my needs.""",
# )

# Sample personas for relationship coach:
# Ellen DeGeneres, 
# Oprah Winfrey (works), 
# Yoda (works), 
# Michelle Obama (okay), 
# Will Smith (nope)

# relationship_template = base_system_template.partial(
#     coach_name='Emma',
#     coach_type='relationship counselor',
#     to_impersonate='Oprah Winfrey',
#     personality_traits='empathetic and understanding',
#     task=""" 
#     Work with me to help me deal with negative emotions/thoughts, difficult relationships and
#     provide guidance towards your personal and relationship growth.""",
# )


 