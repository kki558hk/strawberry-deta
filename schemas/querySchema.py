import strawberry
import typing
from typing import Optional
from crud.crud import getQuoteByPerson,getAllQuotes,getSinglePerson,getAllPeople

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

@strawberry.type
class Query:
    @strawberry.field
    def AllPeople(self,ID: Optional[int] = None) -> typing.List[People]:
        #Query All
        items  = getAllPeople();
        li = [];
        for itm in items:
          p = People(itm['Name'],itm['Institution'],itm['Title'],itm['Age'],itm['Nationality']);
          li.append(p);
        return li;
   
    @strawberry.field
    def SinglePerson(self,name: str) -> People:
        #  Query All
        retDic = getSinglePerson(name);
        p = People(retDic['Name'],retDic['Institution'],retDic['Title'],retDic['Age'],retDic['Nationality']);
        return p;
   
    @strawberry.field
    def AllQuotes(self) -> typing.List[Quote]:
        #  Query All
        items  = getAllQuotes();
        li = [];
        for itm in items:
          q = Quote(itm["PersonKey"],itm["Content"]);
          li.append(q);
        return li;
   
    @strawberry.field
    def QuotesByPerson(self,name :str) -> typing.List[Quote]:
        #  Query All
        items = getQuoteByPerson(name);
        li = [];
        for itm in items:
           q = Quote(itm["PersonKey"],itm["Content"]);
           li.append(q);
        return li;