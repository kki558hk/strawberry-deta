from fastapi import FastAPI
from schemas.graphqlBase import schema,graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


