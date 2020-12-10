FROM python:3.7
EXPOSE 8080
WORKDIR /app
COPY . .
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \
                      libsndfile1
RUN apt-get install -y ffmpeg
RUN pip3 install -r requirements.txt
CMD streamlit run --server.port 8080 --server.enableCORS=false app.py
