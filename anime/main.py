import requests
import re
from bs4 import BeautifulSoup as bs
from datetime import datetime




def newani(n,m):
    try:
        req = requests.session()
        r = req.get('https://ani.gamer.com.tw/')

        source = bs(r.text,'html.parser')
        soup = source.find_all(class_='newanime-title')
        title=soup[n].text.strip()
       
        soup = source.find_all(class_='newanime-date')
        date = soup[n].text.strip()
        day = re.split('/',date)
        day=re.split(' ',day[1])
        
        soup = source.find_all(class_='newanime-vol')
        vol = soup[n].text.strip()
     
        #soup=source.find_all(class_="newanime__content__cover")
       # src = str(soup[n])
        #src = src.split('"')[5]
        
        result = str("<span>"+date+vol+"</span>"+"<h4>"+title+"</h4>")
        #if(day[0]==str(datetime.now().day)):
              # result = str("<span>"+date+vol+"</span>"+"<h4>"+title+"</h4>")
               #srcresult=src
        #else:
             #srcresult = "https://i.imgur.com/2FYaJGi.jpg"
        
        soup=source.find_all(class_="newanime__content")
        soup = str(soup[n])
        
        href = soup.split('"')[5]
        src =soup.split('"')[11]
        

        if(m==0):    
             return result
        elif(m==1):
             #return srcresult
             return src
        else:
             return href
       
    except :
        return "本日無更新"




    

