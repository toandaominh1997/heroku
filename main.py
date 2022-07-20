from fastapi import FastAPI
from sysinfo import get_systeminfo
app = FastAPI()

@app.get("/")
def hello():
    return get_systeminfo()
@app.get("/info")
def hello():
    return get_systeminfo()
