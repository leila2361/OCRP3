nutrients = ['energy_100g','sugars_100g','saturated-fat_100g','fiber_100g','proteins_100g','sodium_100g',
               'fruits-vegetables-nuts_100g' ]

def nutri(data,code):
    nutriv = {}
    for name in nutrients :
        nutriv[name[:-5]]=data[data['code']==code][name].values[0]
    nutriv['sodium']*=1000
    return nutriv

def points_N_not_beverages(data,code):
    a = b = c = d = 0
    nutris=nutri(data,code)
    
    if(nutris['energy'] <= 335):
        a = 0
    elif(nutris['energy']<= 670):
        a = 1
    elif(nutris['energy'] <= 1005):
        a = 2
    elif(nutris['energy'] <= 1340):
        a = 3
    elif(nutris['energy'] <= 1675):
        a = 4
    elif(nutris['energy'] <= 2010):
        a = 5
    elif(nutris['energy'] <= 2345):
        a = 6
    elif(nutris['energy'] <= 2680):
        a = 7
    elif(nutris['energy'] <= 3015):
        a = 8
    elif(nutris['energy'] <= 3350):
        a = 9
    else:
        a = 10
         
        
    if(nutris['sugars'] <= 4.5):
        b = 0
    elif(nutris['sugars'] <= 9):
        b = 1
    elif(nutris['sugars'] <= 13.5):
        b = 2
    elif(nutris['sugars'] <= 18):
        b = 3
    elif(nutris['sugars'] <= 22.5):
        b = 4
    elif(nutris['sugars'] <= 27):
        b = 5
    elif(nutris['sugars'] <= 31):
        b = 6
    elif(nutris['sugars'] <= 36):
        b = 7
    elif(nutris['sugars'] <= 40):
        b = 8
    elif(nutris['sugars'] <= 45):
        b = 9
    else:
        b = 10
   
        
    if(nutris['saturated-fat'] <= 1):
        c = 0
    elif(nutris['saturated-fat'] <= 2):
        c = 1
    elif(nutris['saturated-fat'] <= 3):
        c = 2
    elif(nutris['saturated-fat'] <= 4):
        c = 3
    elif(nutris['saturated-fat'] <= 5):
        c = 4
    elif(nutris['saturated-fat'] <= 6):
        c = 5
    elif(nutris['saturated-fat'] <= 7):
        c = 6
    elif(nutris['saturated-fat'] <= 8):
        c = 7
    elif(nutris['saturated-fat'] <= 9):
        c = 8
    elif(nutris['saturated-fat'] <= 10):
        c = 9
    else:
        c = 10
    
    
    if(nutris['sodium'] <= 90):
        d = 0
    elif(nutris['sodium'] <= 180):
        d = 1
    elif(nutris['sodium'] <= 270):
        d = 2
    elif(nutris['sodium'] <= 360):
        d = 3
    elif(nutris['sodium'] <= 450):
        d = 4
    elif(nutris['sodium'] <= 540):
        d = 5
    elif(nutris['sodium'] <= 630):
        d = 6
    elif(nutris['sodium'] <= 720):
        d = 7
    elif(nutris['sodium'] <= 810):
        d = 8
    elif(nutris['sodium'] <= 900):
        d = 9
    else:
        d = 10
   
    return a, b, c, d


def points_N_beverages(data,code):
    a = b = c = d = 0
    nutris=nutri(data,code)
    
    if(nutris['energy'] <= 0):
        a = 0
    elif(nutris['energy']<= 30):
        a = 1
    elif(nutris['energy'] <= 60):
        a = 2
    elif(nutris['energy'] <= 90):
        a = 3
    elif(nutris['energy'] <= 120):
        a = 4
    elif(nutris['energy'] <= 150):
        a = 5
    elif(nutris['energy'] <= 180):
        a = 6
    elif(nutris['energy'] <= 210):
        a = 7
    elif(nutris['energy'] <= 240):
        a = 8
    elif(nutris['energy'] <= 270):
        a = 9
    else:
        a = 10
         
        
    if(nutris['sugars'] <= 0):
        b = 0
    elif(nutris['sugars'] <= 1.5):
        b = 1
    elif(nutris['sugars'] <= 3):
        b = 2
    elif(nutris['sugars'] <= 4.5):
        b = 3
    elif(nutris['sugars'] <= 6):
        b = 4
    elif(nutris['sugars'] <= 7.5):
        b = 5
    elif(nutris['sugars'] <= 9):
        b = 6
    elif(nutris['sugars'] <= 10.5):
        b = 7
    elif(nutris['sugars'] <= 12):
        b = 8
    elif(nutris['sugars'] <= 13.5):
        b = 9
    else:
        b = 10
   
        
    if(nutris['saturated-fat'] <= 10):
        c = 0
    elif(nutris['saturated-fat'] <= 16):
        c = 1
    elif(nutris['saturated-fat'] <= 22):
        c = 2
    elif(nutris['saturated-fat'] <= 28):
        c = 3
    elif(nutris['saturated-fat'] <= 34):
        c = 4
    elif(nutris['saturated-fat'] <= 40):
        c = 5
    elif(nutris['saturated-fat'] <= 46):
        c = 6
    elif(nutris['saturated-fat'] <= 52):
        c = 7
    elif(nutris['saturated-fat'] <= 58):
        c = 8
    elif(nutris['saturated-fat'] <= 64):
        c = 9
    else:
        c = 10
    
    
    if(nutris['sodium'] <= 90):
        d = 0
    elif(nutris['sodium'] <= 180):
        d = 1
    elif(nutris['sodium'] <= 270):
        d = 2
    elif(nutris['sodium'] <= 360):
        d = 3
    elif(nutris['sodium'] <= 450):
        d = 4
    elif(nutris['sodium'] <= 540):
        d = 5
    elif(nutris['sodium'] <= 630):
        d = 6
    elif(nutris['sodium'] <= 720):
        d = 7
    elif(nutris['sodium'] <= 810):
        d = 8
    elif(nutris['sodium'] <= 800):
        d = 9
    else:
        d = 10
   
    return a, b, c, d

                      
def F_not_beverages(data,code):
    fruit = nutri(data,code)['fruits-vegetables-nuts']
    if(fruit == -1): return -1
    elif(fruit <= 40): return 0
    elif(fruit <= 60): return 1
    elif(fruit <= 80): return 2
    else: return 5
    
def F_beverages(data,code):
    fruit = nutri(data,code)['fruits-vegetables-nuts']
    if(fruit == -1): return -1
    elif(fruit <= 40): return 0
    elif(fruit <= 60): return 2
    elif(fruit <= 80): return 4
    else: return 10

def points_P(data,code):
    a = b =  0
    nutris=nutri(data,code)
    
    
    if(nutris['fiber'] <= 0.9):
        a = 0
    elif(nutris['fiber'] <= 1.9):
        a = 1
    elif(nutris['fiber'] <= 2.8):
        a = 2
    elif(nutris['fiber'] <= 3.7):
        a = 3
    elif(nutris['fiber'] <= 4.7):
        a = 4
    else:
        a = 5
    
    
    
    if(nutris['proteins'] <= 1.6):
        b = 0
    elif(nutris['proteins'] <= 3.2):
        b = 1
    elif(nutris['proteins'] <= 4.8):
        b = 2
    elif(nutris['proteins'] <= 6.4):
        b = 3
    elif(nutris['proteins'] <= 8):
        b = 4
    else:
        b = 5
    return a,b
    
def nscore(data,code) :
    a,b =points_P(data,code)    
    if (data[data['code']==code]['categorie'].values[0]=='boissons'):
        neg=sum(points_N_beverages(data,code))
        maxF=10
        c=F_beverages(data,code)
        
    else :
        neg=sum(points_N_not_beverages(data,code))
        maxF=5
        c=F_not_beverages(data,code)
        
    if (neg>=11) and (c<maxF):
        return neg-(a+c)
    else :
        return neg-(a+b+c)
            
#la fonction ngrade n'est pas utilisable pour les produits considérées comme des eaux (gazeuses ou non, parfumees ou non)

def ngrade(data,code):
    score=data[data['code']==code]['nutrition-score-fr_100g'].values
    if (data[data['code']==code]['categorie'].values[0]=='boissons'):       
        if(score >= -99 and score <=1):
            return "b"
        elif(score >= 2 and score <= 5):
            return "c"
        elif(score >= 6 and score <= 9):
            return "d"
        elif(score > 10):
            return "e"
        
    else :
        if(score > -99 and score < -1):
            return "a"
        elif(score >= 0 and score <=2):
            return "b"
        elif(score >= 3 and score <= 10):
            return "c"
        elif(score >= 11 and score <= 18):
            return "d"
        elif(score > 18):
            return "e"

