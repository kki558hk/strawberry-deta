import strawberry
import typing
from typing import Optional
from crud.crud import getQuoteByPerson,getAllQuotes,getSinglePerson,getAllPeople
from objectSchemas.querySchemaObjects import Quote,People


@strawberry.type
class Query:
    @strawberry.field
    def AllPeople(self,ID: Optional[int] = None) -> typing.List[People]:
        #Query All
        return getAllPeople();
   
    @strawberry.field
    def SinglePerson(self,name: str) -> People:
        #  Query Single
        return getSinglePerson(name);
   
    @strawberry.field
    def AllQuotes(self) -> typing.List[Quote]:
        #  Query All
        return getAllQuotes();
   
    @strawberry.field
    def QuotesByPerson(self,name :str) -> typing.List[Quote]:
        #  Query By Param
        return getQuoteByPerson(name);