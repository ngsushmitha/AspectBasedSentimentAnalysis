import pandas as pd
from collections import OrderedDict
msg=pd.read_csv('train_1500.txt',encoding="utf-8", names=['message','label'])
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
xtrain=msg.message
ytrain=msg.labelnum

msg1=pd.read_csv('test.txt', names=['message','label'])
msg1['labelnum']=msg1.label.map({'pos':1,'neg':0})
xtest=msg1.message
ytest=msg1.labelnum


from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
xtrain_dtm=cv.fit_transform(xtrain)
xtest_dtm=cv.transform(xtest)
df=pd.DataFrame(xtrain_dtm.toarray(),columns=cv.get_feature_names())

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(xtrain_dtm,ytrain)
pred=clf.predict(xtest_dtm)

from sklearn import metrics
print(metrics.confusion_matrix(ytest,pred))
print("precision",metrics.precision_score(ytest,pred))
print(metrics.recall_score(ytest,pred))
print("accuracy",metrics.accuracy_score(ytest,pred))

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
        for line in file:
            c=c+1
            line=[line]
            t=cv.transform(line)
            predicted=clf.predict(t)
            if predicted==1:
                p=p+1
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
    
print("Hotel Average Sentiment Values using NAIVE BAYES classifier")
print(hotel1_average)
print(hotel2_average)
print(hotel3_average)
print(hotel4_average)
rate1= round(((sum(hotel1_average))*5)/1100, 2)
rate2= round(((sum(hotel2_average))*5)/1100, 2)
rate3= round(((sum(hotel3_average))*5)/1100, 2)
rate4= round(((sum(hotel4_average))*5)/1100, 2)


with open('hotel1FeatureReviews.txt', encoding="utf-8") as f1:
    content1 = f1.readlines()
content1 = [x.strip() for x in content1] 


with open('hotel4FeatureReviews.txt', encoding="utf-8") as f2:
    content4 = f2.readlines()
content4 = [x.strip() for x in content4] 


with open('hotel3FeatureReviews.txt', encoding="utf-8") as f3:
    content3 = f3.readlines()
content3 = [x.strip() for x in content3] 


with open('hotel2FeatureReviews.txt', encoding="utf-8") as f4:
    content2 = f4.readlines()
content2 = [x.strip() for x in content2] 
