def valuetokey(val,dic):
    t = []
    for a in range(0,len(dic)):
        if list(dic.values())[a] == val:
            t.append(list(dic.keys())[a])
    return t
def op(ol):
    olp = []
    order = []
    ord3 = []
    olp = ol
    dic = {}
    for i in range(len(ol)):
        for j in range(len(ol)):
            if j!= i:
                for k in range(len(ol)):
                    if k!= j and k!= i:
                        y = olp[j] 
                        z = olp[k] 
                        l = (not olp[i])*(y) ^ ((olp[i])*z) 
                        t = ((olp[i])*(y)) ^ ((not olp[i])*z) 
                        lo = olp[:]
                        lo[j] = l
                        lo[k] = t
                        order.append(lo)
                        ord3.append([i,j,k])
                        for x in range(len(order)):
                            dic[f"{ord3[x]}"] =  order[x]
                        olp = ol
                    else:
                        pass
            else:
                pass
    return dic

###################################################################################################
#Above function has introduced in the Construct _ Toffoli_by_Fredkin_S1.py
###################################################################################################

#This function is to locate the Fredkin gate from i,j,k [which get from the Construct _ Toffoli_by_Fredkin_S1.py]
def DE(ol,i,j,k):
    all = []
    ol1 = []
    ol2 = []
    ol3 = []
    x = op(ol)
    for value in x.values():
        ol1.append(value)
    y = op(ol1[i])
    for value in y.values():
        ol2.append(value)
    z = op(ol2[j])
    for value in z.values():
        ol3.append(value)
    all.extend([valuetokey(ol1[i],x),valuetokey(ol2[j],y),valuetokey(ol3[k],z)])
    return all
###################################################################################################
###################################################################################################
###################################################################################################
#This 3 function is to clean up data
def st(i,j,k,order):
    f = []
    x =  sorted(list(set(DE([0,0,0,1,0],i,j,k)[order]) & set(DE([0,0,1,1,0],i,j,k)[order]) & set(DE([0,1,0,1,0],i,j,k)[order])&set(DE([1,0,0,1,0],i,j,k)[order])&set(DE([0,1,1,1,0],i,j,k)[order])&set(DE([1,0,1,1,0],i,j,k)[order])&set(DE([1,1,0,1,0],i,j,k)[order])&set(DE([1,1,1,1,0],i,j,k)[order])))
    if x[0][4] == x[1][7]:
        f.append(x[0])

    return f[0]

def printf(i,j,k):
    f = []
    for o in range(3):
        f.append(st(i,j,k,o))
    return f

f = []
def ijk(i,j,k):
    if printf(i,j,k) not in f:
        f.append(printf(i,j,k))
###################################################################################################
###################################################################################################
###################################################################################################
#we get the data from the section 1:
'''
i = 8,j= 32,k = 17
i = 8,j= 32,k = 22
i = 8,j= 35,k = 17
i = 8,j= 35,k = 22
i = 11,j= 32,k = 17
i = 11,j= 32,k = 22
i = 11,j= 35,k = 17
i = 11,j= 35,k = 22
i = 20,j= 5,k = 56
i = 20,j= 5,k = 59
i = 20,j= 10,k = 56
i = 20,j= 10,k = 59
i = 20,j= 32,k = 5
i = 20,j= 32,k = 10
i = 20,j= 35,k = 5
i = 20,j= 35,k = 10
i = 23,j= 5,k = 56
i = 23,j= 5,k = 59
i = 23,j= 10,k = 56
i = 23,j= 10,k = 59
i = 23,j= 32,k = 5
i = 23,j= 32,k = 10
i = 23,j= 35,k = 5
i = 23,j= 35,k = 10
i = 32,j= 8,k = 17
i = 32,j= 8,k = 22
i = 32,j= 11,k = 17
i = 32,j= 11,k = 22
i = 32,j= 20,k = 5
i = 32,j= 20,k = 10
i = 32,j= 23,k = 5
i = 32,j= 23,k = 10
i = 35,j= 8,k = 17
i = 35,j= 8,k = 22
i = 35,j= 11,k = 17
i = 35,j= 11,k = 22
i = 35,j= 20,k = 5
i = 35,j= 20,k = 10
i = 35,j= 23,k = 5
i = 35,j= 23,k = 10
Done
'''
###################################################################################################
###################################################################################################
#We input the all i,j,k and clear up the data, final clearly get the position of the Fredkin gate 
ijk(i = 8,j= 32,k = 17)
ijk(i = 11,j= 32,k = 17)
ijk(i = 20,j= 5,k = 56)
ijk(i = 20,j= 32,k = 5)
ijk(i = 20,j= 10,k = 59)
ijk(i = 20,j= 35,k = 10)
ijk(i = 23,j= 5,k = 56)
ijk(i = 23,j= 10,k = 59)
ijk(i = 32,j= 11,k = 22)
ijk(i = 23,j= 35,k = 10)
ijk(i = 23,j= 32,k = 5)
ijk(i = 32,j= 8,k = 17)
ijk(i = 32,j= 20,k = 5)
ijk(i = 32,j= 23,k = 10)
ijk(i = 35,j= 8,k = 17)
ijk(i = 35,j= 11,k = 22)
ijk(i = 35,j= 20,k = 5)
ijk(i = 35,j= 23,k = 10)
###################################################################################################
###################################################################################################
all = []
for i in f:
    if sorted(i) not in all:
        all.append(sorted(i))
for i in all:
    print(f"First Fredkin gate position is :{i[0]},Second Fredkin gate position is :{i[1]},Third Fredkin gate position is :{i[2]}")
