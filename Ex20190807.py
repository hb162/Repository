# bai 1+2:
list1 = [1, 5, 4, 2, 3, 6]


def tong_list():
    total = 0
    for i in list1:
        total += i
    print(f"total: {total}")


def tich_list():
    tich = 1
    for i in list1:
        tich *= i
    print(f"tich: {tich}")


def max_list():
    max_1 = list1[0]
    for i in list1:
        if i > max_1:
            max_1 = i
    return max_1


def min_list():
    min_1 = list1[0]
    for i in list1:
        if i < min_1:
            min_1 = i
    return min_1


print("--------bai 1,2---------")

tong_list()
tich_list()
gtln = max_list()
print(f"max:{gtln}")
gtnn = min_list()
print(f"min:{gtnn}")

# bai 3:Viết hàm đếm số lần xuất hiện các ký tự trong một String


def count_word(word):
    dict1 = {}
    for i in word:
        key = dict1.keys()
        if i in key:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1


print("---------bai 3----------")
print(count_word("Stringings"))
# bai 4: Viết hàm đếm số lần xuất hiện các từ đơn trong một String.


def single_word(string1):
    count = dict()
    str = string1.split(" ")
    for word in str:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


print("-------bai 4---------")
str1 = "tao co sung day ne, tao ban may a !"
print(single_word(str1))


# bai 5:Viết hàm đếm các chuỗi trong List các chuỗi thoả mãn
# Độ dài từ 2 trở lên
# Ký tự đầu tiên và ký tự cuối cùng của chuỗi giống nhau
list2 = ["Tran", "Dan", "cac", "VietNam", "aba"]


def count_string():
    count = 0
    for word in list2:
        n = len(word)
        if n >= 2 and word[0] == word[-1]:
            count += 1
    return count


print("-------bai 5-----------")
print(f"so tu thoa man: {count_string()}" )
# bai 6: Viết hàm sắp xếp tăng dần bởi phần từ cuối cùng trong một List các Tuple không rỗng


def sort_last(value):
    return value[-1]


print("---------bai 6---------")
list3 = [(1, ), (2, 0), (0, 1), (5, 2), (9, -1, 0)]
list3.sort(key=sort_last)
print(list3)

# bai 7: Viết hàm thay thế tất cả các ký tự giống ký tự đầu của một String thành $


def change_word(word):
    temp = word[0]
    word = word.replace(temp, "$")
    word = temp + word[1:]
    return word


print("-------bai 7----------")
print(change_word("HAY TRAO CHO ANH"))

