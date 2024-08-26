import streamlit as st

with open("./static/lgrigorian_job_cv.md", "r") as file:
    cv_text_md = file.read()

with open("./static/lgrigorian_job_cv.pdf", "rb") as file:
    st.download_button(
        label="Download PDF",
        data=file,
        file_name="lgrigorian_job_cv.pdf",
        mime="application/pdf"
    )
st.markdown(cv_text_md)
