# n=None
# print(type(n)) # NoneType

'''String is immutable,modifications can't be done '''
# a=('hello''world')
# a[0]='hey' # (TpyeError: str object does not support item assignment) 


'''List Data Type'''
# a=[] (List repesents with square bracket,Empty list can be possible)
# print(a,type(a)) # [] list

# b=['niharika',4.5]
# print(b[0],type(b)) # niharika list
# print(b[1]) # 4.5
# print(b[2]) # IndexError: list index out of range

# x=['hello','world'] # ['hey','world] (list is mutable,modifications can be made in list)
# x[0]='hey'
# print(x)
# y=['v','a','n'] # ['c','a','n']
# y[0]='c'
# print(y)

# z=[2,5.6,'hai',True,[4,5]] # (List can contains several data types in it,it can also include one more list inside it)
# print(z[0],type(z[0])) # 2 int
# print(z[1],type(z[1])) # 5.6 float
# print(z[2],type(z[2])) # 'hai' str
# print(z[3],type(z[3])) #  True bool
# print(z[4],type(z[4])) # [4,5] list
# print(z[5],type(z[5])) # IndexError:  list index out of range 

# y=['niharika'] # (list is sequence type)
# print(y[0]) # niharika
# print(y[0][0]) # n
# print(y[0][2]) # h
# print(y[0][-3]) # i

'''List Methods'''
# a=[1,2,3,4]
# a.append(5) 
# print(a) # [1,2,3,4,5]
# b=[2.3,4,'hi']
# b.append(True)
# print(b) # [2.3,4,'hi',True]
# c=[5,4,3]
# c.append(6,7)
# print(c) # TypeError: list .append takes only one argument

# n=['abc']
# n.clear()
# print(n) # [] (it will clear the list)

# a=[123]
# b=a.copy() # [123]
# print(b)
# b=a
# print(b) # [123]

# s=[1,1,2,3,4] 
# print(s.count(1)) # 2
# print(s.count(5)) # 0

# d=[2,3.4,'abc']
# d.extend('9')
# print(d) # [2,3.4,'abc','9']
# d.extend('all') # [2,3.4,'abc','a','l','l']
# print(d)
# d.extend('5.6')
# print(d) # [2, 3.4, 'abc', '5', '.', '6']

# a=['hyderabad',2,[5,3]]
# print(a.index(2)) # 1
# print(a.index('hyderabad')) # 0
# print(a.index(7)) # ValueError: 7 is not in list
# print(a.rindex(7)) # AttributeError
 
# b=[1,2,'hiii',5,10]
# b.insert(2,5)
# print(b) # [1, 2, 5, 'hiii', 5, 10]
# c=[1,2,6,5,10]
# c.insert(-1,1) 
# print(c) # [1, 2, 6, 5, 1, 10]

# a=[1,2,3,4]
# a.pop()
# print(a) # [1,2,3]
# a.pop(2)
# print(a) # [1,2,4]
# a.pop(1)
# print(a) # [1,3,4]
# a.pop(4)
# print(a) # IndexError: pop index out of range


# b=[10,20,30,'hii']
# b.remove('hii')
# print(b) # [10,20,30]
# b.remove(20)
# print(b) # [10, 30, 'hii']

# c=[1,4,7,9,3,6]
# c.reverse()
# print(c) # [6, 3, 9, 7, 4, 1]

# a=[3,5,7,9,8,6,4]
# a.sort() (empty sort will take by default as reverse=False)
# print(a) # [3,4,5,6,7,8,9]
# a.sort(reverse=True)
# print(a) # [9,8,7,6,5,4,3]


'''Tuple Data Type'''
# x=(4,)
# print(type(x)) # tuple (Tuple represents with ,)

'''Tuple is immutable,modifications can't be done'''
# x=(1,2,3,4)
# x[0]= 2 # TypeError: 'tuple' object does not support item assignment

# z=(2,5.6,'hai',True,[4,5],(2,3)) # (Tuple can contains several data types in it,it can also include tuple inside it)
# print(z[0],type(z[0])) # 2 int
# print(z[1],type(z[1])) # 5.6 float
# print(z[2],type(z[2])) # 'hai' str
# print(z[3],type(z[3])) # True bool
# print(z[4],type(z[4])) # [4,5] list
# print(z[5],type(z[5])) # (2,3) tuple
# print(z[6],type(z[6])) # IndexError: tuple index out of range


'''Tuple Methods'''
# a=(1,4,3,1,5.6,'hii')
# print(a.count(1)) # 2
# print(a.count(9)) # 0
# print(a.index(5.6)) # 4
# print(a.index(6.7)) # ValueError: tuple.index(x): x not in list
