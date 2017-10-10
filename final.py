from __future__ import division
import os
import collections
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
import glob

def tokenize(docTerms):
    stopset = open("C:\\Users\\manoj\\Desktop\\IRWS\\Crawling\\stopwords.txt").read().split()
    ps = PorterStemmer()
    line = re.sub('(<.*?>)', ' ' , docTerms)
    returned_terms = []
    for word in line.split():
        for i in ['(', ')', '*','?', ':', ';', ',', '.', '!', '/', '"', "'",""''"",'_', '[',']','!','/','@','#','$','%','^','&','*',',','{','}','+','=','-','|','1','2','3','4','5','6','7','8','9']:
            word = word.replace(i,"")
        word=word.strip()
        word = word.lower()
        word = ps.stem(word)
        is_stop = False
        for stop_word  in stopset:
            if(word ==stop_word):
               is_stop = True 
        if len(word.strip()) > 0 and is_stop == False:
            returned_terms.append(word)

    return returned_terms

def dic_doc_selection(search_string, documents):
	document_titles = documents.keys()
	list_of_documents = [documents[x] for x in document_titles]
	#list of consine_similarities of each document
	cos_similarity = cal_cos_sim(search_string,list_of_documents)
	#return document_titles[cos_similarity.index(max(cos_similarity))]
	results = sorted(zip(cos_similarity,document_titles),key=lambda x:x[0],reverse=True)
	return results
    
def cal_cos_sim(search_string, list_documents):
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    tfs = vectorizer.fit_transform([search_string] +list_documents)
    return cosine_similarity(tfs[0:1],tfs)[0][1:].tolist()
 
urls = []       
urls = open("C:\\Users\\manoj\\Desktop\\IRWS\\Crawling\\urls.txt").read().split()

if __name__ == "__main__":
    datasetPath = "C:\\Users\\manoj\\Desktop\\IRWS\\Crawling\\Crawledurls\\"
    data =  dict((x,open(x).read().decode('utf8','ignore')) for x in glob.glob(datasetPath+"*"))
    results=dic_doc_selection(raw_input("Enter the query:"),data)
    for item in results[:5]:
		path=item[1].split("\\")[-1].split(".")[0]
		print "Please wait for few minutes. Sorry for keeping you wait."
		print urls[int(path)]
		 
