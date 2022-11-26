# print('Hello Python')

# Cách chạy file Python:
#     - New terminal
#     - "py fileName.py"
    
# Các lệnh trong terminal:
#     - mũi tên lên: quay lại lịch sử các lệnh đã sử dụng trước đó
#     - mũi tên XUỐNG: đi tới các lệnh mới
#     - Ctr + C: cancel current command
#     - tab: auto complete
    
# Steps:
# 1. Viết code
# 2. Save code (kiểm tra cái nút tròn mất chưa)
# 3. Chạy code
#     - nếu chưa chạy 1 lần: py tênfile.py (có thể sử dụng tab để auto complete)
#     - nếu chạy 1 lần: dùng mũi tên lên và enter để chạy

# print('Hello Python')

# INTRODUCTION TO PYTHON

# comment: ctrl + /

# print(): function dùng để output ra màn hình

# tab/enter để auto complete code

# print('python is fun')

# VARIABLE: BIẾN
# ten bien = gia tri

name = 'Hoang'  # string: chuỗi
born = 1995     # integer: số nguyên

print("Hello my name is " + name + ' and I was born in ' + str(born))
print('People say hello in Japan as "Konnichiwa"')

# Data types:
#     - Numbers:
#         - int: integer -> 0, -5, 12...
#         - float: số thập phân
#     - String: str: chuỗi -> 'tên', "tên" ''
#     - Boolean: bool: True/False
#     (- Byte: bytes)

PI = 3.1415962 # constant
banKinh = 15 # bán kính

area = banKinh**2 * PI # (5^2)*PI
print("Area of the circle is: " + str(area))

print(area)

# Type casting: biến đổi kiểu dữ liệu

# đây là màn hình của em