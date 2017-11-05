f = open("Little-league-simulation_InputForSubmission_1.txt","r")
x = f.readlines()
i = x[0]
i = i.replace("FB, S","S").replace("FB, F","HR").replace("C, S","H").replace("C, F","S").replace("(","").replace(")","").replace(" ","")
new = i.split(",")
first = new[0]
out = 0
strike = 0
points = 0
h = 0
if (first==("S")):
    strike = 1
for var in new:
    if ((var==first) & (first == "S")):
        strike += 1
    if (strike == 3):
        out += 1
        strike = 0
        if (out == 3):
            break
    if (var == "H"):
        strike = 0
        h += 1
        if (h==4):
            h -= 1
            points += 1
    elif (var=="HR"):
        strike = 0
        points += h + 1
        h = 0
    first = var
print (points)
    
    

