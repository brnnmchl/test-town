import random
import csv
from tkinter import *

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

def new_button(container,name,btntxt,cmd,col,rw,stick):
    name = Button(container,text=btntxt,font=("OCR A Extended",11),bg="darkgreen",fg="white",command=cmd)
    name.grid(column=col,row=rw,pady=5,padx=5,sticky=stick)
    return(name)

def new_lbl(lblname,lbltxt,col,rw,colspan,stick,fnt_typ,fnt_sz,bkgd):
    lblname.config(text = lbltxt,font=(fnt_typ,fnt_sz),bg=bkgd)
    lblname.grid(column=col,row=rw,columnspan=colspan,pady=5,padx=5,sticky=stick)
    return(lblname)

def new_round(table,effects,lbl,used,col,rw,colspan,stick):
    index1 = random.randrange(len(effects))
    active_effect = effects[index1]
    new_lbl(lbl,"You use " + active_effect[1],col,rw,colspan,stick,"OCR A Extended",11,"palegoldenrod")
    lbl.configure(fg="deeppink4")
    effects[index1] = table[0]
    used.append(table[0])
    del table[0]
    return(table,effects,used)

def get_started():
    create_effects('paramon.csv',effect_table)
    result1 = Label(set_up_overlay, text = str(len(effect_table)) + " effects set! ",
                    font=("OCR A Extended",11),bg="palegoldenrod")
    result1.grid(column=2,row=0,pady=5,padx=5,sticky=E)
    btn1.destroy()

def get_effects(effect_set):
    effect_list = ""
    for stat in effect_set:
        effect_list = effect_list + "\n" + str(stat[1])
    return(effect_list)

def make_csv(used,ent_name):
    filename = ent_name.get() + ".csv"
    with open(filename,"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(used)
	
effect_table = []
effect_set = []
used_effects = []
	
# set up window
root = Tk()
root.title("What's a Paramon to do?")
root.geometry('525x575')
root.config(bg="black")


# set up title frame
title = Frame(root,bg="darkorange2",bd=5,relief="ridge")
title.grid(column=0,row=0,pady=5,padx=5)

greet = Label(title, text = "WHAT'S A PARAMON TO DO?!",
              font=("OCR A Extended",20),fg="navy",bg="palegoldenrod")
greet.grid(column=0,row=0,sticky=N)


# set up effects set up frame
set_up = Frame(root,bg="darkorange2",bd=5,relief="ridge")
set_up.grid(column=0,row=1,pady=5,padx=5,sticky=N)
set_up_overlay = Frame(set_up,bg="palegoldenrod",bd=0,relief="flat")
set_up_overlay.grid(column=0,row=0)

lbl1 = Label(set_up_overlay, text = "Set the effects table?",font=("OCR A Extended",11),bg="palegoldenrod")
lbl1.grid(column=0,row=0,pady=5,padx=5,sticky=W)
buffer_lbl1 = Label(set_up_overlay,text="buffer",bg="palegoldenrod",fg="palegoldenrod")
buffer_lbl1.grid(column=1,row=0)
btn1 = Button(set_up_overlay, text = "Set",font=("OCR A Extended",11),bg="darkgreen",fg="white", command=get_started)
btn1.grid(column=2,row=0,pady=5,padx=5)

lbl2 = Label(set_up_overlay, text = "Shuffle the effects table?",font=("OCR A Extended",11),bg="palegoldenrod")
lbl2.grid(column=0,row=1,pady=5,padx=5,sticky=W)
buffer_lbl2 = Label(set_up_overlay,text="buffer",bg="palegoldenrod",fg="palegoldenrod")
buffer_lbl2.grid(column=1,row=1)
result2 = Label(set_up_overlay, text = "")
btn2 = new_button(set_up_overlay,"btn2","Shuffle",
                  lambda:[random.shuffle(effect_table),
                    new_lbl(result2,"Effects table shuffled",2,1,1,E,"OCR A Extended",11,"palegoldenrod"),
                    btn2.destroy()],2,1,NW)


# set up the effects zone frame
fx_zone = Frame(root,bg="darkorange2",bd=5,relief="ridge")
fx_zone.grid(column=0,row=2,pady=5,padx=5,sticky=N)
fx_zone_overlay = Frame(fx_zone,bg="palegoldenrod",bd=0,relief="flat")
fx_zone_overlay.grid(column=0,row=0)

lbl3 = Label(fx_zone_overlay, text = "Generate starting effects?",font=("OCR A Extended",11),bg="palegoldenrod")
lbl3.grid(column=0,row=0,sticky=W)
lbl5 = Label(fx_zone_overlay, text="",font=("OCR A Extended",11),bg="palegoldenrod")
lbl6 = Label(fx_zone_overlay, text="",font=("OCR A Extended",11),bg="palegoldenrod")
btn3 = new_button(fx_zone_overlay,"btn3","Generate",
                  lambda: [starting_effects(effect_table,effect_set,used_effects),
                    new_lbl(lbl5,"Your starting effects are: ",0,4,2,N,"OCR A Extended",11,"palegoldenrod"),
                    new_lbl(lbl6,get_effects(effect_set),0,5,2,N,"OCR A Extended",11,"palegoldenrod"),
                    btn3.destroy(),lbl3.destroy()],1,0,W)

lbl4 = Label(fx_zone_overlay, text = "Start first round?",font=("OCR A Extended",11),bg="palegoldenrod")
lbl4.grid(column=0,row=1,pady=5,padx=5,sticky=NW)
effects_remain = Label(fx_zone_overlay, text = "")
used = Label(fx_zone_overlay, text = "")
btn4 = Button(fx_zone_overlay, text="Get effects",font=("OCR A Extended",11),bg="darkgreen",fg="white",
              command=lambda:[new_round(effect_table,effect_set,used,used_effects,0,2,2,N),
                                lbl5.configure(text="Your new effects are: "),
                                lbl6.configure(text = get_effects(effect_set)),
                                new_lbl(effects_remain,"There are " + str(len(effect_table)) + " effects remaining.",
                                        0,3,2,N,"OCR A Extended",11,"palegoldenrod"),
                                lbl4.configure(text="Next Round: ")])
btn4.grid(column=1,row=1,pady=5,padx=5,sticky=NW)


# frame out the end of session options
end_sesh = Frame(root,bg="darkorange2",borderwidth=5,relief="ridge")
end_sesh.grid(column=0,row=3,pady=5,padx=5,sticky=N)
end_sesh_overlay = Frame(end_sesh,bg="palegoldenrod",bd=0,relief="flat")
end_sesh_overlay.grid(column=0,row=0)

csv_lbl = Label(end_sesh_overlay, text="Enter filename: ",font=("OCR A Extended",11),bg="palegoldenrod")
csv_lbl.grid(column=0,row=0,pady=5,padx=5,sticky=NW)
ent_filename = Entry(end_sesh_overlay)
ent_filename.grid(column=1,row=0,pady=5,padx=5,sticky=NW)
csv_created = Label(end_sesh_overlay,text="")
used_csv_btn = Button(end_sesh_overlay, text="Get used effects",font=("OCR A Extended",11),bg="darkgreen",fg="white",
                      command=lambda: [make_csv(used_effects,ent_filename),
                                       new_lbl(csv_created,"CSV created in root folder!",
                                               1,1,2,NW,"OCR A Extended",11,"palegoldenrod")])
used_csv_btn.grid(column=2,row=0,pady=5,padx=5,sticky=NW)

quit_btn = Button(end_sesh_overlay, text="All done",font=("OCR A Extended",11),bg="firebrick",fg="white",command=root.destroy)
quit_btn.grid(column=0,row=1,pady=5,padx=5,sticky=SW)

# let's get this show on the road
root.mainloop()