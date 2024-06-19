from dataEntry import DataEntry


macro = """
K,0001,"A-",0001,00000000,0000,0000,0000,0000,
0000006c,0003,0014,00000007,fffffff6,00000000,0000006e,0;
K,0002,"A+",0001,00000000,0000,0000,0000,0000,
0000007b,0003,0014,00000007,0000000a,00000000,0000003e,0;
K,0003,"B-",0001,00000000,0000,0000,0000,0000,
00000075,0003,0014,00000006,fffffff6,00000000,0000006a,0;
K,0004,"B+",0001,00000000,0000,0000,0000,0000,
0000007e,0003,0014,00000006,0000000a,00000000,0000006e,0;
K,0005,"C-",0001,00000000,0000,0000,0000,0000,
00000078,0003,0014,00000005,fffffff6,00000000,0000006d,0;
K,0006,"C+",0001,00000000,0000,0000,0000,0000,
00000069,0003,0014,00000005,0000000a,00000000,00000062,0;
K,0007,"D-",0001,00000000,0000,0000,0000,0000,
0000006f,0003,0014,00000004,fffffffe,00000000,0000005e,0;
K,0008,"D+",0001,00000000,0000,0000,0000,0000,
00000054,0003,0014,00000004,00000002,00000000,00000060,0;"""

def getMacroAsClassList (macro):
    dataSplit = macro.split(";")
    dataSplit = dataSplit[:-1]
    classList:list[DataEntry] = []
    for item in dataSplit:
        classList.append(DataEntry(item))
    
    return classList

def getMacroListWithStartIndex (i):
    listMacro = getMacroAsClassList(macro)
    for item in listMacro:
        item.newId(i)
        i += 1
    return listMacro


automation = """D,0008,0007,00000000,00000000,00000000,00000000,00000000,"'a'",
0000001e,00000001,00000000,0.000000,00000029,00000000,"",;

D,0007,0007,00000000,00000000,00000000,00000000,00000000,"'b'",
0000001e,00000002,00000000,0.000000,00000029,00000000,"",;

D,0006,0007,00000000,00000000,00000000,00000000,00000000,"'c'",
0000001e,00000003,00000000,0.000000,00000029,00000000,"",;

D,0005,0007,00000000,00000000,00000000,00000000,00000000,"'d'",
0000001e,00000004,00000000,0.000000,00000029,00000000,"",;

D,0004,0007,00000000,00000000,00000000,00000000,00000000,"'e'",
0000001e,00000005,00000000,0.000000,00000029,00000000,"",;

D,0003,0007,00000000,00000000,00000000,00000000,00000000,"'f'",
0000001e,00000006,00000000,0.000000,00000029,00000000,"",;

D,0002,0007,00000000,00000000,00000000,00000000,00000000,"'g'",
0000001e,00000007,00000000,0.000000,00000029,00000000,"",;

D,0001,0007,00000000,00000000,00000000,00000000,00000000,"'h'",
0000001e,00000008,00000000,0.000000,00000029,00000000,"",;
"""

def getAutoAsClassList (auto):
    dataSplit = auto.split(";")
    dataSplit = dataSplit[:-1]
    classList:list[DataEntry] = []
    for item in dataSplit:
        classList.append(DataEntry(item))
    
    return classList

def getAutoWithStartIndex (i):
    listAuto = getMacroAsClassList(automation)
    for item in listAuto:
        item.newId(i)
        i += 1
    return listAuto

def setMacroIndexInAuto (listAuto, i):
    for item in listAuto:
        item.newMacroTarget(i)
        i += 1

    return listAuto
