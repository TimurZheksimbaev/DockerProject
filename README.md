# Docker and FastAPI project

### This is my first project using Docker 

---

## Project description:

- It is a simple FastAPI project which has two endpoints:
- root `/` and dogs `/dogs`
- root endpoint outputs text
- dogs endpoint displays random image of a dog, using this API https://random.dog/woof.json

### Project structure
```
.
└── Docker Project/
    ├── src/
    │   ├── main.py
    │   └── NetworkManager.py
    ├── templates/
    │   └── index.html
    ├── docker-compose.yaml
    ├── Dockerfile
    ├── Makefile
    ├── requirements.txt
    └── README.md
```
---

## *To start an application use `Makefile`*
    make all

*or*

    make build name=<name of image>
    make run name=<name of image>

> docker run command is defaulted to port 8000, if you use another port, then go to `Makefile` and manually change port binding


## *Go to your browser and use `localhost:8000`*
- root endpoint `localhost:8000/`
- dogs endpoint `localhost:8000/dogs`
- docs `localhost:8000/docs`
---
>*By default port is 8000, but you can change it how you want*
 
>*Just remember that if your app is using some port X you need to bind it to Dokcer run port* 
