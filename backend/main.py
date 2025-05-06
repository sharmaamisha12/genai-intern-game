from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "🎮 Welcome to the Generative AI Guessing Game!"}

@app.head("/")
def head_root():
    # If someone sends a HEAD request to the root, they will get the headers without the body
    return {"message": "🎮 Welcome to the Generative AI Guessing Game!"}