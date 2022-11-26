# print() -> display
# get user input -> input()

# trả lời = input('câu hỏi?') 10 => "10"

# input() returns a string

# yourName = input('What\'s your name: ')

# print("Hello " + yourName + ". Nice to meet you!")

# birth_year = int(input("When were you born: ")) # str -> int

# age = 2022 - birth_year # int

# print("You are " + str(age) + " years old.")

# Variable naming conventions: quy tắc đặt tên biến
# - snake_case: this_is_a_very_long_variable_name (this is a very long variable name)
# - camelCase: thisIsAVeryLongVariableName
# - PascalCase: ThisIsAVeryLongVariableName (class)

# Variables:
# - must start with a letter
# - must NOT start with a number: student1 (OK), 1student (WRONG)
# - case-sensitive: student vs Student (DIFFERENT)
# - must NOT contain a space
# - must NOT contain a special character !@#%^&*()-+ (được sử dụng $, nhưng chỉ trong trường hợp đặc biệt)

# Conditionals: câu điều kiện
# if - elif - else

# balance = 1000
# mercedes = 8000

# if balance > mercedes:
#     # statement
#     print("Enough money to buy a Mercedes")
# else:  # ko cần điều kiện, xét tất cả trường hợp còn lại
#     print("Save more money")
    
# age = int(input("Nhập vào số tuổi của bạn: "))

# # Chained elif's
# if 1 <= age <= 12:
#     print("Baby")
# elif 13 <= age <= 18:
#     print("Teenager")
# elif 19 <= age <= 40:
#     print("Medior")
# else:
#     print("Senior")
    
# Evaluate to True or False

# = : dấu gán (assignment operator)

# comparison operators: > < >= <= 
# == : phép so sánh bằng
# != : ko bằng

# isRaining = False

# if isRaining == True:
#     print("Vô nhà")
# else:
#     print("Ra ngoài chơi")

# if isRaining:
#     print("Vô nhà")
# else:
#     print("Ra ngoài chơi")
    
# vacation = True

# if not vacation:
#     print("Work")
# else:
#     print("Vacation")
    
# Core -> Application -> Machine Learning

# Trợ lý thông minh

# -> Hỏi: bạn đến từ đâu
# vietnam: xin chào
# japan: konnichiwa
# france: bonjour
# korea: annyeong haseyo
# china: nihao
# all: hello
