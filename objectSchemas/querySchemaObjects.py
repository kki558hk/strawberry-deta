import strawberry
from typing import Optional

@strawberry.type
class Quote:
   PersonKey:str
   Content:str

   def __init__(self, personKey:str,content:str):
        self.Content  = content
        self.PersonKey = personKey

@strawberry.type
class People:
   Name:str
   Institution:str
   Title:str
   Age:int
   Nationality:str

   def __init__(self, name,institution,title,age,nationality):
        self.Name = name
        self.Age = age
        self.Institution = institution
        self.Nationality = nationality
        self.Title = title
#    @strawberry.field
#    def Quotes(self) ->  typing.List[Quote]:
#     #  Find From DB
#      return getQuoteByPerson(self.Name);