import itertools

operations=[]
i = input("Enter schedule: ")
i = i.split(",")
for a in i:
    s = a.strip()
    s2 = s.split("(")
    operations.append([s[0], int(s2[0][1:]), s2[1][0:-1]])
nodes=[]
edges=[]
for i in range(len(operations)):
    t = operations[i]
    operation = t[0]
    transaction = t[1]
    variable = t[2]
    if transaction not in nodes:
        nodes.append(transaction)
    #makes the nodes
        
for i in range(len(operations)):
    t = operations[i]
    operation = t[0]
    transaction = t[1]
    variable = t[2]
    
    for i2 in range(i+1, len(operations)):
        t2 = operations[i2]
        operation2 = t2[0]
        transaction2 = t2[1]
        variable2 = t2[2]
        if operation.lower() == "w" or operation2.lower() == "w":
            if transaction != transaction2:
                if variable2 == variable:
                    edges.append([transaction, transaction2])
reachable=[]#this is based on DIRECTED data
reachable2=[]#this is based on DIRECTED data
pathtoreach=[]
emptylist=[]
for i in range(len(nodes)+1):#index 0 is not used, we start counting from 1
    emptylist.append([])
for i in range(len(nodes)+1):#index 0 is not used, we start counting from 1
    reachable.append([])
    reachable2.append([])
    pathtoreach.append(emptylist)
for i in range(len(edges)):
    a = edges[i][0]
    b = edges[i][1]
    if b not in reachable[a]:
        reachable[a].append(b)
        reachable2[a].append(b)
        pathtoreach[a][b]=[b]
changed = True
cycle=None
while changed:
    changed = False
    for i in range(1, len(reachable)):
        for i2 in reachable[i]:
            #i2 are the things reachable by i
            for i3 in reachable[i2]:
                #i3 are things reachable by i indirectly
                
                if i3 not in reachable[i]:
                    changed = True
                    reachable[i].append(i3)
                    pathtoreach[i][i3]=[]
                    for x in pathtoreach[i][i2]:
                        pathtoreach[i][i3].append(x)
                    pathtoreach[i][i3].append(i3)
                    if i3==i:
                        cycle=i
if cycle!=None:
    print("Not conflict serializable.")
    path = pathtoreach[cycle][cycle]
    concat="Cycle: "
    for i in range(len(path)):
        if i>0:
            concat+=" -> "
        concat+=str(path[i])
    print(concat)
    
else:
    print("Conflict quivalent serial schedule:")
    permutations=list(itertools.permutations(nodes))
    for list in permutations:
        bad = False
        for i in range(1, len(list)):
            if list[i] not in reachable[list[i-1]]:
                bad = True
                break
        if not bad:
            concat = ""
            for a in list:
                for op in operations:
                    if op[1] == a:
                        concat += op[0]+str(op[1])+"("+op[2]+"), "
            print(concat[:-2])
            break