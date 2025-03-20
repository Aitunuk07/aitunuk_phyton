# from tkinter import *

# main = Tk()
# main.title("METANIT.COM")
# main.geometry("250x200")

# enabled=IntVar()


# enabled_checkbutton=Checkbutton(text="Male",variable=enabled)
# enabled_checkbutton1=Checkbutton(text="Female",variable=enabled)
# enabled_checkbutton.pack()
# enabled_checkbutton1.pack()

# main.mainloop()


# from  tkinter import *
# from  tkinter import ttk
# main = Tk()
# main.title("METANIT.COM")
# main.geometry("250x200")
# position = {"padx": 6, "pady": 6, "anchor": NW}
# python = "Python"
# java = "Java"
# lang = StringVar(value = java)
# header =ttk.Label (textvariable=lang)
# header.pack(**position)

# python_btn=ttk.Radiobutton(text=python,value=python,variable=lang)
# python_btn.pack(**position)
# java_btn=ttk.Radiobutton(text=java,value=java,variable=lang)
# java_btn.pack(**position)
# main.mainloop()

# from  tkinter import *
# from  tkinter import ttk
# main = Tk()
# main.title("METANIT.COM")
# main.geometry("250x200")
# languages = ["python", "java", "java.script"]
# languages_var = Variable(value=languages)
# languages_listbox = Listbox(listvariable= languages_var)
# languages_listbox.pack(anchor= NW, fill= X, padx= 5, pady= 5)
# main.mainloop()


# from  tkinter import *
# from  tkinter import ttk
# languages = ["python", "java", "C++", "Swift", "java.script"]
# main = Tk()
# main.title("METANIT.COM")
# main.geometry("250x200")

# languages_var = StringVar(value=languages)
# languages_listbox = Listbox(listvariable= languages_var)
# languages_listbox.pack(side = LEFT, fill= BOTH, expand= 1)
# scrollbar = ttk.Scrollbar(orient= "vertical", command= Listbox.yview)
# scrollbar.pack(side= RIGHT, fill= Y)
# Listbox["yscrollcommand"]=scrollbar.set
# main.mainloop()

from tkinter import *
from tkinter import ttk

languages = ["Python", "Java", "C++", "Swift", "JavaScript"]

main = Tk()
main.title("METANIT.COM")
main.geometry("250x200")

languages_var = StringVar(value=languages)

languages_listbox = Listbox(main, listvariable=languages_var)
languages_listbox.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main, orient="vertical", command=languages_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

languages_listbox.config(yscrollcommand=scrollbar.set)

main.mainloop()
