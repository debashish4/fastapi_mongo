FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY . /test
WORKDIR /test
VOLUME /test/logs
ENV PYTHONPATH="${PYTHONPATH}:/test/app"
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
