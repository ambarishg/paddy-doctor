FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8501  
ENTRYPOINT ["streamlit","run"]
CMD ["paddyui_identity.py"]