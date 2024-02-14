import math
from collections import defaultdict
from nltk import bigrams

class BigramModel():
    def __init__(self, data):
        self.unigram_count = defaultdict(lambda: 0.0)
        self.bigram_count = defaultdict(lambda: 0.0)
        self.vocab = set()
        for sentence in data:
            for w1, w2 in bigrams(sentence.split('|'), pad_right=True, pad_left=True): #None I go to school . None
                self.bigram_count[(w1,w2)] += 1.0
                self.unigram_count[w1] += 1.0
                self.vocab.add(w1)
        self.unk_value = math.pow(len(self.vocab),-1)

    def bigram_prob(self, bigram):
        if self.unigram_count[bigram[0]] > 0:
            return self.bigram_count[bigram]/self.unigram_count[bigram[0]]
        else:
            return self.unk_value
        
    def getLnValue(self, x):
        if x >0.0:
            return math.log(x)
        else:
            return math.log(self.unk_value) 
        
    def get_bigrams(self, sentence):
        return bigrams(sentence.split('|'), pad_right=True, pad_left=True)
    
    def sentence_ln_prob(self, sentence):
        return sum(self.getLnValue(self.bigram_prob(bigram)) for bigram in self.get_bigrams(sentence))

    def perplexity(self, test):
        ln_prob = 0
        bigram_count = 0
        for sentence in test:
            ln_prob += self.sentence_ln_prob(sentence)
            bigram_count += len(list(self.get_bigrams(sentence)))
        return math.exp(-ln_prob / bigram_count)
    
# data = ["ฉัน|ชอบ|กิน|ข้าวผัด",
#         "ฉัน|ชอบ|กิน|ข้าวผัดปู",
#         "ผม|ชอบ|กิน|ข้าวผัด"]
# model = BigramModel(data)
# print(model.perplexity("ฉัน|ชอบ|กิน"))