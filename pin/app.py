import database 
from database import * 

res= str(input('which kind security key would u need, that inclue with : \n number  \n, text, and  \n number_text : choose anyone : number and only  text content with 12 chracter \n and number_text content with 12 chracter : \n number_text reamin a highly strong security :'))
if res == 'number': 
    database.number()
elif res=='text':
    database.text()
elif res=='number_text':
    database.text_num()
else :
    print('invalid input : ')
    