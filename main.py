from fastapi import FastAPI

app = FastAPI()

@app.get("/recipes")
async def read_recipes():
    return [{"id": 1, "title": "Spaghetti"}, {"id": 2, "title": "Tacos"}]
