import random
import csv
from tkinter import *

def clicked(filename,table):
    lbl.configure(text = "I just got clicked")

def create_effects(filename,table):
    with open('paramon.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            effect_table.append(row)
    return(effect_table)
    
def starting_effects(table,effects,used):
    for x in range(0,8):
        effects.append(table[x])
        used.append(table[x])
    del table[0:8]
    return(table,effects,used)

def new_button(name,btntxt,cmd,col,rw):
    name = Button(root, text = btntxt, command = cmd)
    name.grid(column=col,row=rw)
    return(name)

def new_lbl(lblname,lbltxt,col,rw):
    lblname.config(text = lbltxt)
    lblname.grid(column=col,row=rw)
    return(lblname)

def new_round(table,effects,lbl,used,col,rw):
    index1 = random.randrange(len(effects))
    active_effect = effects[index1]
    new_lbl(lbl,"You use " + active_effect[1],col,rw)
    effects[index1] = table[0]
    used.append(table[0])
    del table[0]
    return(table,effects,used)

def get_started():
    create_effects('paramon.csv',effect_table)
    result1 = Label(root, text = str(len(effect_table)) + " effects set! ")
    result1.grid(column=5,row=2)
    btn1.destroy()

def get_effects(effect_set):
    effect_list = ""
    for stat in effect_set:
        effect_list = effect_list + "\n" + str(stat[1])
    return(effect_list)
	
effect_table = []
effect_set = []
used_effects = []
	
root = Tk()
root.title("What's a Paramon to do?")
root.geometry('700x350')

greet = Label(root, text = "Let's get started!")
greet.grid(column=1, row=0)

lbl1 = Label(root, text = "Set the effects table?")
lbl1.grid(column=1,row=2)
btn1 = Button(root, text = "Set", command=get_started)
btn1.grid(column=3, row=2)

lbl2 = Label(root, text = "Shuffle the effects table?")
lbl2.grid(column=1,row=3)
result2 = Label(root, text = "")
btn2 = new_button("btn2","Shuffle",
                  lambda:[random.shuffle(effect_table),
                    new_lbl(result2,"Effects table shuffled",5,3),
                    btn2.destroy()],3,3)

lbl3 = Label(root, text = "Generate starting effects?")
lbl3.grid(column=1,row=4)
lbl5 = Label(root, text = "")
lbl6 = Label(root, text="")
btn3 = new_button("btn3","Generate",
                  lambda: [starting_effects(effect_table,effect_set,used_effects),
                    new_lbl(lbl5,"Your starting effects are: ",7,5),
                    new_lbl(lbl6,get_effects(effect_set),7,6),
                    btn3.destroy()],3,5)

lbl4 = Label(root, text = "Start first round?")
lbl4.grid(column=1,row=7)
effects_remain = Label(root, text = "")
used = Label(root, text = "")
btn4 = Button(root, text="Start",command=lambda:[new_round(effect_table,effect_set,used,used_effects,5,6),
                                                    lbl5.configure(text="Your new effects are: "),
                                                    lbl6.configure(text = get_effects(effect_set)),
                                                     new_lbl(effects_remain,"There are " + str(len(effect_table)) + " effects remaining.",5,10),
                                                     lbl4.configure(text="Next Round: ")])
btn4.grid(column=3,row=7)

quit_btn = Button(root, text="All done",command=root.destroy)
quit_btn.grid(column=5,row=12)

root.mainloop()