# 元组和列表很像，都是用来保存多个数据
# 使用一队小括号() 来保存一个元组
# 元组和列表的区别在于列表是可变数据类型，而元组是不可变数据类型
words = ['hello', 'goog', 'hi', 'nihao']
nums = (1, 9, 3, 2, 5, 8, 9)

# 和列表一样，元组也是一个有序的存储数据的容器
# 元组也可以通过下标来获取数据
print(nums[3])  # 2
# nums[3] = 40 # 修改就会报错

# 元组的查询
print(nums.index(9))  # 查找元素的下标
print(nums.count(9))  # 查看元素出现次数

# 特殊情况：
# 如何表示只有一个元素的元组
age = (18)
age2 = (18,)
print(type(age), type(age2))

# 列表元组相互转换
words = ['hello', 'goog', 'hi', 'nihao']
print(tuple(words))  # 转元组

nums = (1, 9, 3, 2, 5, 8, 9)
print(list(nums))  # 转列表

heights = ("189", "174", "144")
print('*'.join(heights))

# 元组的遍历
nums = (1, 9, 3, 2, 5, 8, 9)
for i in nums:
    print(i)

# 元组可以使用+来合并
nums = (1, 9, 3, 2, 5, 8, 9)
nums1 = (10, 93, 31, 22, 51, 81, 91)
nums2 = nums+nums1
print(nums2)
