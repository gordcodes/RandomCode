import urllib.request as urllib2





user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
     
headers = { 'User-Agent' : user_agent }



pageNum=1


textCounter=110

#findText='Exam Associate Cloud Engineer topic 1 question '+str(textCounter)+' discussion'


while textCounter<115:
    print('TextCounter = ',textCounter) #auditing
    findText='Exam Associate Cloud Engineer topic 1 question '+str(textCounter)+' discussion'


    while pageNum<45:
        #print('pageNumber = ',pageNum)
        URL='https://www.examtopics.com/discussions/google/'+str(pageNum)+'/'
        req = urllib2.Request(URL, None, headers)
        response = urllib2.urlopen(req)
        page = response.read()
        response.close()
        
        #print(pageNum) #auditing
    

        if findText in str(page):
            print(findText)
            print(URL)
            #print(pageNum)
            textCounter=textCounter+1
            pageNum=1
            print()
            print()
            print()
            break

        pageNum=pageNum+1

        
        if pageNum==45:
            textCounter=textCounter+1
            pageNum=1
            break


    






'''
while pageNum<45:
    URL='https://www.examtopics.com/discussions/google/'+str(pageNum)+'/'
    req = urllib2.Request(URL, None, headers)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    

    if findText in str(page):
        print(findText)
        print(pageNum)
        print()
        print()
        print()
        break

    pageNum=pageNum+1


if pageNum==45:
    print(findText)
    print("not on website")
    print()
    print()
'''