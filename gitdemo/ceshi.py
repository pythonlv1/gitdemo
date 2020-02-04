# coding=utf-8


a = {1:"a","q":"w","2":"123"}
for i in a:
    print(i)
    print(str(i)+":"+str(a[i]))


list = [1,4,3,7,12,9,56,19]
# 由小到大
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
# 由大到小
def bubble_sort1(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]<list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

# bubble_sort(list)
# print(list)
# bubble_sort1(list)
# print(list)

# 快速排序

def quick_sort(list,left,right):
    if left < right:
        mid = patition(list,left,right)
        quick_sort(list,left,mid-1)
        quick_sort(list,mid+1,right)
def patition(list,left,right):
    temp = list[left]
    while left < right:
        while left < right and list[right] > temp:
            right-=1
        list[left] = list[right]
        while left < right and list[left]<temp:
            left+=1
        list[right] = list[left]
    temp = list[left]
    return left

# 二分法查找

def binary_search(list,val):
    left = 0
    right = len(list)-1
    while left <= right:
        mid = (right+left)//2
        if list[mid] == val:
            return mid
        elif list[mid] < val:
            left = mid+1
        else :
            right = mid-1
    return

s = [1,2,3,4,5,12,9,10]
print(binary_search(s,10))
c = "asdfasdf"
c2 = c[:-1]
print(c2)
# 操作文件夹（库）
# 1.增 ：create database db1 charset ut-8;
# 2.删 : drop database db1
# 3.改 : alter database db1 charsetlatinl
# 4.查 : show databases

#  操作文件（表）
# 先切换到文件夹下 use db1
# 1.增 ：create table dt1(sno int primary kay auto_increment,sname varchar)
# 2.删 : drop table dt1;
# 3.改 : alter table t1 modify name char(2)
#       alter table t1 change name name1 char(3);
# 4.查 : show tables;

# 操作文件中的内容（记录）
# 1.增 ：insert into t1 values(sno,1),(sname,2);
        # insertinto t1(sno,sname,sex)values(%s%s%s);
# 2.删 : delete from t1 where id=1
# 3.改 : update t1 set sname = "sb" where id=1
# 4.查 : select * from t1 where id>2

    # 清空表：
    #     delete from t1; 如果有自增id，新增的数据，仍然会以删除前的最后一项作为起始
    #     truncate table t1;数据量大，删除速度比上一条快，直接从零开始