from django.test import TestCase

# Create your tests here.
# import re
# a='q2431'
# res=re.findall(r'^[A-Za-z]_.*\d+$',a)
# print(res)
#
#
# def bubble_sort_1(li):
#     for i in range(len(li)-1):
#         exchange=False
#         for j in range(len(li)-i-1):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#                 exchange=True
#         if not exchange:
#             return


# def a(n):
#     if n == 1:
#         print('我的小鲤鱼',end='')
#         return
#     print('抱着',end='')
#     n=n-1
#     a(n)
#     print('的我',end='')
#
# a(4)

# def bin_search(data,value):
#     low=0
#     high=len(data)-1
#     while low<=high:
#         mid=(low+high)//2
#         if data[mid]==value:
#             return mid
#         elif data[mid]>value:
#             high=mid-1
#         else:
#             low=mid+1

# #二分查找
# def bin_search(data,value):
#     low=0
#     high=len(data)-1
#     while low<=high:
#         mid=(low+high)//2
#         if data[mid]==value:
#             return mid
#         elif data[mid]<value:
#             high=mid-1
#         else:
#             low=mid+1
# #冒泡查找
# def bubble_sort(li):
#     for i in range(len(li)-1):
#         exchange=False
#         for j in range(len(li)-i-1):
#             if li[j]<li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
#                 exchange=True
#         if not exchange:
#             return
# #选择排序
# def select_sort(li):
#     for i in range(len(li)-1):
#         min_loc=i
#         for j in range(i+1,len(li)):
#             if li[j]<li[min_loc]:
#                 min_loc=j
#         if min_loc!=i:
#             li[i],li[min_loc]=li[min_loc],li[i]
# #插入排序
# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp=li[i]
#         j=i-1
#         while j>=0 and tmp<li[j]:
#             li[j+1]=li[j]
#             j=j-1
#         li[j+1]=tmp
# #快速排序
# def quickSort(L, low, high):
#     i = low
#     j = high
#     if i >= j:
#         return L
#     key = L[i]
#     while i < j:
#         while i < j and L[j] >= key:
#             j = j-1
#         L[i] = L[j]
#         while i < j and L[i] <= key:
#             i = i+1
#         L[j] = L[i]
#     L[i] = key
#     quickSort(L, low, i-1)
#     quickSort(L, j+1, high)
#     return L



#二分查找
# def bin_sort(data,value):
#     low=0
#     high=len(data)-1
#     mid=(low+high)//2
#     if data[mid]==value:
#         return mid
#     elif data[mid]>value:
#         high=mid-1
#     else:
#         low=mid+1


#快速排序
# def quick_sort(data,left,right):
#     i=left
#     j=right
#     if i>j:
#         return data
#     tmp=data[left]
#     while left<right:
#         while left<right and data[right]>=tmp:
#             right=1
#         data[left]=data[right]
#         while left<right and data[left]<=tmp:
#             left+=1
#         data[right]=data[left]
#     data[left]=tmp
#     quick_sort(data,left,i-1)
#     quick_sort(data,j+1,right)
#     return data

#二分查找
# def bin_search(data,value):
'''
二分查找基于查找可迭代对象是有序的情况！
'''
#     low=0
#     high=len(data)-1
#     while low<=high:
#         mid=(low+high)//2
#         if data[mid]==value:
#             return mid
#         elif data[mid]>value:
#             high=mid-1
#         else:
#             low=mid+1
#     return '没有该值'
# res=bin_search([7,8,9,10,11,12,13],9)
# print(res)

#冒泡排序
# def bubble_sorted(data):
#     for i in range(len(data)-1):
#         exchange=False
#         for j in range(len(data)-i-1):
#             if data[j]<data[j+1]:
#                 data[j],data[j+1]=data[j+1],data[j]
#                 exchange=True
#         if not exchange:
#             return data



#插入排序
# def insert_sorted(data):
#     for i in range(1,len(data)):
#         tmp=data[i]
#         j=i-1
#         while j>=0 and tmp<data[j]:
#             data[j+1]=data[j]
#             j=j-1
#         data[j+1]=tmp

# def insert_sorted(data):
#     for i in range(1,len(data)):
#         tmp=data[i]
#         j=i-1
#         while j>=0 and tmp<data[j]:
#             data[j+1]=data[j]
#             j=j-1
#         data[j+1]=tmp

# def insert_sorted(data):
#     for i in range(1,len(data)):
#         tmp=data[i]
#         j=i-1
#         while j>=0 and tmp<data[j]:
#             data[j+1]=data[j]
#             j=j-1
#         data[j+1]=tmp














'''
 def quick_sort(data,left,right):
     i=left
     j=right
     if i>j:
         return data
     tmp=data[left]
     while left<right:
         while left<right and data[right]>=tmp:
             right=1
         data[left]=data[right]
         while left<right and data[left]<=tmp:
             left+=1
         data[right]=data[left]
     data[left]=tmp
     quick_sort(data,left,i-1)
     quick_sort(data,j+1,right)
     return data
'''
'''
快排思路:取第一个元素p，使元素p归位
列表别p分为左右两部分，左边比p小，右边比p大
递归完成排序
'''
'''
冒泡排序思路:取第一个元素值与其他元素各做比较，比该元素大则交换位置，比该元素小则继续往上比较
一趟下来可以保证最大的数在最顶端。
'''
# def quick_sorted(data,left,right):
#     i=left
#     j=right
#     if i>j:
#         return data
#     tmp=data[left]
#     while left<right:
#         while left<right and data[right]>=tmp:
#             right+=1
#         data[left]=data[right]
#         while left<right and data[left]<=tmp:
#             left+=1
#         data[right]=data[left]
#     data[left]=tmp
#     quick_sorted(data,left,i-1)
#     quick_sorted(data,j+1,right)
#     return data

# def bin_search(data,value):
#     low=0
#     high=len(data)-1
#     while low<+high:
#         mid=(low+high)//2
#         if data[mid]==value:
#             return mid
#         elif data[mid]<value:
#             low=mid+1
#         else:
#             high=mid-1

# def bubble_sorted(data):
#     for i in range(len(data)):
#         exchange=False
#         for j in range(len(data)-i-1):
#             if data[j]<data[j+1]:
#                 data[j],data[j+1]=data[j+1],data[j]
#                 exchange=True
#         if not exchange:
#             return data


# def quick_soretd(data,left,right):
#     i=left
#     j=right
#     if i<j:
#         return data
#     tmp=data[left]
#     while left<right:
#         while left<right and data[right]>=tmp:
#             right+=1
#         data[left]=data[right]
#         while left<right and data[left]<=tmp:
#             left+=1
#         data[right]=data[left]
#     data[left]=tmp
#     quick_soretd(data,left,i-1)
#     quick_soretd(data,j+1,right)
#     return data

'''
希尔排序是一种分组插入排序算法
首先取一个整数d=n/2,将元素分为d个组，每组相邻量元素之间距离为d
在各组内进行直接插入排序
'''

# def insert_sorted(data):
#     for i in range(1,len(data)):
#         tmp=data[i]
#         j=i-1
#         while j>=0 and tmp<data[j]:
#             data[j+1]=data[j]
#             j=j-1
#         data[j+1]=tmp

# def quick_sorted(data,left,right):
#     i=left
#     j=right
#     if i>j:
#         return data
#     tmp=data[left]
#     while left<right:
#         while left<right and data[right]>=tmp:
#             right+=1
#         data[left]=data[right]
#         while left <right and data[left]<=tmp:
#             left+=1
#         data[right]=data[left]
#     data[left]=tmp
#     quick_sorted(data,left,i-1)
#     quick_sorted(data,j+1,right)
#     return data

'''
希尔排序
def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>=0 and tmp<data[j]:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap/=2
'''

'''
基于类的绑定方法
class Mysql:
    _instance=None
    def __init__(self,host,port):
        self.host=host
        self.port=port
    @classmethod
    def singleton(cls):
        if not cls._instance:
            cls._instance=cls('127.0.0.1',3306)
        return cls._instance
'''
'''
基于元类
class Mymetaclass(type):
    def __init__(self,name,bases,attrs):
        super().__init__(name,bases,attrs)
        self._instance=object.__new__(self)
        self.__init__(self._instance,'127.0.0.1',3306)
    def __call__(self, *args, **kwargs):
        if args or kwargs:
            obj=object.__new__(self)
            self.__init__(obj,*args,**kwargs)
            return obj
        return self._instance

'''
'''
基于装饰器
def singleton(cls):
    cls._instance=cls('127.0.0.1',3306)
    def inner(*args,**kwargs):
        if args or kwargs:
            obj=cls(*args,**kwargs)
            return obj
        return cls._instance
    return inner
'''
'''
冒泡排序
def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]>data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                exchange=True
        if not exchange:
            return data
res=bubble_sorted([6,4,2,3,1,9,6,7,8])
print(res)
'''
'''
插入排序
def insert_sorted(data):
    for i in range(1,len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and tmp<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=tmp
a=[4,2,1,5,9,6,8,7]
insert_sorted(a)
print(a)
[1, 2, 4, 5, 6, 7, 8, 9]
'''
'''
快排
def quick_sorted(data,i,j):
    left=i
    right=j
    if left>right:
        return data
    tmp=data[left]
    while left<right:
        while left<right and data[right]>=tmp:
            right-=1
        data[left]=data[right]
        while left<right and data[left]<=tmp:
            left+=1
        data[right]=data[left]
    data[left]=tmp
    quick_sorted(data,i,left-1)
    quick_sorted(data,right+1,j)
    return data
res=quick_sorted([6,3,4,1,8,9,5,7],0,7)
print(res)
[1, 3, 4, 5, 6, 7, 8, 9]

'''
'''
希尔排序
def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>=0 and tmp<data[j]:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap//=2
a=[5,2,3,4,8,9,6,7]
shell_sorted(a)
print(a)
[2, 3, 4, 5, 6, 7, 8, 9]
'''
'''
def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j<=0 and tmp<data[j]:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap//=2
def bin_search(data,value):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            low=mid+1
        else:
            high=mid-1
def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                exchange=True
        if not exchange:
            return data
def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data
def insert_sorted(data):
    for i in range(1,len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and tmp<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=tmp


'''
a=[1,2,3,4,5,6,7,8]
b=[5,7,9,8,6,4,2,3,1]

'''
def bin_search(data,value):
    low=0
    high=len(data)
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]>value:
            high=mid-1
        else:
            low=mid+1

def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                exchange=True
        if not exchange:
            return data

def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>0 and data[j]>tmp:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap//=2

def insert_sorted(data):
    for i in range(len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and data[j]>tmp:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=tmp

'''
'''
def bin_search(data,value):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            low=mid+1
        else:
            high=mid-1

def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                exchange=True
        if not exchange:
            return data

def insert_sorted(data):
    for i in range(len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and tmp<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=tmp

def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>0 and data[j]>tmp:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp

'''
'''
def bin_search(data,value):
    low=0
    high=len(data)
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            low=mid+1
        else:
            high=mid-1
def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j+1],data[j]=data[j],data[j+1]
                exchange=True
        if not exchange:
            return data
def insert_sorted(data):
    for i in range(1,len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and data[j]>tmp:
            data[j+1]=data[j]
            j-=1
        data[j+1]=tmp
def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j  :
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data
def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>=0 and data[j]>tmp:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap//=2

'''

"""
单列模式
1.静态方法
def Mysql():
    _instance=None
    def __init__(self,host,port):
        self.host=host
        self.port=port
    @classmethod
    def singleton(cls):
        if not cls._instance:
            cls._instance=cls("127.0.0.1",3306)
        return cls._instance
2.装饰器
def singleton(cls):
    cls._instance=cls("127.0.0.1",3306)
    def inner(*args,**kwargs):
        if args or kwargs:
            obj=cls(*args,**kwargs)
            return obj
        return cls._instance
    return inner
3.元类
def MemetaClass(type):
    def __init__(self,name,bases,attrs):
        super().__init__(name,bases,attrs)
        self._instance=object.__new__(self)
        self.__init__(self._instance,"127.0.0.1",3306)
    def __call__(self,*args,**kwargs):
        if args or kwargs:
            obj=object.__new__(self)
            self.__init__(*args,**kwargs)
            return obj
        return self._instance
"""
'''
def bin_search(data,value):
    low=0
    high=len(data)
    while low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            low=mid+1
        else:
            high=mid-1
def bubble_search(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j+1],data[j]=data[j],data[j+1]
                exchange=True
        if not exchange:
            return data


def insert_sorted(data):
    for i in range(1,len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and data[j]>tmp:
            data[j+1]=data[j]
            j-=1
        data[j+1]=tmp

def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j :
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def shell_sorted(data):
    gap=len(data)//2
    while gap>0 :
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            while j>=0 and data[j]>tmp:
                data[j+gap]=data[j]
                j-=gap
            data[j+gap]=tmp
        gap//=2
'''
'''
def shell_sorted(data):
    gap=len(data)//2
    for i in range(gap,len(data)):
        tmp=data[i]
        j=i-gap
        while j>=0 and data[j]>tmp:
            data[j+1]=data[j]
            j-=gap
        data[j+1]=tmp
    gap//=2

def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if data[j+1]<data[j]:
                data[j+1],data[j]=data[j],data[j+1]
                exchange=True
        if not exchange:
            return data



'''
#导入模块
import numpy as np
import pandas as pd

'''
pandas中的数据类型
1.序列  数组
2.二维数组 Dataframe
......

'''

'''
l=pd.Series([1,3,5])
print(l)
print('index:',l.index)
print('value',l.values)
0    1
1    3
2    5
dtype: int64
index: RangeIndex(start=0, stop=3, step=1)
value [1 3 5]
'''

'''
d=pd.Series({'a':1,'b':3})
print(d)
print('index',d.index)
print('values',d.values)
a    1
b    3
dtype: int64
index Index(['a', 'b'], dtype='object')
values [1 3]
'''


'''
e=pd.DataFrame([[1,2],[3,4],[6,7,9]])
print(e)
print('index',e.index)
print('values',e.values)
   0  1    2
0  1  2  NaN
1  3  4  NaN
2  6  7  9.0

index RangeIndex(start=0, stop=3, step=1)
values [
        [ 1.  2. nan]
        [ 3.  4. nan]
        [ 6.  7.  9.]
        ]
'''
'''
demo=[[1,2],[4,6],[6,9]]
demo1=pd.DataFrame(demo,index=["line1","line2","line3"],columns=["name","age"])
print(demo1)
print('index',demo1.index)
print('values',demo1.values)
       name  age
line1     1    2
line2     4    6
line3     6    9

Index(['line1', 'line2', 'line3'], dtype='object')
values [
        [1 2]
        [4 6]
        [6 9]
        ]
总结可知，这里的index并不仅仅指的是索引值，而是表数据的第一行
values则是取每一行对应的数据部分的内容
'''


'''
dates=['2018_8_%s'%i for i in range(8)]
n=pd.DataFrame(np.random.randn(8,8),index=dates,columns=[chr(ord('A')+i) for i in range(8)])
#写入数据
n.to_csv('D:\pandas.csv')
#导出数据
read_n=pd.read_csv('D:\pandas.csv')
print(read_n)
print(n)
print('前三行',n.head(3))
print('后三行',n.tail(3))
print('获取特定的行',n.ix[['2018_8_1','2018_8_5']])
print('获取特定的列',n[['A','C']])
print('获取A列里面数据大于0的',n[n['A']>0])
                 A         B         C    ...            F         G         H
2018_8_0  0.004453  0.043859  2.051120    ...    -0.742216  0.783950 -0.387588
2018_8_1 -0.275733 -0.613522 -0.669921    ...     0.874959 -0.803459  1.399357
2018_8_2  0.028822 -0.672915 -1.999537    ...    -0.422370 -0.602221 -2.211795
2018_8_3 -0.129852  0.500231 -0.540413    ...    -0.222426  0.019738  1.215877
2018_8_4 -0.313071 -0.591547  1.817462    ...    -0.263002  0.414922 -1.156374
2018_8_5  0.679770  1.588511 -0.108629    ...    -0.069570  2.286812  0.048368
2018_8_6  1.899039  0.254042  0.312609    ...    -0.209025 -0.181206 -2.401868
2018_8_7 -0.184544 -1.337919 -1.380939    ...     0.153365  0.495810 -1.177276

[8 rows x 8 columns] 
前三行                  A         B         C    ...            F         G         H
2018_8_0  0.004453  0.043859  2.051120    ...    -0.742216  0.783950 -0.387588
2018_8_1 -0.275733 -0.613522 -0.669921    ...     0.874959 -0.803459  1.399357
2018_8_2  0.028822 -0.672915 -1.999537    ...    -0.422370 -0.602221 -2.211795

[3 rows x 8 columns]
后三行                  A         B         C    ...            F         G         H
2018_8_5  0.679770  1.588511 -0.108629    ...    -0.069570  2.286812  0.048368
2018_8_6  1.899039  0.254042  0.312609    ...    -0.209025 -0.181206 -2.401868
2018_8_7 -0.184544 -1.337919 -1.380939    ...     0.153365  0.495810 -1.177276

[3 rows x 8 columns]
获取特定的行                  A         B         C    ...            F         G         H
2018_8_1 -0.275733 -0.613522 -0.669921    ...     0.874959 -0.803459  1.399357
2018_8_5  0.679770  1.588511 -0.108629    ...    -0.069570  2.286812  0.048368

[2 rows x 8 columns]

获取特定的列                  A         C
2018_8_0                    -1.030400    0.538639
2018_8_1                     0.887302    -2.614686
2018_8_2                    -0.812352    -0.481380
2018_8_3                     0.639233    -2.316585
2018_8_4                    -1.023764    -0.955641
2018_8_5                    -0.224729    0.224836
2018_8_6                     0.581603    -0.808184
2018_8_7                    -1.064073    1.127286

获取A列里面数据大于0的                  A         C
2018_8_0                              0.382606  0.718785
2018_8_1                              0.159323  0.008885
2018_8_2                              0.558493 -1.479370
2018_8_3                              2.937412  0.226566

'''
'''
def bin_search(data,value):
    low=0
    high=len(data)-1
    while low>=0:
        mid=(low+high)//2
        if data[mid]==value:
            return mid
        elif data[mid]<value:
            low= mid+1
        else:
            high=mid-1


def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if j>=0 and data[j]>data[j+1]:
                data[j+1],data[j]=data[j],data[j+1]
                exchange=True
        if not exchange:
            return data

def insert_sorted(data):
    for i in range(1,len(data)):
        tmp=data[i]
        j=i-1
        while j>=0 and data[j]>tmp:
            data[j+1]=data[j]
            j-=1
        data[j+1]=tmp


def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def shell_sorted(data):
    gap=len(data)//2
    for i in range(gap,len(data)):
        tmp=data[i]
        j=i-gap
        while j>=0 and data[j]>tmp:
            data[j+gap]=data[j]
            j-=gap
        data[j+gap]=tmp
    gap//=2
'''



'''
def bin_search(data,value):
    low=0
    high=len(data)
    if low<=high:
        mid=(low+high)//2
        if data[mid]==value:
            return value
        elif data[mid]>value:
            low=mid+1
        else:
            high=mid-1

def bubble_sorted(data):
    for i in range(len(data)):
        exchange=False
        for j in range(len(data)-i-1):
            if j>=0 and data[j+1]<data[j]:
                data[j+1],data[j]=data[j],data[j+1]
                exchange=True
        if not exchange:
            return data

def insert_sorted(date):
    for i in range(len(date)):
        tmp=date[i]
        j=i-1
        while j>=0 and date[j]>tmp:
            date[j+1]=date[j]
            j-=1
        date[j+1]=tmp

def quick_sorted(data,left,right):
    i=left
    j=right
    if i>j:
        return data
    tmp=data[i]
    while i<j:
        while i<j and data[j]>=tmp:
            j-=1
        data[i]=data[j]
        while i<j and data[i]<=tmp:
            i+=1
        data[j]=data[i]
    data[i]=tmp
    quick_sorted(data,left,i-1)
    quick_sorted(data,j+1,right)
    return data

def shell_sorted(data):
    gap=len(data)//2
    while gap>0:
        for i in range(gap,len(data)):
            tmp=data[i]
            j=i-gap
            if j>=0 and  data[j]<tmp:
                data[j+gap]=data[j]
                j=j-gap
            data[j+gap]=tmp
        gap//=2

'''








































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































