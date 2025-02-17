FROM python:3.8
EXPOSE $PORT
RUN pip install streamlit requests pandas
RUN mkdir -p /root/.streamlit
COPY config.toml /root/.streamlit/config.toml
COPY web/app.py /var/dashboard/app.py
COPY streamlit.sh /streamlit.sh
RUN chmod +x /streamlit.sh
CMD /streamlit.sh
