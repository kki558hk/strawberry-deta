import csv
from deta import Deta
from detaModel.Quote import *
from detaModel.People import *
from crud.crud import *
from detaModel.config import *

ret = getAllPeople();

# # Initialize with a Project Key
quote = ConnectQuotes();
ppl = ConnectPeople();

nowtime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S");
csv_file = open(CSV_PATH+"/people.csv", "r", encoding="ms932")
#リスト形式
f = csv.reader(csv_file,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
cnt:int
cnt = 0
for row in f:
    p= {"key":row[0],"Name":row[0],"Institution": row[2],"Title":row[3],"Age":row[1],"Nationality":row[4],
    "created_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
    dp = vars(p);
    ppl.insert(dp);
csv_file.close()

csv_file_quote = open(CSV_PATH+"/quotes.csv", "r", encoding="ms932")
fq = csv.reader(csv_file_quote,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
headerq = next(fq)
print(headerq)
qid:int
qid = 0;
for row in fq:
    pplres = ppl.get({"Name" : row[0]});
    pplKeyDict = pplres.items[0];
    pplKey = pplKeyDict['key'];
    q = {"key":str(ret.count + 1) + row[0]
    ,"PersonKey":row[0]
    ,"Content":row[1]
    ,"created_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ,"modified_time":datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}
    qd = vars(q);    
    quote.insert(qd);
    qid= qid +1;


print('終了');



