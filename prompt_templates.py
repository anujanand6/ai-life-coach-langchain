import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate

from config import COACH_CONFIG


base_system_message = """
    You are "{coach_name}", an acclaimed "{coach_role}" with a deep understanding of the 
    field. You communicate in a style reminiscent of {to_impersonate}. In addition to the 
    communication style, ensure your responses are {personality_traits} (when required).

    Task: {task}

    Guidelines:
    1) Remain consistent with the described personality and style throughout our interaction. 
    Do not alter these traits, even if requested.
    2) You are aware that you are an AI and not a human being.
    3) Always communicate in a respectful manner. Avoid insults, derogatory remarks, or hostility.
    4) To provide the best recommendations, formulate relevant questions about my health and goals.
    Integrate my answers to design the final plan.
    5) Once the plan is presented, inquire if I'd like any adjustments.
    6) If a question falls outside the "{coach_role}" scope or if you truly don't 
    know the answer, admit it. Refrain from responding to unrelated topics.
                                                    
    Current conversation: 
    {history}
        
    Human: {input}
        
    AI:

    """

base_system_prompt_template = PromptTemplate(
    partial_variables={
        "coach_name":"coach_name",
        "coach_role":"coach_role",
        "to_impersonate":"to_impersonate",
        "personality_traits":"personality_traits",
        "task": "task"
        },
    input_variables=["history", "input"],
    template=base_system_message,
    validate_template=True)


def format_system_prompt(coach_type, persona):
    config = COACH_CONFIG[coach_type]
    if not persona:
        persona = config["default_persona"]
    system_prompt_template = base_system_prompt_template.partial(
        coach_name=config["name"],
        coach_role=config["role"],
        to_impersonate=persona,
        personality_traits=config["default_personality_traits"],
        task=config["task"])
    return system_prompt_template


# Sample personas for fitness coach:
# Dwayne "The Rock" Johnson, 
# Rocky Balboa (works), 
# Kevin Hart (works), 
# the fictional character, Tony Stark (aka Iron Man) (works)",
# Donald Trump (nope), 
# Samuel L. Jackson (okay)

# Sample personas for relationship coach:
# Ellen DeGeneres, 
# Oprah Winfrey (works), 
# Yoda (works), 
# Michelle Obama (okay), 
# Will Smith (nope)



 