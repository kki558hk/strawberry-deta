from fastapi import FastAPI
from schemas.graphqlBase import schema,graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/{query_str}")
async def fetchData(query_str):
  print(query_str)
  result = await schema.execute(query_str);
  return result.data;

@app.get("/")
def read_root():
    return {"Test": "HelloWorld"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


