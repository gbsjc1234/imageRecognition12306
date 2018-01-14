# -*- coding: UTF-8 -*-
def getAllWord():
    respoPath='../images/typeStr/000.txt'
    file=open(respoPath,'r')
    resultList=[]
    for line in file:
        try:
            strs=line.split(':')
            word=strs[0]
            resultList.append(word)
        except:
            print 'error'
    return resultList

def getMostMatchType(identifiedWord,allResult):
    matchWord = None
    maxCount=0
    for result in allResult:
        count=0
        for word in identifiedWord:
            if word in result:
               count+=1
        if count> maxCount:
            maxCount=count
            matchWord = result
    return matchWord

allWords=getAllWord()
word='沙包'
match=getMostMatchType(word,allWords)
print match