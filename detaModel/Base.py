from deta import Deta,_Base,base
from .config import API_KEY
from typing import Optional

class Base:
    dt: _Base
    def __init__(self,name:str):
        self.getConnection(name);
   
    #@classmethod
    def getConnection(cls,conName:str):
        deta = Deta(API_KEY)
        cls.dt = deta.Base(conName)
    
    # 取得する処理
    def get(self,filter:str = None) -> base.FetchResponse:    
        if filter is None:
          return self.dt.fetch();
        else:
          return self.dt.fetch(filter);
    
    #INSERTする処理。
    def insert(self,content:dict) ->any:
        return self.dt.put(content);
    
    #更新する処理
    def update(self,content:dict,updKey:str) ->any:
        te = self.dt.put(content,updKey);
        return te
    
    #削除する処理
    def delete(self,key:str) -> any:
        return self.dt.delete(key)
    

#Quotesテーブルとのデータ通信
class People(Base):
 def __init__(self,name: str = 'People'):
  super().__init__(name)

#Quotesテーブルとのデータ通信
class Quotes(Base):
 def __init__(self,name: str = 'Quotes'):
  super().__init__(name)


      