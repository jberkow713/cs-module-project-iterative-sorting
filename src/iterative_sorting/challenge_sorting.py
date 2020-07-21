import word2number
from word2number import w2n

stringlist = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]


#print out all elements in this list divisible by 3



# any number with all 3s
# any number with all 3s or 6s or 9s or any combination 
# twelve
# 
#print(w2n.word_to_num('two point three'))

def word_to_num(arr):
    num_list = []
    for i in range(len(arr)):
        x = w2n.word_to_num(arr[i])
        if x % 3 == 0:
            num_list.append(x)
                        
    return (num_list)        

#arr[i] represents the actual word itself

print(word_to_num(stringlist))



#print(word_to_num(stringlist))     

#y = [w2n.word_to_num(i) for i in stringlist]
#z = [x for x in y if x % 3 == 0  ]
#print(z)


#for i in stringlist:
#    x = w2n.word_to_num(i)
#    
#    for number in range(len(x)):
#        if(number % 3 == 0):
#            return number
    

    
