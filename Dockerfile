#Steps: run "docker build -t dockerimage", then "docker run dockerimage"
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "docker_image.py"]
