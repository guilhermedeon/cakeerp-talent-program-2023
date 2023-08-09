'''
1. Criar um arquivo main.py que contenha um endpoint de "/status" que retorna o seguinte
JSON: {"status": "it's alive"}.
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
async def return_status():
    return {"status" : "It's alive!"}
