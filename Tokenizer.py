from re import sub,compile
import cPickle as pickle
from nltk import stem
from Queue import Queue
import threading
from collections import defaultdict

tweet_filter=compile(r'(@[A-Za-z0-9]+)|(\w+:\/\/\S+)|(#[^ ]+)')
word_normalize=compile(r'(\w)\1+') #remove repeating charecters
stop=pickle.load(open("stopwords.p",'rb')) #load stop words

#splits the data in files into lines and inserts them into work Queue
workq=Queue()

def make_Queue(filename):
    with open(filename,'rb') as file:
        for line in file.readlines():
            workq.put(line)

#extract the features and places them in Queues for word counting
processq=Queue()

class ThreadExtract(threading.Thread):
    def __init__(self,workq,processq,id):
        threading.Thread.__init__(self)
        self.workq=workq
        self.processq=processq
        self.id=id
    def run(self):
        while True:
            tuple=self.workq.get()
            #print "\nThreadExtract",self.id,self.workq.qsize(),"\n"
            temp=set(tweet_filter.sub("",word_normalize.sub(r'\1\1',tuple.lower())).split())
            for word in temp:
                tmp_word=stem.PorterStemmer().stem(word.strip('!,.:;/` '))
                if tmp_word not in stop:
                    self.processq.put(tmp_word)
            self.workq.task_done()


dic=defaultdict(int)
lock=threading.RLock()

#count the word frequency

class ThreadFreq(threading.Thread):
    def __init__(self,processq,id):
        threading.Thread.__init__(self)
        self.processq=processq
        self.id=id
    def run(self):
        #print "thread waiting for processq"
        while True:
            with lock:
                dic[processq.get()]+=1
                #print "\nThreadFreq",self.id,self.processq.qsize(),"\n"
            self.processq.task_done()

for i in range(5):
    t=ThreadExtract(workq,processq,i)
    t.setDaemon(True)
    t.start()

print "Started filling the Queue"
make_Queue("data.txt")
print "Queue full"

for i in range(5):
    tf=ThreadFreq(processq,i)
    tf.setDaemon(True)
    tf.start()

print "Processing data ..."
workq.join()
processq.join()
print "Finished Tokenizing.Saving data ..."
print "Only words with Frequency more than 1 are saved!"
posdic=defaultdict(int)

for word in dic:
    tmp=dic[word]
    if tmp > 1:
        posdic[word]=tmp

pickle.dump(posdic,open("datafrequency.p",'wb'))