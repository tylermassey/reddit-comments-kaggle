import re
import itertools
from nltk.corpus import stopwords

string = "hey. youre prettyyyyyy soooooooo ThisIsAwesome cool.\n lol\t i'm lee"

NO_APPOSTROPHE = { "youre" : "you are", "theyre" : "they are", "im" : "i am",
        "hes" : "he is", "shes" : "she is", "its" : "it is", "aint" : "am not",
        "arent" : "are not", "couldnt" : "could not", "doesnt" : "does not",
        "hasnt" : "has not", "hadnt" : "had not" }

APPOSTROPHE = { "s" : "is", "'re" : "are", "m" : "am", "ll" : "will",
        "d" : "had"}

def replace_two_or_more(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)


string = replace_two_or_more(string)
string = ' '.join(re.findall('[A-Z][^A-Z]*', string))
# string = ''.join(''.join(s)[:2] for _, s in itertools.groupby(string))

words = re.split(r'\W+', string) 


# words = [ APPOSTROPHE[x].split() if x in APPOSTROPHE else x for x in words]

print words

# words = [ APPOSTROPHE[x] if x in APPOSTROPHE or 
        # NO_APPOSTROPHE[x] if
        # x in NO_APPOSTROPHE else x for x in words]

#words = [ NO_APPOSTROPHE[x] if x in NO_APPOSTROPHE else x for x in words]


for i, word in enumerate(words) :

    print i
    print words

    if word in NO_APPOSTROPHE:
        print "in no_'"
        print word , " : ", NO_APPOSTROPHE[word]
        split_words = NO_APPOSTROPHE[word].split()
        words[i] = split_words[0]
        words.append(split_words[1])

    if word in APPOSTROPHE:
        print "in '"
        print words[i], " : ", APPOSTROPHE[word]
        words[i] = APPOSTROPHE[word]

words = [word for word in words if word not in stopwords.words('english')]
words = ' '.join(words)

print words
