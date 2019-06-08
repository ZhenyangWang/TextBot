#! /usr/bin/env python

"""
Last updated on 2017-3-10
@author: ZhenyangWang
"""

from time import time

#creat the class
class Func(object):
    def __init__(self):
        print u'Welcome the usage, please input the file'

# define the function to output the high frequency words
    def test(self,txt):
        count = {}
        for word in open(txt).read().split():
            count[word] = count.get(word, 0) + 1
        word_freq = []
# traversing the dictionary into tuples
        for freq,word in count.items():  
            word_freq.append((word,freq))
        word_freq.sort(reverse = True)
# output the high frequency words
        for freq,word in word_freq[:Fword]:  
            print word

# define the function to calculate the frequence
    def counter(self,txt):
        wordList1 = open(txt).read().split()
# strip any punctuation marks and build modified word list start with an empty list
        wordList2 = []
        for word1 in wordList1:
            lastchar = word1[-1:]
# use a list of punctuation marks
            if lastchar in [",", ".", "!", "?", ";", ":", ")"]:
                word2 = word1.rstrip(lastchar)
            else:
                word2 = word1
# build a wordList of lower case modified words
            wordList2.append(word2.lower()) 
        freqDict = {}
        for word2 in wordList2:
            freqDict[word2] = freqDict.get(word2, 0) + 1
# create a list of keys and sort the list all words are lower case already
        keyList = freqDict.keys()
        keyList.sort()
 
        for key2 in keyList:
            print "%-10s %d" % (key2, freqDict[key2])

# the main function
if __name__ == '__main__':   
    t = time()
    txtreader = Func()
    Fword = 10
    print 'Top '+str(Fword)+' high frequency words:'
    txtreader.test('test.txt')
    print "Frequency of each word in the word list (sorted):"
    txtreader.counter('test.txt')
    print "Time consumed:"
    print time()-t


