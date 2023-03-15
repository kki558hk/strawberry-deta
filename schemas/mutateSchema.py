import strawberry
from typing import Optional
from crud.crud import addPerson,addQuote,updatePerson,updateQuote,deletePerson
from objectSchemas.mutateSchemaObjects import AddedPerson,UpdatedPerson,AddedQuote,DeletedPerson,UpdatedQuote;


@strawberry.type
class Mutation:
    @strawberry.mutation
    def AddPerson(self,name:str,age:int,nationality:str,institution:str,title:str)->AddedPerson:
        return addPerson(name,age,nationality,institution,title);
               
    @strawberry.mutation
    def UpdatePerson(self,name:str,age:int,nationality:str,institution:str,title:str)->UpdatedPerson:       
        return updatePerson(name,age,nationality,institution,title);

    @strawberry.mutation
    def DeletePerson(self,name:str) -> DeletedPerson:
        return deletePerson(name);

    @strawberry.mutation
    def AddQuote(self,name:str,content:str)->AddedQuote:
        return addQuote(name,content);

    @strawberry.mutation
    def UpdateQuote(self,key:str,name:str,content:str)->UpdatedQuote:
        return updateQuote(key,name,content);


