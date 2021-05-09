##################################################################################################
#You can use value to locate the keys of it
def valuetokey(val,dic):
    t = []
    for a in range(0,len(dic)):
        if list(dic.values())[a] == val:
            t.append(list(dic.keys())[a])
    return t
###################################################################################################
###################################################################################################
#this is the single Fredkin gate
# when you input a list [i,j,k] or list more than 3 dim it can return a dict which includes the position of the Fredkin gate
# The dict will also return the result after the operator of Fredkin gate:
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
###################################################################################################
#This function will return the final result when it apply to 3 Fredkin gate
def fs(a,b,c,i,j,k):#final state
    ol = [a,b,c,1,0]
    ol1 = []
    ol2 = []
    ol3 = []
    for value in op(ol).values():
        ol1.append(value)
    for value in op(ol1[i]).values():
        ol2.append(value)
    for value in op(ol2[j]).values():
        ol3.append(value)
    return ol3[k]

###################################################################################################
###################################################################################################
#This function we traverse all posibility of the position the Fredkin gate will apply but it will run 60^3 .
def run():
    l=0
    for i in range(60):
        for j in range(60):
            for k in range(60):
                l = l+1
                '''
                Help me to see whether the code is running
                if l%10000 == 0:
                    print("Good")
                else:
                    pass
                '''
                if ls(0,0,0,i,j,k) and ls(0,0,1,i,j,k) and ls(0,1,0,i,j,k) and ls(1,0,0,i,j,k) and ls(1,1,0,i,j,k) and ls(1,0,1,i,j,k)and ls(0,1,1,i,j,k) and ls(1,1,1,i,j,k):
                    print(f"i = {i},j= {j},k = {k}")#we can get the i,j,k and below we will use the i,j,k and the dict to locate the position of the Fredkin gate
                else:
                    pass
###################################################################################################
###################################################################################################
#This function will return a boolen and it is to justify the answer
def ls(a,b,c,i,j,k):
    return fs(a,b,c,i,j,k)[:3] == [a,b,c^(a*b)]
###################################################################################################
run()
print("Done")

###################################################################################################
#Tip:Because this function will costs much time so the progress of locating the position of Fredkin gate will put in the next code:[Construct _ Toffoli_by_Fredkin_S2.py]
