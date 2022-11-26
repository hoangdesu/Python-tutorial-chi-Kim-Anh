# List methods, Slicing & String vs List

# -- MORE STRING METHODS -- 
countries = ['vietnam', 'japan', 'korea', 'singapore', 'malaysia']

# explicit type inferrence: tự động nhận dạng data type
# implicit: int[]
# . dot notation: access more properties/fields and methods within an object

# print(countries.index('japan')) # make sure item exists in list

name = 'Hoang'
# print(name.upper())

# countries.clear() #abc123 # similar result to countries = [] # xyz456
# clear(): xóa toàn bộ phần tử trong chuỗi, giữ lại địa chỉ bộ nhớ (memory address)
# list = []: gán lại vào 1 list mới, ở tại địa chỉ mới

# count: đếm số lần xuất hiện của 1 phần tử trong list
# print('Count vietnam:', countries.count('vietnam'))

# sort: sắp xếp từ bé đến lớn (mặc định)
# truyền vào tham số reverse=True nếu muốn sắp xếp từ lớn đến bé
# countries.sort()

# reverse: đảo ngược thứ tự chuỗi
# print('Before:', countries)
# countries.reverse()

# extend: mở rộng trên list hiện tại. Tham số truyền vào phải là 1 LIST
countries.extend(['thailand', 'laos', 'cambodia'])

western_countries = ['usa', 'canada', 'england']
countries.extend(western_countries)

# copy: tạo 1 list mới
copied_country_list = countries.copy()

# print('Copied:', copied_country_list)

# -- SLICING -- 
# slicing: cắt

# new list = list[start index:stop index(:step)]

asian_countries = countries[:8] # tương tự countries[0:8]
# print('asian countries:', asian_countries)

english_speaking_countries = countries[8:] # tương tự countries[8:11]
# print('english speaking countries:', english_speaking_countries)

# đi ngược
reversed_countries_list = english_speaking_countries[2::-1]
# print('reversed:', reversed_countries_list)

# ex: 'cambodia', 'laos', 'thailand'
sea = countries[7:4:-1]
# print('sea:', sea)

favorite_countries = [countries[0], countries[3], countries[8], countries[10]]
# print('fav countries:', favorite_countries)

countries_1 = countries[1::3]
# print('countries 1:', countries_1)

# -- STRING VS LIST -- 

# string: array of characters

my_country = 'VIETNAM'

# access individual character using index
print(my_country[0]) # V

# can re-assign item in list
# countries[1] = 'china'

# đối với string: chỉ có thể access từng ký tự, KHÔNG reassign từng ký tự riêng lẻ được
# my_country[0] = 'B' # BIETNAM => không cho phép
# my_country = 'JAPAN'
# print(my_country)

# String slicing
introduction = 'my name is Hoang. I am from Vietnam'
name = introduction[11:16]
country = introduction[28:]
print('name:', name)
print('country:', country)

# access multiple levels
print(countries[1][2]) # 'japan' index 2 = p

# print('countries:', countries)

