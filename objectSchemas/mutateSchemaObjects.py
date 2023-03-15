import strawberry
from typing import Optional



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