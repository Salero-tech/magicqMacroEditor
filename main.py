from macro import addMacro
from automation import addAutomation
import customtkinter
from tkinter import filedialog as fd
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Magicq Macro editor")
        self.geometry(f"{760}x{80}")
        self.resizable(width=False, height=False)


        self.inputPathBox = customtkinter.CTkEntry(self, width=600)
        self.inputPathBox.grid(row=0, column=0, padx=5, pady=5)

        self.browseInputBtn = customtkinter.CTkButton(self, text="browse", command=self.browseInput)
        self.browseInputBtn.grid(row=0, column=1, padx=5, pady=5)

        self.generateButton = customtkinter.CTkButton(self, text="Generate", command=self.generate)
        self.generateButton.grid(row=1, column=0, padx=5, pady=5)


    def generate (self):
        outPath = self.browseOutput()
        inPath = self.inputPathBox.get()
        if (outPath == None or inPath == ""):
            return
        
        #read file
        file = open(inPath)
        data = file.read()
        file.close()

        #macro
        MacroStartId, data = addMacro(data)

        #automation
        data = addAutomation(data, MacroStartId)

        file = open(outPath, "w")
        file.write(data)
        file.close()


    def browseInput (self):
        filetypes = (
            ('show file', '*.shw'),
            ('show backup', '*.sbk')
        )

        startPath = self.inputPathBox.get()

        if (startPath == ""):
            startPath = os.path.expanduser('~')

        filename = fd.askopenfilename(
            title='open Showfile',
            initialdir=startPath,
            filetypes=filetypes)
        
        self.inputPathBox.delete(0, 'end')
        self.inputPathBox.insert(0, filename)
    
    def browseOutput (self):
        startPath = self.inputPathBox.get()

        if (startPath == ""):
            startPath = os.path.expanduser('~')

        filename = fd.asksaveasfilename(
            title='save new file',
            initialfile=startPath,
            defaultextension=".shw",
            )
        return filename
    






if __name__ == "__main__":
    app = App()
    app.mainloop()


