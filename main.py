
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

# def count_a_words(s):
#     word_list = s.split(" ")
#     a_word_list = []
#     for word in word_list:
#         if 'а' in word or "А" in word:
#             a_word_list.append(word)      
#     return a_word_list


# print(count_a_words("настроение как дел пример новость ПАЛЬМА"))    


# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     if student_scores[student] > 90:
#         student_grades[student] = 'Outstanding'
#     elif  student_scores[student] > 80:
#         student_grades[student] = 'Exceeds Expectations' 
#     elif  student_scores[student] > 70:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'

# print(student_grades)


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
    new_country={}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities

    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)








