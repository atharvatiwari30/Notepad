import tkinter as tk
from tkinter import END, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from turtle import color, left, title

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("MS Notepad")


main_menu = tk.Menu()

#New_icon = tk.PhotoImage(file="")
#Open = tk.PhotoImage(file="")
#Save = tk.PhotoImage(file="")
#SaveAs = tk.PhotoImage(file="")
#ExitButton = tk.PhotoImage(file="")

file = tk.Menu(main_menu,tearoff = False)

#Edit manu icon:

#Copy_icon = tk.PhotoImage(file="")
#Paste = tk.PhotoImage(file="")
#Cut = tk.PhotoImage(file="")
#SaveAs = tk.PhotoImage(file="")
#ExitButton = tk.PhotoImage(file="")

edit = tk.Menu(main_menu,tearoff = False)

#tool_bar = tk.PhotoImage(file="Location")
#status_bar = t.PhotoImage(file="Location")

view = tk.Menu(main_menu,tearoff = False)

#color theme:

#LightTheam = tk.PhotoImage(file="Location")
#LightPlus = tk.PhotoImage(file="Location")
#DarkTheme = tk.PhotoImage(file="Location")
#RedTheme = tk.PhotoImage(file="Location")
#Monica = tk.PhotoImage(file="Location")
#Night = tk.PhotoImage(file="Location")

#color_theme = tk.Menu(main_menu,tearoff=False)


help = tk.Menu(main_menu,tearoff = False)


main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Help",menu=help)
#main_menu.add_cascade(label="Color Theme",menu=color_theme)


file.add_command(label="New",compound=tk.LEFT,accelerator="Ctrl+N")
file.add_command(label="Open",compound=tk.LEFT,accelerator="Ctrl+O")
file.add_command(label="Save",compound=tk.LEFT,accelerator="Ctrl+s")
file.add_command(label="Save As",compound=tk.LEFT,accelerator="Ctrl+Alt+s")
file.add_command(label="Exit",compound=tk.LEFT,accelerator="Ctrl+")

edit.add_command(label="Copy",compound=tk.LEFT,accelerator="Ctrl+c")
edit.add_command(label="Paste",compound=tk.LEFT,accelerator="Ctrl+v")
edit.add_command(label="Cut",compound=tk.LEFT,accelerator="Ctrl+x")
edit.add_command(label="Clear All",compound=tk.LEFT,accelerator="Ctrl+Alt+x")
edit.add_command(label="Find",compound=tk.LEFT,accelerator="Ctrl+f")

view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,compound=tk.LEFT)
view.add_checkbutton(label="Status Bar",onvalue=True,offvalue=0,compound=tk.LEFT)

#color_icons = (light_plus_icon,light_theme,dark_theme,red_theme,monica_theme,night_theme)
#color_dict = {
  # 'Light Default' : ('#000000',"ffffff"),
   #'Dark' : ('#c4c4c4','#2d2d2d'),
   #'Monica' : ('#d3b774','#474747'),
    #'Night Blue' : ('#ededed','#6b9dc2')
#}

#count = 0
#for i in color_dict:
 #   color_theme.add_radiobutton(label=i,image=color_icons[count],compound=tk.LEFT)
  #  count+=1

help.add_command(label="View Help",compound=tk.LEFT)
help.add_command(label="Send Feed-Back",compound=tk.LEFT)

tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP,fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar
font_box = ttk.Combobox(tool_bar_label,width=30,textvariable=font_family,state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx= 5,pady = 5)


size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state ="readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

bold_btn = ttk.Button(tool_bar_label,text="Bold")
bold_btn.grid(row=0,column=2,padx=5)

italic_btn = ttk.Button(tool_bar_label,text="Italic")
italic_btn.grid(row=0,column=3,padx=5)

underline = ttk.Button(tool_bar_label,text="Underline")
underline.grid(row=0,column=4,padx=5)

left_align = ttk.Button(tool_bar_label,text="Left Align")
left_align.grid(row=0,column=5,padx=5)

right_align = ttk.Button(tool_bar_label,text="Rigt Align")
right_align.grid(row=0,column=6,padx=5)

center_align = ttk.Button(tool_bar_label,text="Center")
center_align.grid(row=0,column=7,padx=5)

text_editor = tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# status bar and word count:

status_bars  = ttk.Label(main_application,text="Status Bar")
status_bars.pack(side = tk.BOTTOM)
text_change= False

def change_word(event = None):
  global text_change
  if text_editor.edit_modified():
    text_change = True
    word = len(text_editor.get(1.0,"end-1c").split())
    chararcter = len(text_editor.get(1.0,"end-1c").replace(" "," "))
    status_bars.config(text=f"charecter:{chararcter} word:{word}")
  text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_word)


# font family and function

font_now = "Arial"
font_size_now = 16


def change_font(main_application):
  global font_now
  font_now = font_family.get()
  text_editor.configure(font=(font_now,font_size_now))
  
def change_size(main_application):
  global font_size_now
  font_size_now = size_variable.get()
  text_editor.configure(font=(font_now,font_size_now))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

#bold function:

def bold_fun():
  text_get = tk.font.Font(font=text_editor["font"])
  if text_get.actual()["weight"] == "normal":
    text_editor.configure(font=(font_now,font_size_now,"bold"))
  if text_get.actual()["weight"] == "bold":
    text_editor.configure(font=(font_now,font_size_now,"normal"))
bold_btn.configure(command = bold_fun)

#italic function:
def italic_fun():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"]=="roman":
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"]=="italic":
        text_editor.configure(font=(font_now,font_size_now,"roman"))
italic_btn.configure(command = italic_fun)


#underline function:

def under_line():
  text_get = tk.font.Font(font=text_editor["font"])
  if text_get.actual()["underline"]==0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
  if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))
underline.configure(command = under_line)


# function for left align:

def left_a():
  text_get_all = text_editor.get(1.0,"end")
  text_editor.tag_config("left",justify=tk.LEFT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_get_all,"left")
left_align.configure(command=left_a)

def right_a():
  text_get_all = text_editor.get(1.0,"end")
  text_editor.tag_config("right",justify=tk.RIGHT)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_get_all,"right")
right_align.configure(command=right_a)

def center_a():
  text_get_all = text_editor.get(1.0,"end")
  text_editor.tag_config("center",justify=tk.CENTER)
  text_editor.delete(1.0,tk.END)
  text_editor.insert(tk.INSERT,text_get_all,"center")
center_align.configure(command=center_a)


file_url =" "
def new_file(event = None):
  global text_url
  text_url = " "
  text_editor.delete(1.0,tk.END)




def save_file(self):
        if self.file_name:
            with open(self.file_name, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.file_name = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                                          defaultextension=".txt", 
                                                          filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
            if self.file_name:
                with open(self.file_name, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.root.title(f"Notepad - {self.file_name}")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()

main_application.config(menu= main_menu)

main_application.mainloop()
