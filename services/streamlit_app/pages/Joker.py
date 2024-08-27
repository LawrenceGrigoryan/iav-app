import os
import streamlit as st
import requests

from utils.prompts import joke_prompt

st.set_page_config(
    page_title="Joker",
)

model_url = os.environ.get("MODEL_URL")

if 'generation_config' not in st.session_state:
    st.session_state.generation_config = {}

st.markdown("# AI Joker 🤡")


def upd_temperature():
     st.session_state.generation_config["temperature"] = st.session_state.temperature

    
def upd_top_p():
    st.session_state.generation_config["top_p"] = st.session_state.top_p
    
    
def upd_top_k():
    st.session_state.generation_config["top_k"] = st.session_state.top_k


temperature = st.slider(
     label="temperature",
     key="temperature",
     min_value=0.01,
     max_value=2.0,
     step=0.05,
     value=1.5,
     on_change=upd_temperature
)
top_p = st.slider(
     label="top_p",
     key="top_p",
     min_value=0.01, 
     max_value=1.0,
     step=0.05,
     value=0.95,
     on_change=upd_top_p)
top_k = st.slider(
     label="top_k",
     key="top_k",
     min_value=1,
     max_value=1024,
     step=1,
     value=128,
     on_change=upd_top_k)


if st.button("Generate a joke"):
     response_json = requests.post(
          url=model_url,
          json={"prompt": joke_prompt,
                "generation_config": st.session_state.generation_config}
     ).json()
     joke = response_json["response"]
     st.write(joke)
