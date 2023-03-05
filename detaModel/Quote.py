from .Base import Base
import datetime
from dataclasses import dataclass
import sys


#Quotesテーブルとのデータ通信
class ConnectQuotes(Base):
 def __init__(self,name: str = 'Quotes'):
  super().__init__(name)