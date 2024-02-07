import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
title = soup.find(class_="title is-4 is-size-5-touch").text.replace("\n","")
print(title)
questionNo = soup.find(class_="subtitle has-text-weight-bold has-title-case cursor-pointer tooltip").text.replace("\n","")
print(questionNo)
question = soup.find(class_="single_fatwa__question text-justified").text.replace("\n","")
print(question)
answer = soup.find(class_="content").text.replace("\n","")
print(answer)

data=[[title,questionNo,question,answer,url ]]
data
df = pd.DataFrame(data,columns=['title','questionNo','question','answer','url'])
df
df.to_csv("scrapin.csv")

