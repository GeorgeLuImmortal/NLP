__author__ = 'user'
# bits from http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
# load_docs, process_docs and compute_vector by MK
import math
import itertools
from scipy import spatial
from collections import Counter

vector_dict = {}

#Just loads in all the documents
def load_docs():
 print("Loading docs...")
 doc1=('d1', 'Muffin is so delicious especially it is hot')
 doc2=('d2', 'My wife is happy when I bought her a cake')
 doc3=('d3', 'It is a very nice dissert shop with delicious cake and muffin')
 doc4=('d4', 'Muffin is so delicious especially it is warm')
 doc5=('d5', 'Muffin is so delicious especially it is cold')
 doc6=('d6', 'Cake is so delicious especially it is cold')
 doc7=('d7', 'Muffin is so delicious especially it is hot and using jam')
 doc8=('d8', 'Muffin is so delicious')
 return [doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8]

#Computes TF for words in each doc, DF for all features in all docs; finally whole Tf-IDF matrix
def process_docs(all_dcs):
 stop_words = [ 'of', 'and', 'on','in' ]
 all_words = []
 counts_dict = {}
 for doc in all_dcs:
    words = [x.lower() for x in doc[1].split() if x not in stop_words]
    words_counted = Counter(words)
    unique_words = list(words_counted.keys())
    counts_dict[doc[0]] = words_counted
    all_words = all_words + unique_words
 n = len(counts_dict)
 n=float(n)
 df_counts = Counter(all_words)
 compute_vector_len(counts_dict, n, df_counts)


#computes TF-IDF for all words in all docs
def compute_vector_len(doc_dict, no, df_counts):
  global vector_dict
  for doc_name in doc_dict:
    doc_words = doc_dict[doc_name].keys()
    wd_tfidf_scores = {}
    for wd in list(set(doc_words)):
        wds_cts = doc_dict[doc_name]
        wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)
        wd_tfidf_scores[wd] = round(wd_tf_idf, 4)
    vector_dict[doc_name] = wd_tfidf_scores

def get_cosine(text1, text2):
     vec1 = vector_dict[text1]
     vec2 = vector_dict[text2]
     combination = set(vec1.keys())|set(vec2.keys())            #form the union set of two sets
     for x in combination:                                     #if one dictionary don't have a counterpart word that in unionset,
         if x not in vec1:                                     #then add one and make its value 0
            vec1[x]=0.0
         if x not in vec2:
            vec2[x]=0.0
     
     list1=[]
     list2=[]
     for i in combination:
         list1.append(vec1[i])
         list2.append(vec2[i])
    
     return (1-spatial.distance.cosine(list1,list2))
     
         
     
         
        
     
     
     
        
    

#RUN
all_docs = load_docs()
process_docs(all_docs)




docs=['d1','d2','d3','d4','d5','d6','d7','d8']                          #put all documents into array
array=list(itertools.combinations(docs,2))                              #find all combinations of these documents                                     
p=len(array)                                                            #find the length of the array
for i in range(0,p):                                      
    print(get_cosine(array[i][0],array[i][1]))  #print all cosine similarity of combinations

