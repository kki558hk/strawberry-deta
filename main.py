from fastapi import FastAPI
from schemas.graphqlBase import schema,graphql_app
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.add_middleware(
    CORSMiddleware, allow_headers=["*"], allow_origins=["*"], allow_methods=["*"]
)

