from tkinter import filedialog 

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Select a File", 
                                            filetypes = (
                                                ( "all files", "*.*" ),
                                                ( "Text files", "*.txt*") 
                                            )
                                        )
    return filename