'''
Viết chương trình C để tính cước điện thoại bàn cho một hộ gia đình với các thông số như sau:

            Phí thuê bao bắt buộc là 25 nghìn.

            600 đồng cho mỗi phút gọi của 50 phút đầu tiên.

            400 đồng cho mỗi phút gọi của 150 phút tiếp theo.

            200 đồng cho bất kỳ phút gọi nào sau 200 phút đầu tiên.
'''

input = int(input("Nhap so phut"))
print(type(input))

output = 25

if input <= 50:
    output = output + 600*input
elif input <= 200:
    output = output + 600*50 + 400*(input-50)
else:
    output = output + 600*50 + 400*150 + 200*(input-200)

print("Cuoc dien thoai la:", output)
