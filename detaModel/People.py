from .Base import Base
import datetime
from dataclasses import dataclass
import sys


#Quotesテーブルとのデータ通信
class ConnectPeople(Base):
 def __init__(self,name: str = 'People'):
  super().__init__(name)
