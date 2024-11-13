values = [1995, 1998, "ranjitha", 15, 20, 28]
print(values[0]) #1995
print(values[3]) #15
print(values[2]) #RANJITHA
print(values[1]) #1998
print(values[4]) #20
print(values[-1]) #28
print(values[0:4]) #1995,1998,RANJITHA,15,20
values.insert(3,"THIMMESH")
print(values)#1995, 1998, 'RANJITHA', 'THIMMESH', 15, 20, 28]
values.append("I LOVE U")
print(values)#1995, 1998, 'RANJITHA', 'THIMMESH', 15, 20, 28, 'I LOVE U'

values[3] = "RANJITHA" #updating
del values[0]
print(values)

#TUPLES
val = (1, 2, "ranju", "thim")
print(val[2:4])

#DICTIONARY
dic = {1:"thimmesh","a":"ranju", 2:"in love"}
print(dic[1])
print(dic["a"])
print(dic[2])

