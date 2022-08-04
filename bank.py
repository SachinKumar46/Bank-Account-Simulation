from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog   #(filedialog - browser button for take any audio file video file,images etc )
import os       #(rename)
import shutil   #(cut, copy, paste)

win=Tk()
win.state("zoomed")
win.configure(bg="orange")

title=Label(win,text="Bank Account Simulation", font=("arail",50,"bold","underline"),bg="orange",fg="blue")
title.pack()
 
logo_pic = Image.open("images/logo.jpg")
logo_pictk=ImageTk.PhotoImage(logo_pic.resize((300,100)),master=win)

lbl_logo = Label(win, image=logo_pictk)
lbl_logo.place(relx=0, rely=0)

my_pic=Image.open("images/my.jpg")
my_pictk=ImageTk.PhotoImage(my_pic.resize((200,100)),master=win)

mypic_label=Label(win,image=my_pictk)
mypic_label.place(relx=.87,rely=0)

default_pic = ImageTk.PhotoImage(Image.open("images/profile pic.jpg").resize((140,130)), master=win)

import sqlite3
con=sqlite3.connect(database="bank4.sqlite")
cur=con.cursor
try:
    con.execute("create table user(acn integer primary key autoincrement,name text,pass text,email text,mob float,type text,bal float) ")
    con.execute("create table txn (acn integer, date_time text, amt integer, txn_type text, updated_bal float ) ")
    con.commit()    
    print("table created")
except:
    print("table already exits")    
    con.close()

def home_screen():
    frm=Frame(win)
    frm.configure(bg="green")  
    frm.place(x=1,y=100 ,relheight=1 ,relwidth=1 ) 

#   where i do image place for background in frm 
    backgd=Image.open("images/pic1.jpg")  
    backgd_tk=ImageTk.PhotoImage(backgd,master=frm)
    
    backgd_label = Label(win, image=backgd_tk)
    backgd_label.place(relx=1, rely=1)
     
    def newuser():
        frm.destroy()         
        newuser_screen()

    def newforget():
        frm.destroy()
        newforget_screen()  

    def newlogin():
        act= acn_entry.get() 
        pas=pass_entry.get()
        if(len(act)==0 or len(pas)==0):
            messagebox.showerror("validation","please fill both fields")
        elif (not act .isdigit() ):
            messagebox.showerror("validation", "Account must be digit")
        else:
            #for authentication
            con=sqlite3.connect(database="bank4.sqlite") 
            cur=con.cursor()
            cur.execute("select* from user where acn=? and pass=?",(act,pas))
            global tup
            tup=cur.fetchone()
            if (tup==None):
                messagebox.showerror("login","Invalid acn/pass")
            else:    
                frm.destroy()
                newlogin_screen()
    
    def reset():
        acn_entry.delete(0,"end")
        pass_entry.delete(0,"end")
        acn_entry.focus()     #cursor billing on entry of acn       
    
    acn_label=Label(frm,text="Account",font=("arial",20,"bold"),bg="green")
    acn_label.place(relx=.36,rely=.1)    

    acn_entry=Entry(frm,font=("arial",20,"bold"),bd=5)
    acn_entry.place(relx=.46,rely=.1)

    pass_label=Label(frm,text="Password",font=("arial",20,"bold"),bg="green")
    pass_label.place(relx=.36,rely=.2)

    pass_entry=Entry(frm,font=("arial",20,"bold"),bd=5,show="*")
    pass_entry.place(relx=.46,rely=.2)

    login_button=Button(frm,text="login",font=("arial",20,"bold"),bg="green",fg="yellow",width=7,bd=5,command=newlogin)
    login_button.place(relx=.36,rely=.3)
    
    forget_button=Button(frm,text="Forget ",font=("arial",20,"bold"),bg="green",fg="yellow",width=7,bd=5,command=newforget)
    forget_button.place(relx=.47,rely=.3)
    
    reset_button=Button(frm,text="Reset",font=("arial",20,"bold"),bg="green",fg="yellow",width=7,bd=5,command=reset)
    reset_button.place(relx=.58,rely=.3)
    
    newuser_button=Button(frm,text="New User",font=("arial",20,"bold"),bg="green",fg="yellow",width=8,bd=5,command=newuser)
    newuser_button.place(relx=.46,rely=.4)



def newuser_screen():
    frm=Frame(win)
    frm.configure(bg="green")  
    frm.place(x=1,y=100 ,relheight=1 ,relwidth=1 )

    def back():
        home_screen()
        frm.destroy() 

    def submit():
        name=name_entry.get()               
        pas=pass_entry.get()
        mob=mob_entry.get()
        mail=email_entry.get()
        cotype=type_combo.get()
        bal=1000
        
        con=sqlite3.connect(database="bank4.sqlite") 
        con.cursor()
        con.execute("insert into user(name,pass,email,mob,type,bal) values(?,?,?,?,?,?)",(name,pas,mob,mail,cotype,bal)) 
        con.commit()
        con.close() 

        con=sqlite3.connect(database="bank4.sqlite") 
        cur=con.cursor()
        cur.execute("select max(acn) from user")  
        tup=cur.fetchone()
        messagebox.showinfo("Account",f"Account  open with Acn :{tup[0]}")
        con.close()      
    
    back_Button = Button(frm, text="Back", font=("arial", 15, "bold"), bg="green", fg="yellow", width=5, bd=5, command=back)
    back_Button.place(relx=.95, rely=0)
    
    submit_Button = Button(frm, text="submit", font=("arial", 20, "bold"), bg="green", fg="yellow", width=7, bd=5,command=submit)
    submit_Button.place(relx=.48, rely=.6)

    name_label = Label(frm, text="Name", font=("arial", 20, "bold"), bg="green")
    name_label.place(relx=.36, rely=.1)

    name_entry = Entry(frm, font=("arial", 20, "bold"),bd=5)
    name_entry.place(relx=.46, rely=.1)

    pass_label = Label(frm, text="Pass", font=("arial", 20, "bold"), bg="green")
    pass_label.place(relx=.36, rely=.2)

    pass_entry = Entry(frm, font=("arial", 20, "bold"),bd=5,show="*")
    pass_entry.place(relx=.46, rely=.2)
    
    mob_label = Label(frm, text="Mob", font=("arial", 20, "bold"), bg="green")
    mob_label.place(relx=.36, rely=.3)

    mob_entry = Entry(frm, font=("arial", 20, "bold"),bd=5)
    mob_entry.place(relx=.46, rely=.3)

    email_label = Label(frm, text="Email", font=("arial", 20, "bold"), bg="green")
    email_label.place(relx=.36, rely=.4)

    email_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    email_entry.place(relx=.46, rely=.4)

    type_label = Label(frm, text="Type", font=("arial", 20, "bold"), bg="green")
    type_label.place(relx=.36, rely=.5)

    type_combo =Combobox(frm,values=["saving","current"] ,font=("arial", 20, "bold"))
    type_combo.place(relx=.46, rely=.5)
    type_combo.current(0)

    """ how i do set validation on new user
    s=("python is a simple lamguage created by Guido VAN Rossom in 1991 i5")   
    l=re.findall("i[0-9]",s)
    print(l) """

def newforget_screen():
    frm=Frame(win)
    frm.configure(bg="green")  
    frm.place(x=1,y=100 ,relheight=1 ,relwidth=1 )

    def back():
        home_screen()
        frm.destroy()

    def submit():
        acn=acn_entry.get()
        mob=mob_entry.get()
        mail=email_entry.get()
        con=sqlite3.connect(database="bank4.sqlite")
        cur=con.cursor()
        cur.execute("select pass from user where acn=? and mob=? and email=?",(acn,mob,mail))
        p=cur.fetchone()
        con.close() 
        if(p==None): 
            messagebox.showerror("Recovery"," Details not found")
        else:
            messagebox.showinfo("Recovery",f"your pass  : {p[0]}") 

        
        if(p==None):
                messagebox.showerror("Recovery","Details not found")
        else:
            messagebox.showinfo("Recovery",f"Your pass:{p[0]}")   
    con.close()             

    back_button=Button(frm,text="back",font=("arial",15,"bold"),bg="green",fg="yellow",width=7,bd=5,command=back)    
    back_button.place(relx=.94,rely=0)

    submit_button=Button(frm,text="submit",font=("arial",20,"bold"),bg="green",fg="yellow",bd=5,command=submit)
    submit_button.place(relx=.45,rely=.4)

    acn_label = Label(frm, text="Account", font=( "arial", 20, "bold"), bg="green")
    acn_label.place(relx=.36, rely=.1)

    acn_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    acn_entry.place(relx=.46, rely=.1)

    mob_label = Label(frm, text="email", font=("arial", 20, "bold"), bg="green")
    mob_label.place(relx=.36, rely=.2)

    mob_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    mob_entry.place(relx=.46, rely=.2)

    email_label = Label(frm, text="mob", font=("arial", 20, "bold"), bg="green")
    email_label.place(relx=.36, rely=.3)

    email_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    email_entry.place(relx=.46, rely=.3)



def newlogin_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def logout():
        frm.destroy()
        home_screen()


    def details():
        frm.destroy()
        detalis_screen()

    def deposit():
        frm.destroy()
        deposit_screen()

    def withdraw():
        frm.destroy()
        withdraw_screen()

    def history():
        frm.destroy()
        history_screen()  

    def profileupdate():
        frm.destroy()
        profileupdate_screen()

    def pichange():
        path = filedialog.askopenfilename()
        index = path.rindex(".")
        ext = path[index+1:]
        shutil.copy(path, f"images/{tup[0]}.{ext}")
        
        pic=ImageTk.PhotoImage(Image.open(f"images/{tup[0]}.{ext}").resize((140, 130)), master=win)
    
    
    logout_button = Button(frm, text="logout", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=logout)
    logout_button.place(relx=.94, rely=0)

    wel_label=Label(frm,text=f"Welcome  :  {tup[1]} ",font=("arial",20,"bold"),bg="green",fg="black")
    wel_label.place(relx=0,rely=0)
    
    lbl_pic= Label(frm,image=default_pic)
    lbl_pic.place(relx=0,rely=.06)


    imgs=os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image=pic

    def pichange():
        path = filedialog.askopenfilename() 
        index = path.rindex(".")
        ext = path[index+1:]
        shutil.copy(path, f"images/{tup[0]}.{ext}")
        
        default_pic=ImageTk.PhotoImage(Image.open(f"images/{tup[0]}.{ext}").resize((140, 130)), master=win)
        lbl_pic.configure(image=default_pic)
        lbl_pic.image=default_pic 
     
    prof_upt_button = Button(frm, text="profile update", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5, command=profileupdate)
    prof_upt_button.place(relx=.38, rely=.2)

    pic_change_button = Button(frm, text="pic change", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5,command=pichange)
    pic_change_button.place(relx=.53, rely=.2)
 
    withdraw_button = Button(frm, text="withdraw", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5,command=withdraw)
    withdraw_button.place(relx=.38, rely=.3)

    deposit_button = Button(frm, text="deposit", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5,command=deposit)
    deposit_button.place(relx=.53, rely=.3)

    details_button = Button(frm, text="details", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5,command=details)
    details_button.place(relx=.38, rely=.4)

    history_button = Button(frm, text="Txn history", font=("arial", 15, "bold"), bg="green", fg="yellow", width=12, bd=5,command=history)
    history_button.place(relx=.53, rely=.4)

def detalis_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def logout():
        home_screen()
        frm.destroy()

    def back():
        frm.destroy()
        newlogin_screen()

    detail = Label(frm, text="Details", font=("arial", 30, "bold"), bg="green")
    detail .pack()

    back_button=Button(frm,text="back",font=("arial",15,"bold"),bg="green",fg="yellow",width=7,bd=5,command=back)
    back_button.place(relx=.94,rely=0)    

    logout_button = Button(frm, text="logout", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=logout)
    logout_button.place(relx=.46, rely=.6)

    wel_label=Label(frm,text=f"Welcome : {tup[1]}",font=("arial",20,"bold"),bg="green",fg="black")
    wel_label.place(relx=0,rely=0)
    
    lbl_pic = Label(frm, image=default_pic)
    lbl_pic.place(relx=0,rely=.06)

    
    imgs = os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image = pic


    
    con = sqlite3.connect(database="bank4.sqlite")
    cur = con.cursor()
    cur.execute("select* from user where acn=? and pass=?", (tup[0], tup[2]))
    row = cur.fetchone()

    data = f"""
    Acn     :   {row[0]}
    Name    :   {row[1]}
    Pass    :   {row[2]}
    \tEmail   :   {row[3]}
    \tMob     :   {row[4]}
    \tType    :   {row[5]}   
    \tBal     :   {row[6]} """

    data_label=Label(frm,text=data,font=("arial",20,"bold"),bg="green",fg="yellow")
    data_label.place(relx=.35,rely=.15)    

def deposit_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def submit():
        amt=int(amt_entry.get())
        con=sqlite3.connect(database="bank4.sqlite")
        cur=con.cursor()
        cur.execute("select bal from user where acn=?",(tup[0],))
        t=cur.fetchone() 
        bal=t[0]
        bal=bal+amt
        con.close()

        con=sqlite3.connect(database="bank4.sqlite")
        cur=con.cursor()
        cur.execute("update user set bal=? where acn=?",(bal,tup[0]))
        con.commit()
        messagebox.showinfo("Deoposit","balance deposited")

        con=sqlite3.connect(database="bank4.sqlite")
        cur=con.cursor()
        from datetime import datetime
        dt=str(datetime.now())
        cur.execute("insert into txn values(?,?,?,?,?)",(tup[0],dt,amt,"credit",bal)) 
        con.commit()
        con.close()   
    
    
    def back():
        frm.destroy()
        newlogin_screen()
 
    name=Label(frm,text="Deposit",font=("arial",30,"bold"),bg="green")
    name.pack()

    back_button = Button(frm, text="back", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=back)
    back_button.place(relx=.94, rely=0)

    submit_button = Button(frm, text="submit", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=submit)
    submit_button.place(relx=.46, rely=.35)

    wel_label = Label(frm, text=f"Welcome :  {tup[1]} ", font=("arial", 20, "bold"), bg="green", fg="black")
    wel_label.place(relx=0,rely=0)
    
    amt_lbl=Label(frm,text="Ammount",font=("arial",20,"bold"),bg="green")
    amt_lbl.place(relx=.35,rely=.2)

    amt_entry=Entry(frm,font=("arial",20,"bold"),bd=5,)
    amt_entry.place(relx=.46,rely=.2)
    
    lbl_pic = Label(frm, image=default_pic)
    lbl_pic.place(relx=0,rely=.06)

    imgs = os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image = pic


def withdraw_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def back():
        frm.destroy()
        newlogin_screen() 

    def submit():
        amt = int(amt_entry.get())
        con = sqlite3.connect(database="bank4.sqlite")
        cur = con.cursor()
        cur.execute("select bal from user where acn=?", (tup[0],))
        t = cur.fetchone()
        bal = t[0]
        if bal>amt:
            bal = bal-amt

            con = sqlite3.connect(database="bank4.sqlite")
            cur = con.cursor()
            cur.execute("update user set bal=? where acn=?", (bal, tup[0]))
            con.commit()
            messagebox.showinfo("withdraw", "ammount withdraw")
            con.close()

            con = sqlite3.connect(database="bank4.sqlite")
            cur = con.cursor()
            from datetime import datetime
            dt = str(datetime.now())
            cur.execute("insert into txn values(?,?,?,?,?)",(tup[0], dt, amt, "debit", bal))
            con.commit()
            con.close()
        else:
            messagebox.showerror("balance","insufficent balance")    

    

    name=Label(frm,text="Withdraw",font=("arial",30,"bold"),bg="green")
    name.pack() 

    amt_label=Label(frm,text="submit",font=("arial",20,"bold"),bg="green",fg="yellow")
    amt_label.place(relx=.35,rely=.2)       

    amt_entry=Entry(frm,font=("arial",20,"bold"),bd=5)
    amt_entry.place(relx=.46,rely=.2)
    
    back_button = Button(frm, text="back", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=back)
    back_button.place(relx=.94, rely=0)

    submit_button=Button(frm,text="submit",font=("arial",20,"bold"),bg="green",fg="yellow",command=submit)
    submit_button.place(relx=.45,rely=.4)

    wel_label=Label(frm,text=f"Welcome :  {tup[1]}",font=("arial",20,"bold"),bg="green",fg="black")
    wel_label.place(relx=0,rely=0)
    
    lbl_pic = Label(frm, image=default_pic)
    lbl_pic.place(relx=0,rely=.06)

    imgs = os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(
                f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image = pic


def history_screen():
    frm = Frame(win)
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def back():
        frm.destroy()
        newlogin_screen()

    name = Label(frm, text="History", font=("arial", 30, "bold"), bg="green")
    name.pack()

    back_button = Button(frm, text="back", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=back)
    back_button.place(relx=.94, rely=0)

    wel_label = Label(frm, text=f"Welcome :   {tup[1]}", font=("arial", 20, "bold"), bg="green", fg="black")
    wel_label.place(relx=0, rely=0)

    lbl_pic = Label(frm, image=default_pic)
    lbl_pic.place(relx=0, rely=.06)

    imgs = os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image = pic

    con=sqlite3.connect(database="bank4.sqlite")
    cur=con.cursor()
    cur.execute("select* from txn where acn=?",(tup[0],))
    txn_data="(Act)     (date_time)  (amt)   (txn_type)     (update_bal)\n"
    all_data=cur.fetchall()
    for t in all_data:
        t=map(str,t) #make every element in string
        t1=" ".join(t)
        txn_data=txn_data+t1+"\n"

    lbl_txndata=Label(frm,text=txn_data,font=("arial",20,"bold"),bg="green",fg="yellow") 
    lbl_txndata.place(relx=.2,rely=.2)    

def profileupdate_screen():
    frm = Frame(win) 
    frm.configure(bg="green")
    frm.place(x=1, y=100, relheight=1, relwidth=1)

    def update():
        name=name_entry.get()
        pas=pass_entry.get()
        mob=mob_entry.get()
        mail=email_entry.get()
        con=sqlite3.connect(database="bank4.sqlite")
        cur=con.cursor()
        cur.execute("update user set name=?,pass=?,mob=?,email=? where acn=?",(name,pas,mob,mail,tup[0]))
        con.commit()
        con.close()
        messagebox.showinfo("update","details updated")

    def back():
        frm.destroy()
        newlogin_screen()

    lbl_pic = Label(frm, image=default_pic)
    lbl_pic.place(relx=0, rely=.06)

    imgs=os.listdir("images")
    for img in imgs:
        if (img.startswith(str(tup[0]))):
            pic = ImageTk.PhotoImage(Image.open(f"images/{img}").resize((140, 130)), master=win)
            lbl_pic.configure(image=pic)
            lbl_pic.image=pic

    name = Label(frm, text="Profile update", font=("arial", 30, "bold"), bg="green")
    name.pack()

    back_button = Button(frm, text="back", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=back)
    back_button.place(relx=.94, rely=0)

    update_button = Button(frm, text="Update", font=("arial", 15, "bold"), bg="green", fg="yellow", width=7, bd=5, command=update)
    update_button.place(relx=.46, rely=.6)

    wel_label = Label(frm, text=f"Welcome :  {tup[1]}", font=("arial", 20, "bold"), bg="green", fg="black")
    wel_label.place(relx=0, rely=0)

    name_label = Label(frm, text="Name", font=("arial", 20, "bold"), bg="green")
    name_label.place(relx=.36, rely=.1)

    name_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    name_entry.place(relx=.46, rely=.1)
    name_entry.insert(0,tup[1])

    pass_label = Label(frm, text="Pass", font=("arial", 20, "bold"), bg="green")
    pass_label.place(relx=.36, rely=.2)

    pass_entry = Entry(frm, font=("arial", 20, "bold"), bd=5, show="*")
    pass_entry.place(relx=.46, rely=.2)
    pass_entry.insert(0, tup[2])

    mob_label = Label(frm, text="Mob", font=("arial", 20, "bold"), bg="green")
    mob_label.place(relx=.36, rely=.3)

    mob_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    mob_entry.place(relx=.46, rely=.3)
    mob_entry.insert(0, tup[4])

    email_label = Label(frm, text="Email", font=("arial", 20, "bold"), bg="green")
    email_label.place(relx=.36, rely=.4)

    email_entry = Entry(frm, font=("arial", 20, "bold"), bd=5)
    email_entry.place(relx=.46, rely=.4)
    email_entry.insert(0, tup[3])

home_screen() 
win.mainloop()