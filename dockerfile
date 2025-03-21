
FROM mysql:latest
WORKDIR /api3

COPY requirements3.txt /api3
COPY api3.py /api3
COPY mysql.sql /api3

RUN echo 'Hello' && ls -al

RUN apt-get -y update
RUN pip install --no-cache-dir -r requirements3.txt

EXPOSE 5000

#RUN curl -sS http://0.0.0.0:5000/hello
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

#RUN python api1.py
#CMD python api1.py
CMD ["python", "api3.py"]
