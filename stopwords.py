import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 


text=''
file_text=open('input.txt', 'r', encoding="utf-8")
text_res = open("output.txt", "w")
for line in file_text:
	text+=line
text_res = open("output.txt", "w")


punktuation = [".", ",", ";", "!", "?", "«", "»", "-"]

download_stopwords = stopwords.words('english') #стоп-слова
stop_text = []
tokens = word_tokenize(text)
for i in tokens:
	if i not in download_stopwords and i not in punktuation:
		stop_text.append(i)


tokens = word_tokenize(text)  #разбиение на слова
tok_sent = sent_tokenize(text) #разбиение на предложения

stemsPorter = []        #Стеммер Портера
porter = PorterStemmer()
for w in tokens:
    a = w
    w = porter.stem(w)
    if w != "":
        stemsPorter.append(w)

stems = []
stemmer = SnowballStemmer("english")     #Стеммер Snowball
for token in tokens:
    token = stemmer.stem(token)
    if token != "" and token not in punktuation:
        stems.append(token)
result=[]
text_split=text.split(" ")
for i in range (len(text_split)):
    result.append(text_split[i])
    if stems[i] not in punktuation:
        result.append(stems[i])



text_res.write("stopwords:")
text_res.write(str(stop_text))
text_res.write("\n")
text_res.write("\n")
text_res.write ("word_tokenize:")
text_res.write(str(tokens))
text_res.write("\n")
text_res.write("\n")
text_res.write("sent_tokenize:")
text_res.write(str(tok_sent))
text_res.write("\n")
text_res.write("\n")
text_res.write("stems:")
text_res.write(str(stems))
text_res.write("\n")
text_res.write("\n")
text_res.write("Количество слов:")
text_res.write(str(len(text_split)))
text_res.write("\n")
text_res.write("Процент стоп-слов:")
text_res.write(str(100-(len(stop_text)/(len(text_split)/100))))
text_res.write("\n")
text_res.write("\n")
text_res.write("Слово, основа:")
text_res.write(str(result))
text_res.close()
