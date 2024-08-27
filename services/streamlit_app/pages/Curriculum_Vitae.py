from pathlib import Path
import streamlit as st

cv_dir = Path(__file__).resolve().parents[1] / "static"

st.set_page_config(
    page_title="Curriculum Vitae",
)

with open(cv_dir / "lgrigorian_job_cv.md", "r") as file:
    cv_text_md = file.read()

with open(cv_dir / "lgrigorian_job_cv.pdf", "rb") as file:
    st.download_button(
        label="Download PDF",
        data=file,
        file_name="lgrigorian_job_cv.pdf",
        mime="application/pdf"
    )
    
st.markdown(cv_text_md)
