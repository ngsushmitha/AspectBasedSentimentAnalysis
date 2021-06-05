from collections import OrderedDict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
  
average_sentiment=OrderedDict()
hotel1_average=[]
hotel2_average=[]
hotel3_average=[]
hotel4_average=[]
list1=["hotel1","hotel2","hotel3","hotel4"]
list2=["affordability","amenities","cleanliness","customer_support","food","location","quietness","staff","view","payment","wifi"]
for i in list1:
    for j in list2:
        file = open(i+"_"+j+".txt", "r", encoding="utf-8") 
        p=0
        c=0
        for sentence in file:
            c=c+1
            vs = analyzer.polarity_scores(sentence)
            p+= vs["compound"]
        average_sentiment[i+"_"+j]=round((p/c)*100,2)
        file.close()
    if i=='hotel1':
        for p,q in average_sentiment.items():
            hotel1_average.append(q)
    if i=='hotel2':
        for p,q in average_sentiment.items():
            hotel2_average.append(q)
    if i=='hotel3':
        for p,q in average_sentiment.items():
            hotel3_average.append(q)
    if i=='hotel4':
        for p,q in average_sentiment.items():
            hotel4_average.append(q)
    average_sentiment={}
    
print("Hotel Average Sentiment Values using VADER classifier")
print(hotel1_average)
print(hotel2_average)
print(hotel3_average)
print(hotel4_average)