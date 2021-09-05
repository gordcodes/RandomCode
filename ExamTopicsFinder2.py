import requests
from bs4 import BeautifulSoup
import re

pageNum = 1

#url = 'https://www.examtopics.com/discussions/microsoft/6'
#reqs = requests.get(url)
#soup = BeautifulSoup(reqs.text, 'html.parser')

urlList = []

#https://www.examtopics.com/discussions/microsoft/view/51251-exam-az-104-topic-1-question-42-discussion/

'''
urlList = ['/discussions/microsoft/view/57182-exam-az-104-topic-6-question-18-discussion/','/discussions/microsoft/view/38893-exam-az-104-topic-5-question-15-discussion/',
           '/discussions/microsoft/view/56296-exam-az-104-topic-6-question-41-discussion/','/discussions/microsoft/view/51251-exam-az-104-topic-1-question-42-discussion/',
           '/discussions/microsoft/view/38358-exam-az-104-topic-1-question-31-discussion/']
'''
'''
for x in urlList:
    #print(x)
    print(lambda x:'-'.join(x.split('-')[1:8]))
'''


'''
sortedList = sorted(urlList, key=lambda x:x.split('-')[1:8])

for item in sortedList:
    print(item)

#sortedList = sorted(urlList, key=lambda x: x.split("-")[1])
'''


pageNumber = 1

while pageNumber < 843:
    url = 'https://www.examtopics.com/discussions/microsoft/'+str(pageNumber)+'/'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        hrefLinks = link.get('href')
        hrefLinks = str(hrefLinks)
        match = re.search('.+-exam-az-104.+', hrefLinks)
        if match:
            urlList.append(hrefLinks)
    
    print(pageNumber)
    reqs.close()
    pageNumber = pageNumber + 1


sortedList = sorted(urlList, key=lambda x: x.split("-")[1:8])

for listElement in sortedList:
    print(listElement)
