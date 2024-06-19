from dataEntry import DataEntry
from data import getMacroListWithStartIndex


def addMacro (data):
    #split in params
    dataSplit = data.split(";")

    #macros in file
    existingMacrosList = []
    for item in dataSplit:
        if item.startswith("\nK"):
            existingMacrosList.append(item)

    #read macros to class
    classList:list[DataEntry] = []
    for item in existingMacrosList:
        classList.append(DataEntry(item))

    #get new start index
    if len(classList) == 0:
        newMacroStartIndex = 1
    else:
        newMacroStartIndex = classList[-1].id +1

    #change indexes
    newMacroList = getMacroListWithStartIndex(newMacroStartIndex)

    #add old+new
    updatetList = classList + newMacroList

    newString = ""
    for item in updatetList:
        newString += item.toString() + ";"


    if len(classList) != 0:
        #repalce old wiht new
        oldString = ""
        for item in classList:
            oldString += item.toString() + ";"

        data = data.replace(oldString, newString)
    else:
        #find out where it is
        index = 0
        for i in range(len(dataSplit)):
            if dataSplit[i].startswith("\nE1"):
                index = i
                break
        if (index == 0):
            exit("error no E1 found")

        #add
        updatedStringList = []
        for item in updatetList:
            updatedStringList.append(item.toString())
        dataSplit[:index] = dataSplit[:index] + updatedStringList
        data = ";".join(dataSplit)

    return (newMacroStartIndex, data)
