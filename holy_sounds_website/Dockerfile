FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app/
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
Expose 8000
CMD ["python", "manage.py", "runserver", 8000:800]
