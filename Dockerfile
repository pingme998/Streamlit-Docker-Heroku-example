FROM python:3.8
EXPOSE $PORT
RUN pip install streamlit requests pandas
RUN pip install fake-useragent
RUN mkdir -p /root/.streamlit
COPY config.toml /root/.streamlit/config.toml
COPY app.py /var/dashboard/app.py
