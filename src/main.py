import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from NetworkManager import ImageLoader

app = FastAPI()
IMAGE_URLS = []

# api call takes time, that's why I make it before app starts
@app.on_event("startup")
async def make_api_call():
    global IMAGE_URLS
    loader = ImageLoader()
    IMAGE_URLS = loader.multithreaded_api_call()


@app.get("/")
async def root():
    return "Hello, it is my app using FastAPI and Docker"


@app.get("/dogs", response_class=HTMLResponse)
def get_dog(request: Request):
    templates = Jinja2Templates(directory="templates")
    data = {"title": "Funny dogs", "image": IMAGE_URLS[random.randint(0, 19)]}
    return templates.TemplateResponse("index.html", {"request": request, **data})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

