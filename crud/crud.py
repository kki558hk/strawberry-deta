from detaModel.People import *
from detaModel.Quote import *
from objectSchemas.querySchemaObjects import People,Quote
from objectSchemas.mutateSchemaObjects import AddedPerson,UpdatedPerson,DeletedPerson,AddedQuote,UpdatedQuote
import typing
from typing import Any
import json

def getAllPeople() ->typing.List[People]:
    ppl = ConnectPeople();
    ret = ppl.get();
    li = [];
    for itm in ret.items:
          p = People(itm['Name'],itm['Institution'],itm['Title'],itm['Age'],itm['Nationality']);
          li.append(p);
    return li;

def getSinglePerson(name :str) ->People:
    ppl = ConnectPeople();
    ret = ppl.get({"key" : name});
    retDic = ret.__dict__['_items'][0];
    p = People(retDic['Name'],retDic['Institution'],retDic['Title'],retDic['Age'],retDic['Nationality']);
    return p;

def addPerson(name:str,age:int,nationality:str,institution:str,title:str) ->AddedPerson:
   added:AddedPerson;
   try:
        pppl = ConnectPeople();
        dic = {"key":name,
            "Name":name,
            "Institution": institution,
            "Title":title,
            "Age":age,
            "Nationality":nationality,
            "created_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),
            "modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
        pppl.insert(dic);
        added = AddedPerson(name,None)
   except Exception as e:
        added = AddedPerson(name,str(e))
   return added;

def updatePerson(name:str,age:int,nationality:str,institution:str,title:str) ->UpdatedPerson:
    updated:UpdatedPerson
    try:
        pppl = ConnectPeople();
        upd = pppl.get({"key" : name});
        retDic = upd.__dict__['_items'][0];
        dic = {"key":name,
        "Name":name,
        "Institution": institution,
        "Title":title,
        "Age":age,
        "Nationality":nationality,
        "created_time":retDic["created_time"],
        "modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
        ret = pppl.update(dic, name);
        updated =UpdatedPerson(name,None);
    except Exception as e:
        updated =UpdatedPerson(name,str(e));
    return updated;

def deletePerson(name:str) ->DeletedPerson:
    deleted : DeletedPerson
    try:
        pppl = ConnectPeople();
        pppl.delete(name);
        qu = ConnectQuotes();
        ret = qu.get({"PersonKey" : name});
        for itm in ret.items:
          qu.delete(itm["key"]);
        deleted= DeletedPerson(name,None);
    except Exception as e:
        deleted = DeletedPerson(name,str(e));
    return deleted;


def getAllQuotes()->typing.List[Quote]:
    qu = ConnectQuotes();
    ret = qu.get();
    li = [];
    for itm in ret.items:
          q = Quote(itm["PersonKey"],itm["Content"]);
          li.append(q);
    return li;

def getQuoteByPerson(name:str) ->typing.List[Quote]:
    qu = ConnectQuotes();
    ret = qu.get({"PersonKey" : name});
    li = [];
    for itm in ret.items:
        q = Quote(itm["PersonKey"],itm["Content"]);
        li.append(q);
    return li;
    

def addQuote(name:str,content:str) ->AddedQuote:
    addedQuote : AddedQuote
    try:
        qu = ConnectQuotes();
        ret = qu.get({"PersonKey" : name});
        print(ret.count)
        dic = {"key":str(ret.count + 1) + name
        ,"PersonKey":name
        ,"Content":content
        ,"created_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        ,"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
        qu.insert(dic)
        addedQuote = AddedQuote(name,content,None)
    except Exception as e:
        addedQuote = AddedQuote(name,content,str(e))
    return addedQuote;   


def updateQuote(key:str,name:str,content:str) ->UpdatedQuote:
    updatedQuote : UpdatedQuote
    try:
        qu = ConnectQuotes();
        ret = qu.get({"key" :key});
        dic = {"key":key
        ,"PersonKey":name
        ,"Content":content
        ,"created_time":ret.items[0]["created_time"]
        ,"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
        updRet = qu.update(dic, key);
        updatedQuote  =UpdatedQuote(name,content,None);
    except Exception as e:
        updatedQuote  =UpdatedQuote(name,content,str(e));
    return updatedQuote;




        


    