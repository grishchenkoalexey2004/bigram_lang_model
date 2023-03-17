from math import ceil
import matplotlib.pyplot as plt


text_file = "text.txt"
train_file = "train.txt"
test_file = "test.txt"

alphabet = {}
#number of unique words in the text
#set in fill_alphabet function
alphabet_len = 0 
# number of words in training text
train_corpus_len = 0

def fill_alphabet():
    with open(text_file, encoding = 'utf-8', mode = 'r') as input_file: 
        text = input_file.read()

    for word in text.split():
        if (alphabet.get(word) == None):
            alphabet.update({word:0})

    global alphabet_len 
    alphabet_len = len(alphabet)
    
def form_unigram_dict():
    with open(train_file,encoding= 'utf-8', mode = 'r') as input_file:
        text = input_file.read()
    
    word_array = text.split()
    global train_corpus_len
    train_corpus_len = len(word_array)

    for i in range(len(word_array)):
        this_word = word_array[i]
        alphabet[this_word]+=1 # counting frequencies of words in train.txt


# returns P(word|prev_word) in float format (with application of Laplas smoothing)
def calc_prob(word,smooth_param):
    word_freq = alphabet[word] # getting the freq of word in train text

    if (word_freq == 0):
        return 1/(train_corpus_len + smooth_param*alphabet_len) # since c(wi|wi-1) = 0, c(wi-1) = 0
    
    else:
        return (word_freq+1*smooth_param)/(train_corpus_len+alphabet_len*smooth_param)
    

def calc_perplexion(smooth_param):
    with open(test_file,encoding= 'utf-8', mode = 'r') as input_file:
        text = input_file.read()

    word_array = text.split()
    warray_len = len(word_array)
    prob_mult = 1

    for i in range(len(word_array)):
        word = word_array[i]
        prob_mult*=(1/calc_prob(word,smooth_param))**(1/warray_len)
    
    return prob_mult



fill_alphabet()
form_unigram_dict()

smooth_param = 0.01
min_result = 10000000

param_arr = []
result_arr  = [] 

while (smooth_param<=1):
    param_arr.append(smooth_param)
    result = calc_perplexion(smooth_param)
    result_arr.append(result)
    smooth_param+=0.01
    

# visualization part

plt.axis([0,1,0,max(result_arr)])
plt.title('Зависимость перплексии от параметра сглаживания')
plt.plot(param_arr,result_arr,'ro')
plt.show()
