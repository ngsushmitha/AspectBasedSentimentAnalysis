aspects = {
        "food": ['bread','cooking','cuisine','drink','food','meal','foodstuff','meat','snack','eatable','fruits','dish'],
        "location": ['location','place','area','neighborhood','spot', 'region','venue'],
        "amenities":[ 'amenitites','luxuries', 'conveniences', 'niceities','facility', 'comfort'],
        "staff": ['staff','team', 'official','work force','security','waiter','reception','servent','maid'],
        "cleanliness":['clean','sanitation','tidyness','neatness','fresh','organised'],
        "customer_support": ['help','support'],
        "quietness":['calm','silent','cool','quiet','patient'],
        "affordability":['cheap','affordable','expensive','lavish','extravagant','economical','feasible','budget'],
        "view":['view','look','scene','sight','landscape','panaroma','seascape','vision'],
        "payment":['payment','card','amount','bill','cheque','cash','money','deposit','refund'],
        "wifi":['wifi','internet','net','speed','network']
        }
flag=[]
hotels=["hotel1","hotel2","hotel3","hotel4"]
for hotel in hotels:
    file = open(hotel+".txt", "r", encoding="utf-8")  
    for line in file:
        for word in line.split():
            for i in aspects:
                for j in aspects[i]:
                    if j == word:
                        if i in flag:
                            continue
                        f = open(hotel+"_"+i+".txt", "a",encoding="utf-8")
                        f.write(line)
                        f.close()
                        flag.append(i)
        flag=[]
    file.close()     