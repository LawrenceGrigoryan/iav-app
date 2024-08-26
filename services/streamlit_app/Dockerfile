FROM python:3.11-slim
WORKDIR /streamlit_app
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .