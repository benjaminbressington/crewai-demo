import streamlit as st
from main import ContentStrategyCrew
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Content Strategy Details')
    topic = st.text_input("Main topic or theme for content strategy:")
    target_segments = st.text_area("Specific audience segments you are targeting:")
    content_focus = st.text_area("Any particular themes or messages to emphasize:")

if st.button('Get result'):
    if not topic or not target_segments or not content_focus:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Content Topic: {topic}\nTarget Segments: {target_segments}\nContent Focus: {content_focus}"
        content_strategy_crew = ContentStrategyCrew(inputs)
        result = content_strategy_crew.run()
        st.subheader("Results of your content strategy project:")
        st.write(result)
