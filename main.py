
# #dictionaries

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as \
# expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     }


# for entity in programming_dictionary:
#     print(programming_dictionary[entity])
  

# # print(programming_dictionary["Bug"])    

# import math

# def calc_exp(a,b,c,d):
#     return (math.sqrt(a+b) + math.sqrt(c + d))/ (a**2 + c**2) 

# s = 0
# for i in range(2):
#     print(i)

def count_a_words(s):
    word_list = s.split(" ")
    a_word_list = []
    for word in word_list:
        if 'а' in word or "А" in word:
            a_word_list.append(word)      
    return a_word_list


print(count_a_words("настроение как дел пример новость ПАЛЬМА"))    