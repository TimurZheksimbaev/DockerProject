all :; install compose

build :; docker build -t docker_fastapi_app .

run :; docker run -p 8000:8000 docker_fastapi_app

install :; pip install -r requirements.txt

compose :; docker compose up --build