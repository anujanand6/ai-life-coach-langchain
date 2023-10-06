import os
import streamlit as st

# TODO: Add comments and docstrings
# TODO: Create career/wealth coach
# TODO: Add next steps to docs
# TODO: Add How to use page

# Decorator
def enable_chat_history(func):
    if os.environ.get("OPENAI_API_KEY"):
        # Clear chat history after switching coaches
        current_page = func.__qualname__
        # print('\nCurrent page:', current_page)
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
            # print('Session state current page:', st.session_state["current_page"], '\n')
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass

        # Display chat history on ui
        if "messages" not in st.session_state:
            display_welcome_msg()
        # FIXME: Display chat history in ui
        for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    # TODO: Figure out why this throws keyerror after refresh 
    # Temporary fix for "messages" key error (after refresh)
    if "messages" not in st.session_state:
        display_welcome_msg()
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)
    pass

def display_welcome_msg():
    st.session_state["messages"] = [{
        "role": "assistant", "content": "Welcome to WiseMind AI!"
        }]
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])
    pass

def configure_openai_api_key():
    try:
        # Obtain OpenAI API key from Streamlit secrets
        st.session_state['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
        os.environ['OPENAI_API_KEY']  = st.secrets['OPENAI_API_KEY']
        pass
    except KeyError:
        # Request user to provide api key
        openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            type="password",
            value=st.session_state['OPENAI_API_KEY'] if 'OPENAI_API_KEY' in st.session_state else '',
            placeholder="sk-..."
            )
        if openai_api_key:
            st.session_state['OPENAI_API_KEY'] = openai_api_key
            os.environ['OPENAI_API_KEY'] = openai_api_key
        else:
            st.error("Please add your OpenAI API key to continue.")
            st.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
            st.stop()
        return openai_api_key