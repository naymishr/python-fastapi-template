from fastapi import FastAPI

app = FastAPI()

# List of countries (you can expand this list as needed)
countries = [
    "United States", "Canada", "United Kingdom", "Germany", "France",
    "Japan", "Australia", "Brazil", "India", "China"
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/countries")
def get_countries():
    return {"countries": countries}