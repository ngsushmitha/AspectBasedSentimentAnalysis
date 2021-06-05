import string
from textblob import TextBlob
import re
import json
hotel_ids=[]
with open('a_2.txt') as json_file:
    data = json.load(json_file)
    for p in data:
        for q, id in p.items():
            if q=='hotel_id' and id!=None:
                if id not in hotel_ids:
                    hotel_ids.append(id)
                    
print(hotel_ids)
        
with open('a_2.txt') as json_file:
    data = json.load(json_file)
    for i in hotel_ids:
        for p in data:
            for q, id in p.items():
                if q=='hotel_id' and id==i:
                    for p ,comment in p.items():
                        if  (p=='p_comment' or p=='n_comment') and comment!=None:
                            comment = re.sub(r'\n+', '',comment)
                            comment = re.sub(r'\d+', '',comment)
                            comment = comment.translate(str.maketrans("","", string.punctuation))
                
                            comment=comment.strip()
                            comment=comment.lower()
                
                            spell=TextBlob(comment)
                            comment=str(spell.correct())
                            
                            f = open(i+".txt", "a",encoding="utf-8")
                            f.write(comment)
                            f.write('\n')
                            f.close()
                