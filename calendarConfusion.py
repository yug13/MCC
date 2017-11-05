inputFile = open("Calendar-confusion_InputForSubmission_1.txt", "r" )

inputFileLines = inputFile.readlines()

for lines in inputFileLines:
    a= lines.split(" ") #iterate over each line
                        # store it in an array
    if (a[1].find("m")!=-1):
        posM = a[1].index("m") # find position of the first m in format
                            # use that to extract months from date
    if (a[1].find("y")!=-1):
        
        posY = a[1].index("y") # repeat for year and date
    if (a[1].find("d")!=-1):
        posD = a[1].index("d")

    # write to the output file the replaced date with new format only, replace the mm yyyy and dd using the positions
    # gathered from before 
    
    print(str(a[2].replace("mm",str(a[0][posM:posM+2])).replace("yyyy",str(a[0][posY:posY+4])).replace("dd",str(a[0][posD:posD+2]))).replace("\n",""))


        

    


