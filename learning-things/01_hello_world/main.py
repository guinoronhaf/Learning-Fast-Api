from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {
            "message": "Hello, World!",
            "time": "Vasco",
            "dia": "hoje"
    }

@app.get("/sobre")
def sobre():
    return {
            "nome": "Guilherme",
            "idade": 85
    }
