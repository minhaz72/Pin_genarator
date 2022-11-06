# pin genarator : 
# this will genrate some random pin for  your security : 
import random 
def number(): 
    a= random.randint(100000, 999999)
    
    print(a)
def text(): 
    ar=  ['azxore', 'bexhiu', 'caefgc' , 'efaced', 'fmoniq' , 'qrwasz', 'mlpwqa']
    
    re=random.choices(ar)
    print(re)

def text_num():
    arr=  ['azxore', 'bexhiu', 'caefgc' , 'efaced', 'fmoniq' , 'qrwasz', 'mlpwqa']
    a= random.randint(100000, 999999)
    b= str(a)
    c=  a+b 
    print(c)
    