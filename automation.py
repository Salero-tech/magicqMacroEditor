from dataEntry import DataEntry
from data import getAutoWithStartIndex, setMacroIndexInAuto


def addAutomation (data, macroStartIndex):
    #split in params
    dataSplit = data.split(";")

    #macros in file
    existingAutoList = []
    for item in dataSplit:
        if item.startswith("\nD"):
            existingAutoList.append(item)

    #read macros to class
    classList:list[DataEntry] = []
    for item in existingAutoList:
        classList.append(DataEntry(item))

    #get new start index
    if len(classList) == 0:
        newAutoStartIndex = 1
    else:
        newAutoStartIndex = classList[-1].id +1

    #change indexes
    newAutoList = getAutoWithStartIndex(newAutoStartIndex)
    newAutoList = setMacroIndexInAuto(newAutoList, macroStartIndex)

    #add old+new
    updatetList = classList + newAutoList

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
            if dataSplit[i].startswith("\nu"):
                index = i
                break
        if (index == 0):
            exit("error no u found")

        #add
        updatedStringList = []
        for item in updatetList:
            updatedStringList.append(item.toString())
        dataSplit[:index] = dataSplit[:index] + updatedStringList
        data = ";".join(dataSplit)

    return data
