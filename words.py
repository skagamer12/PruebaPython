from ast import arg
from itertools import count




def concatenate(*args):
    words_added=""
    c=0
    
    for a in args:
        
        if c == len(args)-1:
            words_added += a
        else:
            words_added += a+"-"
        c +=1
    print(words_added)
concatenate("I", "LOVE", "Python", "!", "COÑO")

