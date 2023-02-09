FROM python:3.10

WORKDIR /app-python-practice
COPY requirements.txt /app-python-practice/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app-python-practice/requirements.txt

COPY . /app-python-practice/

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
