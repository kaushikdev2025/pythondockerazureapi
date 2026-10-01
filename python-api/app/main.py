from fastapi import FastAPI

app = FastAPI(title="Python API")


@app.get("/")
def root():
    return {"message": "Hello Kaushik"}


@app.get("/health")
def health():
    return {"status": "healthy"}