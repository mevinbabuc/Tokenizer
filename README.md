Tokenizer
=========

###### Author      : mevinbabuc@gmail.com
###### Description : Tokenizes chunks of text efficiently using a producer comsumer threading architecture and stores the word frequency in a pickled dictionary
__________________________________________________________________________________


## Features

* Tokenize words
* Removes stop words
* Stems the word using NLTK Lancaster stemmer i.e playing => play , played => play
* Removes punctuations and irrelavant charecters like ( !@#$%& )
* Removes more than 2 repeatition of charecters in a text like heyyyy => heyy , yeaaaahh => yeaahh
* Removes links,#tags and @username references
* Removes numbers like 1, 12 but not words like g8 , n8 , m8 etc

## Using Tokenizer

* The data to be processed is assumed to be saved in a file called __*data.txt*__.
* The stopwords.p contains basic stop words.
* Custom stop words list could be created by writting the words line by line in a __*stop.txt*__ file and running the __*stop_pickle.py*__ script
* If u dont need to remove stop words create an empty __*stopwords.p*__ file and save it in the same directory as *Tokenizer.py* or remove the appropriate code from Tokenizer.py

## File Formats

1. __*data.txt*__
	* Write each data line by line
2. __*stop.txt*__
	* Write each word in a line
	* Run the stop_pickle.py script to pickle *stop.txt* file to *stopwords.p* file