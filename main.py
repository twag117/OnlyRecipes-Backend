import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/recipes")
async def read_recipes():
    return [{"id": 1, "title": "Spaghetti"}, {"id": 2, "title": "Tacos"}]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
