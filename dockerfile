
FROM python:3.12

WORKDIR /api3

COPY requirements3.txt /api3
COPY api3.py /api3
COPY mysql.sql /api3

RUN echo 'Hello' && ls -al

RUN apt-get -y update
RUN pip install --no-cache-dir -r requirements3.txt

EXPOSE 5000

CMD ["python", "api3.py"]




# ----------------
# OLD VERSION
# ----------------

# FROM mysql:latest
# WORKDIR /api3

# COPY requirements3.txt /api3
# COPY api3.py /api3
# COPY mysql.sql /api3

# RUN echo 'Hello' && ls -al

# RUN apt-get -y update
# RUN pip install --no-cache-dir -r requirements3.txt

# EXPOSE 5000

# CMD ["python", "api3.py"]
