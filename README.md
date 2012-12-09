Tokenizer
=========

Author      : mevinbabuc@gmail.com
Description : Tokenizes chunks of text efficiently using a producer comsumer threading architecture and stores the word frequency in a pickled dictionary
__________________________________________________________________________________

Tokenizer helps tokenize big chunks of data and save (pickle) the word frequency in a dictionary for NLP.Its best suitable for sentiment analysis and machine learning

Features
========

. Tokenize words
. Removes stop words
. Removes punctuations and irrelavant charecters like ( !@#$%& )
. Removes more than 2 repeatition of charecters in a text like heyyyy => heyy , yeaaaahh => yeaahh
. Removes links,#tags and @username references
. Removes numbers like 1, 12 but not words like g8 , n8 , m8 etc