import os
import streamlit as st
import requests

model_url = os.environ.get("MODEL_URL")

st.markdown("# AI Joker 🤡")

if st.button("Generate a joke"):
     response_json = requests.post(model_url, json={"prompt": "generate a joke"}).json()
     joke = response_json["response"]
     st.write(joke)
