import math

text_file = "text.txt"
train_file = "train.txt"
test_file = "test.txt"

alphabet = {}
bigram_dict = {}


def fill_alphabet():
    with open(text_file, encoding = 'utf-8', mode = 'r') as input_file: 
        text = input_file.read()

    for word in text.split():
        if (alphabet.get(word) == None):
            alphabet.update({word:0})
        else:
            alphabet[word]+=1
    
def form_bigram_dict():
    with open(train_file,encoding= 'utf-8', mode = 'r') as input_file:
        text = input_file.read()
    
    word_array = text.split()

    for i in range(len(word_array)-1):
        this_word = word_array[i]
        next_word = word_array[i+1]
        alphabet[this_word]+=1 # counting frequencies of words in train.txt

        if (bigram_dict.get(this_word)==None): # if there is no such word in bigram_dictionary
            bigram_dict.update({this_word:{next_word:1}})
        else:
            if (bigram_dict[this_word].get(next_word)==None): # if we have met a new combination with this_word
                bigram_dict[this_word].update({next_word:1})
            else:
                bigram_dict[this_word][next_word]+=1 # adding 1 to frequency

    alphabet[next_word]+=1


# returns P(word|prev_word) in float format (with application of Laplas smoothing)
def calc_prob(word,prev_word):
    prev_word_freq = alphabet[prev_word]
    if (bigram_dict[prev_word].get(word) == None):
        comb_freq = 0
    else:
        comb_freq = bigram_dict[prev_word][word]
    #todo: implement laplas smoothing
    return comb_freq/prev_word_freq
    

def calc_perplexion():
    with open(test_file,encoding= 'utf-8', mode = 'r') as input_file:
        text = input_file.read()

    word_array = text.split()
    prob_mult = 1

    for i in range(1,len(word_array)):
        word = word_array[i]
        prev_word = word_array[i-1]
        prob_mult*=1/calc_prob(word,prev_word)
    
    return prob_mult**(1/len(word_array))

    

fill_alphabet()
form_bigram_dict()

