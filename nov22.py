# List: array -> collection of similar items (element, value)

food = ['phở', 'cơm tấm', 'bánh cuốn']

# moi phan tu trong list la 1 bien rieng biet

# Access: ten_list[index] -> index starts from 0

print(food[1])

# Reassign:

food[1] = 'hủ tíu'
print(food[1])

# int numbers[] -> chỉ nhận int

# myself = ['Hoang', 27, True] # mặc dù python hỗ trợ, nhưng ko nên xài 
# => use another data structure: dictionary
# print(myself)

# shortcut: ctrl + /
# / forward slash (ra trước)
# \ backward slash (ra sau)

# List methods: 
    # method = function (hàm)

# Add item AT THE END of the list: .append(item)
food.append('bún riêu')
food.append('bánh tráng')

# Add item AT A SPECIFIC POSITON: .insert(index, item)
food.insert(0, 'bánh xèo')
food.insert(4, 'bánh canh')

# List length: get the total elements from the list -> int
# print(len(food))

# last index = len(list) - 1

# Pay attention to index out of range error
# print(food[7]) # error

# Remove item from a list AT THE END and return the item: .pop()
# food.pop()
removed_item = food.pop()
print('Removed item:', removed_item)

# students = ['a', 'b', 'c']
# absent_student = students.pop()
# print(students)
# print(absent_student)

# Remove item AT A SPECIFIC INDEX: .pop(index)
dinner = food.pop(0)
print('Dinner:', dinner)

# Remove item BY NAME: .remove(name)
food.remove('bánh canh')
# food.remove('cháo lòng') #error

# - chi xoa element dau tien tim duoc
# - neu ko tim duoc element, se bi loi

# Sử dụng keyword del để xóa phần tử (KHÔNG KHUYẾN KHÍCH)
del food[2]

print(food)
