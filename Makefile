all: install compose

# build docker image, pass as a parameter image name
# for example: make build name=dokcer_app
build :
	docker build -t $(name) .

# run docker container, pass image name as parameter `name`
# for example: make run name=doker_app
run :
	docker run -p 8000:8000 $(name)

# install all libraries
install :
	pip install -r requirements.txt

# docker compose command
compose :
	docker compose up --build