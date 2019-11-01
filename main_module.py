from tkinter import *
import os 
window = Tk() 
#use cmdlet to clear up dns cache
os.popen('ipconfig/flushdns')
#Retrieve Func 
def save(): 
    web_txt = web_link.get() 
    linko = '127.0.0.1       ' + web_txt + '\n'
    with open('hfile', 'a+') as file:
        file.write(linko)
#Windows title bar 
window.title('Blocky')
#Window Box Resolution
window.geometry('200x120')
#Label Title
label_1 = Label(window, text = 'Enter website name including www.')
label_1.pack()
#Name Entry
web_link = StringVar()
web_link = Entry(window)
web_link.pack()
#Save Button
save_button = Button (window, text = "Save", command = save)
save_button.pack() 
#Quit Button
Button(window, text = 'Quit', command = window.quit).pack()
#Credit Label
Label(window, text = 'By Reaz Tahmidur Rahman ').pack() 

window.mainloop() 
