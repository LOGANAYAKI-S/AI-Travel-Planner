import streamlit as st

st.set_page_config(
    page_title="AI Super Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Super Assistant")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "AI Chatbot",
        "Memory Chatbot",
        "Translator",
        "Live News"
    ]
)

if module == "Home":

    st.header("Welcome")

    st.write("This is a multi-feature AI application.")

elif module == "AI Chatbot":

    st.header("AI Chatbot Module")

    st.write("Chatbot feature coming soon.")

elif module == "Memory Chatbot":

    st.header("Memory Chatbot")

    st.write("Memory AI feature coming soon.")

elif module == "Translator":

    st.header("AI Translator")

    st.write("Translator feature coming soon.")

elif module == "Live News":

    st.header("Live AI News")

    st.write("News feature coming soon.")