f = open("PracticeInput.txt","r")
x = f.readlines()
for y in x:
    a = y.split(" ")
    print (a)
    D = a[1].index("d")
    M = a[1].index("m")
    Y = a[1].index("y")
    a[2] = a[2].replace("\n","").replace("mm",str(a[0][M:M+2])).replace("dd",str(a[0][D:D+2])).replace("yyyy",str(a[0][Y:Y+4]))
    print (a[2])                                                                                                       
    
    
    
