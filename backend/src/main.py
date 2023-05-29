from fastapi import FastAPI


app = FastAPI(
    title="Learning System"
)

@app.get("/")
def index():
    return "Index page"
