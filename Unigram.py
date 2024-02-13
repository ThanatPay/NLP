import math
from collections import defaultdict

class UnigramModel():
    def __init__(self, data):
        self.unigram_count = defaultdict(lambda: 0.0)
        self.word_count = 0
        self.vocab = set()
        for sentence in data:
            sentence +=  '|</s>'
            for w in sentence.split('|'):
                self.unigram_count[w] +=1.0
                self.word_count+=1
                self.vocab.add(w)
        self.unk_value = math.pow(len(self.vocab-1),-1)

    def word_prob(self, w):
        if self.unigram_count[w] > 0:
            return self.unigram_count[w]/(self.word_count)
        else:
            return self.unk_value
        
    def getLnValue(self, x):
        if x >0.0:
            return math.log(x)
        else:
            return math.log(self.unk_value) 
    
    def sentence_ln_prob(self, sentence):
        word = sentence.split('|')
        ln_prob = .0
        for i in range(0,len(word)):
            ln_prob +=(self.getLnValue(self.word_prob(word[i])))
        return ln_prob

    def perplexity(self,test):
        ln_prob  = .0
        word_count = .0
        for sentence in test:
            sentence += '|</s>'
            word_count += len(sentence.split('|'))
            ln_prob    += self.sentence_ln_prob(sentence)
        return math.exp(-ln_prob/word_count)
    
# data = ["ฉัน|ชอบ|กิน|ข้าวผัด",
#         "ฉัน|ชอบ|กิน|ข้าวผัดปู",
#         "ผม|ชอบ|กิน|ข้าวผัด"]
# model = UnigramModel(data)
# print(model.word_prob("ฉัน"))
# print(model.perplexity("ฉัน|ชอบ|กิน"))