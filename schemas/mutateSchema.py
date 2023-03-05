import strawberry
from typing import Optional
from crud.crud import addPerson,addQuote,updatePerson,updateQuote,deletePerson


@strawberry.type
class AddedPerson:
    Name:Optional[str]
    ErrorMessage:Optional[str]

    def __init__(self, name:str,errMessage:str):
        self.Name = name
        self.ErrorMessage  = errMessage
        


@strawberry.type
class UpdatedPerson:
    Name:Optional[str]
    ErrorMessage:Optional[str]

    def __init__(self, name:str,errMessage:str):
        self.Name = name
        self.ErrorMessage  = errMessage

@strawberry.type
class DeletedPerson:
    Name:Optional[str]
    ErrorMessage:Optional[str]

    def __init__(self, name:str,errMessage:str):
        self.Name = name
        self.ErrorMessage  = errMessage

@strawberry.type
class UpdatedQuote:
    Name:Optional[str]
    Content:Optional[str]
    ErrorMessage:Optional[str]

    def __init__(self, name:str,content:str,errMessage:str):
        self.Content  = content
        self.Name = name
        self.ErrorMessage = errMessage;

@strawberry.type
class AddedQuote:
    Name:Optional[str]
    Content:Optional[str]
    ErrorMessage:Optional[str]

    def __init__(self, name:str,content:str,errMessage:str):
        self.Content  = content
        self.Name = name
        self.ErrorMessage = errMessage;

@strawberry.type
class Mutation:
    @strawberry.mutation
    def AddPerson(self,name:str,age:int,nationality:str,institution:str,title:str)->AddedPerson:
        added : AddedPerson
        try:
            ret = addPerson(name,age,nationality,institution,title);
            added = AddedPerson(ret["Name"],None)
        except Exception as e:
            added = AddedPerson(name,str(e))
        return added
               
    @strawberry.mutation
    def UpdatePerson(self,name:str,age:int,nationality:str,institution:str,title:str)->UpdatedPerson:       
        updated : UpdatedPerson
        try:
            ret  = updatePerson(name,age,nationality,institution,title);
            updated = UpdatedPerson(ret["Name"],None);
        except Exception as e:
            updated = UpdatedPerson(name,str(e));
        return updated

    @strawberry.mutation
    def DeletePerson(self,name:str) -> DeletedPerson:
        deleted : DeletedPerson
        try:
            ret = deletePerson(name);
            deleted = DeletedPerson(ret["Name"],None);
        except Exception as e:
            deleted = DeletedPerson(name,str(e));
        return deleted;

    @strawberry.mutation
    def AddQuote(self,name:str,content:str)->AddedQuote:
        addedQuote : AddedQuote
        try:
            ret = addQuote(name,content);
            addedQuote = AddedQuote(ret["Name"],ret["Content"],None)
        except Exception as e:
            addedQuote = AddedQuote(name,content,str(e))
        return addedQuote;

    @strawberry.mutation
    def UpdateQuote(self,key:str,name:str,content:str)->UpdatedQuote:
        updatedQuote : UpdatedQuote
        try:
            ret = updateQuote(key,name,content);
            updatedQuote  =UpdatedQuote(ret["Name"],ret["Content"],None);
        except Exception as e:
            updatedQuote  =UpdatedQuote(name,content,str(e));
        return updatedQuote;

