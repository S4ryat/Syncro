from fastapi import FastAPI
from app.database import SessionLocal

app = FastAPI()

@app.get("/items/")
def read_items():
    # Code pour récupérer les éléments depuis la base de données ou un autre emplacement
    return {"message": "test"}
