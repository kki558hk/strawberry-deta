from detaModel.People import *
from detaModel.Quote import *
import typing
from typing import Any
import json

def getAllPeople() ->Any:
    ppl = ConnectPeople();
    ret = ppl.get();
    return ret.items;

def getSinglePerson(name :str) ->dict:
    ppl = ConnectPeople();
    ret = ppl.get({"key" : name});
    retDic = ret.__dict__['_items'][0];
    return retDic;

def addPerson(name:str,age:int,nationality:str,institution:str,title:str) ->dict:
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
    return {"Name":name};

def updatePerson(name:str,age:int,nationality:str,institution:str,title:str) ->dict:
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
    return {"Name":ret["Name"]};

def deletePerson(name:str) ->dict:
    pppl = ConnectPeople();
    pppl.delete(name);
    qu = ConnectQuotes();
    ret = qu.get({"PersonKey" : name});
    for itm in ret.items:
        qu.delete(itm["key"]);
    return {"Name":name};


def getAllQuotes()->Any:
    qu = ConnectQuotes();
    ret = qu.get()
    return ret.items;

def getQuoteByPerson(name:str) ->Any:
    qu = ConnectQuotes();
    ret = qu.get({"PersonKey" : name});
    return ret.items;
    

def addQuote(name:str,content:str) ->dict:
    qu = ConnectQuotes();
    ret = qu.get({"PersonKey" : name});
    print(ret.count)
    dic = {"key":str(ret.count + 1) + name
    ,"PersonKey":name
    ,"Content":content
    ,"created_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ,"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
    qu.insert(dic)
    return {"Name" :name,"Content":content};

def updateQuote(key:str,name:str,content:str) ->dict:
    qu = ConnectQuotes();
    ret = qu.get({"key" :key});
    dic = {"key":key
    ,"PersonKey":name
    ,"Content":content
    ,"created_time":ret.items[0]["created_time"]
    ,"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
    updRet = qu.update(dic, key);
    return {"Name" :name,"Content":content};



        


    