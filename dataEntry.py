

class DataEntry:
    id:str

    def __init__(self, dataIn:str) -> None:
        self.data = dataIn.split(",")
        self.id = int(self.data[1], 16)

    def __str__(self) -> str:
        return f"{self.id}"
    
    def newId (self, newId):
        self.data[1] = "{:04x}".format(newId)
        self.id = int(self.data[1], 16)

    def newMacroTarget (self, newTarget):
        self.data[10] = "{:08x}".format(newTarget)

    def toString (self):
        return ",".join(self.data)