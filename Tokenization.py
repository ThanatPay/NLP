from math import inf

class Tokenization:
    def __init__(self,vocab):
        self.vocab = vocab

    def maximal_matching(self, c):
        d = [[None]*len(c) for _ in range(len(c))]
        for i in range(len(c)):
            for j in range(i,len(c)):
                # BASE CASE 1
                if i==0 and j==0:
                    if c[i:j+1] in self.vocab:
                        d[i][j] = 1
                    else:
                        d[i][j] = inf
                # BASE CASE 2
                elif i==0 and c[i:j+1] in self.vocab:
                    d[i][j] = 1
                # Normal CASE
                elif c[i:j+1] in self.vocab:
                    #min d(k,i-1) where k = 0....i-1
                    min_d = inf
                    for k in range(i):
                        if d[k][i-1]<min_d:
                            min_d=d[k][i-1]
                    d[i][j] = 1+min_d
                # Normal CASE
                else:
                    d[i][j] = inf

        return d
    
    def backtrack(self, d):
        eow = len(d)-1 # End of Word position
        word_pos = [] # Word position
        for i in range(len(d)):
            last_col = [x[eow] for x in d if x[eow] is not None]
            min_index = last_col.index(min(last_col))
            word_pos.append((min_index,eow))
            eow = min_index -1
            if min_index == 0:
                break
        word_pos.reverse()
        return word_pos
    
    def print_tokenized_text(self, d, input_text):
        tokenized_text=[]
        for pos in self.backtrack(d):
            #print(pos)
            tokenized_text.append(input_text[pos[0]:pos[1]+1])

        print("|".join(tokenized_text))

# thai_vocab = ["ไ","ป","ห","า","ม","เ","ห","ส","ี",
#               "ไป","หา","หาม","เห","สี","มเหสี","!"]
# tokenize=Tokenization(thai_vocab)
# input_text = "ไปหามเหสี!"
# out = tokenize.maximal_matching(input_text)
# tokenize.print_tokenized_text(out,input_text)