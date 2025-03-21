
FROM python:3.12
WORKDIR /app

#COPY C:\\Users\\Utilisateur\\Documents\\Docker\\requirements.txt ./
COPY requirements.txt /app
COPY api1.py /app

RUN echo 'Hello' && ls -al

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#RUN curl -sS http://0.0.0.0:5000/hello
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]

#RUN python api1.py
#CMD python api1.py
CMD ["python", "api1.py"]