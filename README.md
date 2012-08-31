Tokenizer
=========

Author      : mevinbabuc@gmail.com
Description : Sentimental analysis module for machine learning 
Developers  : ? 
__________________________________________________________________________________

Tokenizer uses python NLTK package to tokenize and filter them for irrelevant data and assigns sentimental value to the
sentenses .

Data Flow Diagram - Tokenizer
=============================

mysqldb => tweeets => tokenize => filter => word rating => mysqldb

Data Flow Diagram - Filter
=============================

remove links => stemming => remove punctuations and irrelevant characters 