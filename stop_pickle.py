#stop words pickling code!

import cPickle as pickle

stop=open("stop.txt")
stopwords=set()
stop.seek(0)
for word in stop.readlines():
    stopwords.update(word.split())

stop.close()
pickle.dump(stopwords,open('stopwords.p', 'wb'))