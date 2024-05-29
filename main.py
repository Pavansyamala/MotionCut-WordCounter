import time 
import string

class WordCounter:
    def __init__(self):
        
        self.user_input_text = input('Please enter Your Text to Count the Number of Words : ')
        self.user_input_text = self.user_input_text.lower()
        self.wordsCount = dict()
        self.totalWords = 0 
        self.uniqueWords = 0 
        self.word_counter() 

    def word_counter(self):
        punctuations = string.punctuation
        lines = self.user_input_text.split('.')
        for line in lines:
            words = line.split() 
            for word in words: 
                word = word.strip(punctuations)
                self.totalWords += 1 
                if len(word) == 0: 
                    continue
                elif self.wordsCount.get(word) is not None : 
                    self.wordsCount[word] += 1 
                else : 
                    self.wordsCount[word] = 1 
                    self.uniqueWords += 1 
        self.displayResult()
    
    def displayResult(self): 
        print("Total Number of Words in the Entered Text is : " , self.totalWords)
        print("Total Number of Unique Words in the Entered Text is : " , self.uniqueWords)
        print('Words Counter : \n\t')
        for key in self.wordsCount.keys() : 
            print(f'\t{key} : ' , self.wordsCount[key])

if __name__ == '__main__': 
    obj = WordCounter()