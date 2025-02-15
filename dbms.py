from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.messagebox
import re
from datetime import datetime
from tkinter import scrolledtext
from time import sleep
import smtplib
import random
import time
import requests
import bs4
import mysql.connector
from tkcalendar import Calendar

import mysql.connector as my
mydb = my.connect(user='ENTER YOUR USERNAME', password='ENTER YOUR PASSWORD', host='localhost', database='library')



def slider():
    global count,text
    if count>=len(txt):
        count=-1
        text=''
        label.config(text=text)
    else:
        text=text+txt[count]
        label.config(text=text)
    count+=1
    label.after(550,slider)
    
def slider2():
    global count1,text1
    if count1>=len(txt1):
        count1=-1
        text1=''
        label1.config(text=text1)
    else:
        text1=text1+txt1[count1]
        label1.config(text=text1)
    count1+=1
    label1.after(550,slider2)

def toggle_password():
    if passwd_entry.cget('show') == '':
        passwd_entry.config(show='*')
        toggle_btn.config(image=eye_closed)
    else:
        passwd_entry.config(show='')
        toggle_btn.config(image=eye)


def on_enter(event):
    event.widget.configure(bg="#99b3ef")  

def on_leave(event):
    event.widget.configure(bg="#7a96d6") 
def mainscreen():
    global label, text, count, p_name1, p_password1, passwd_entry
    global toggle_btn, eye_closed, eye, txt, txt1, label1, text1, count1

    root = Tk()
    root.withdraw()  
    main_screen = Toplevel()
    main_screen.geometry("1350x700+0+0")
    main_screen.state("zoomed")
    main_screen.title("BookBee")
    main_screen.config(bg="lightblue")
    main_screen.iconbitmap(True, "C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\logo.ico")

    main_screen.bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\LOGIN.jpg")
    bg = Label(main_screen, image=main_screen.bg, bg="snow2").pack()

    p_name1 = StringVar()
    p_password1 = StringVar()

    txt = "Book"
    count = 0
    text = ''
    label = Label(main_screen, text=txt, font=("cooper black", 50), fg="#ffa800", bg="white")
    label.place(x=188, y=50)
    slider()

    txt1 = "Bee "
    count1 = 0
    text1 = ''
    label1 = Label(main_screen, text=txt1, font=("cooper black", 50), fg="black", bg="white")
    label1.place(x=370, y=50)
    slider2()

    login = Label(main_screen, text="LOGIN", font=("courier new", 37, "bold"), fg="white", bg="#4253b1").place(x=970, y=80)

    p_name = Label(main_screen, text="STAFF ID", font=("league spartan", 11, "bold"), fg="white", bg="#4253b1").place(x=875, y=225)
    pname_entry = Entry(main_screen, textvariable=p_name1, font=("league spartan", 13), bg="white")
    pname_entry.place(x=875, y=247, width=350, height=30)

    p_password = Label(main_screen, text="PASSWORD", font=("league spartan", 11, "bold"), fg="white", bg="#4253b1").place(x=875, y=318)
    passwd_entry = Entry(main_screen, textvariable=p_password1, font=("league spartan", 13), show='*', bg="white")
    passwd_entry.place(x=875, y=340, width=350, height=30)
    
    eye = PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\openeye.png")
    eye_closed = PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\closeeye.png") 
    toggle_btn = Button(main_screen, image=eye, width=30, height=25, bg="white", fg="white", bd=0, command=toggle_password)
    toggle_btn.place(x=1185, y=342)

    btn_login = Button(main_screen, bg="#7a96d6", fg="white", bd=2, text="Login", font=("aptos", 13,"bold"), command=selection)
    btn_login.place(x=980, y=425, width=150)
    btn_login.bind("<Enter>", on_enter)
    btn_login.bind("<Leave>", on_leave)

    n_newques = Label(main_screen, text="New to BookBee?", font=("league spartan", 12, "bold"), bg="#4253b1", fg="white").place(x=950, y=462)
    btn_signin = Button(main_screen, bg="#4253b1", fg="orange", bd=0, text="Sign Up", font=("league spartan", 12, "bold"), activebackground="#4253b1", activeforeground="orange", command=signup)
    btn_signin.place(x=1100, y=460, width=63)


def staffsignup():
    global insert_stmt
    global data
    global cursor_reg
    global email1

    fname1=fname.get()
    lname1=lname.get()
    sid1=sid.get()
    password="ADD PASSWORD FOR ADMIN"
    date=datetime.today().strftime('%d-%m-%Y')


    if fname1=='' or lname1=='' or sid1=='':
        tkinter.messagebox.showinfo('BookBee',"Please fill the empty field!")
    else:
        cursor_reg= mydb.cursor()
        sql="SELECT * FROM staffsignup where Sid=%s"
        adr=(sid1,)
        cursor_reg.execute(sql,adr)
        myresult = cursor_reg.fetchall()        
        if myresult:
            tkinter.messagebox.showinfo('BookBee','User already registered!')
        else:
            insert_stmt = (
                           "INSERT INTO staffsignup(Sid,Fname,Lname,Password,Date)"
                           "VALUES (%s,%s,%s,%s,STR_TO_DATE(%s, '%d-%m-%Y'))"
                           )
            data = (sid1,fname1,lname1,password,date)
            cursor_reg.execute(insert_stmt,data)
            sql1=("Insert into stafflogin(Sid,Password)"
                      "VALUES (%s, %s)")
            data1=(sid1,password)
            cursor_reg.execute(sql1,data1)
            mydb.commit()
            frame1.destroy()
    
            

def animation1(count):
    global anima
    im3 = im8[count]

    gif_label3.configure(image=im3)
    count += 1
    if count == frames:
        count = 0
    anima = frame1.after(2, lambda: animation1(count))

def signup():
    global frame1
    global frame1_bg
    global sid
    global fname
    global lname
    global count
    global frames
    global imageObject
    global gif_label3
    global anima
    global im8
    
    sid=StringVar()
    fname=StringVar()
    lname=StringVar()
        
    frame1=Toplevel()
    frame1.geometry("1350x700+0+0")
    frame1.state("zoomed")
    frame1.title("BookBee")
    frame1.iconbitmap(True,"C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\logo.ico")
    frame1.config(bg="white")
    frame1_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\SIGN UP.jpg")
    bg1 = Label(frame1, image=frame1_bg).pack()

    s_id=Label(frame1, text="STAFF  ID",font=("league spartan", 10, "bold"),fg="#191970",bg="#cbe7f5").place(x=285,y=255)
    sid_entry=Entry(frame1,textvariable=sid,font=("league spartan",13),bg="white").place(x=285,y=275,width=250)

    f_name=Label(frame1, text="FIRST NAME",font=("league spartan", 10, "bold"),fg="#191970",bg="#cbe7f5").place(x=285,y=320)
    fname_entry=Entry(frame1,textvariable=fname,font=("league spartan",13),bg="white").place(x=285,y=340,width=250)

    l_name=Label(frame1, text="LAST NAME",font=("league spartan", 10, "bold"),fg="#191970",bg="#cbe7f5").place(x=285,y=385)
    lname_entry=Entry(frame1,textvariable=lname,font=("league spartan",13),bg="white").place(x=285,y=405,width=250)


    btn_signup = Button(frame1,bg='#3c8aff',fg="white",bd=2,text="Sign Up",font=("times new roman",13),command=staffsignup)
    btn_signup.place(x=335,y=470,width=150)
    btn_signup.bind("<Enter>", on_enter)
    btn_signup.bind("<Leave>", on_leave)

    count = 0
    anima = None
    file = "C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\gif_Label.gif"
    infom = Image.open(file)
    frames = infom.n_frames
    im8 = []
    for i in range(frames):
        infom.seek(i)  
        im8.append(ImageTk.PhotoImage(infom.copy())) 

    gif_label3 = Label(frame1, image="",bd=0)
    gif_label3.place(x=750,y=170)
    animation1(count)

def slider3():
    global count2,text2
    if count2>=len(txt2):
        count2=-1
        text2=''
        label2.config(text=text2)
    else:
        text2=text2+txt2[count2]
        label2.config(text=text2)
    count2+=1
    label2.after(100,slider3)

def on_enter1(event):
    event.widget.configure(bg="#898686")  

def on_leave1(event):
    event.widget.configure(bg="black")

def lgpage():
    frame2.destroy()

def various_color():
    colors = ["black","#1d3bff","red",]
    fg7 = random.choice(colors)
    qr_code.config(fg = fg7)
    qr_code.after(200,various_color)
    qr=["BeeBot"]
    text7 = random.choice(qr)
    qr_code.config(text=text7)

def selection():
    global frame2_bg
    global u_name
    global u_pass
    global txt2, count2, text2, label2

    u_name = p_name1.get()
    u_pass = p_password1.get()

    cursor = mydb.cursor()
    sql = "SELECT * FROM stafflogin WHERE Sid=%s AND Password=%s"
    adr = (u_name, u_pass)

    try:
        cursor.execute(sql, adr)
        myresult = cursor.fetchall()
    except Exception as e:
        tkinter.messagebox.showerror("BookBee", f"Database error: {e}")
        return

    if myresult:
        global frame2
        frame2 = Toplevel()
        frame2.geometry("1350x700+0+0")
        frame2.state("zoomed")
        frame2.title("BookBee")
        frame2.iconbitmap("C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\logo.ico")
        frame2.config(bg="white")

        def connect_to_db():
            try:
                conn = mysql.connector.connect(
                    host='localhost',  
                    database='library',  
                    user='root',  
                    password='9847709822' 
                )
                if conn.is_connected():
                    return conn
            except Error:
                return None

        def check_greetings_and_farewells(user_input):
            greetings = ["hi", "hello", "hey", "greetings"]
            farewells = ["bye", "goodbye", "see you", "take care","thanks","thank you"]

            if any(word in user_input.lower() for word in greetings):
                return "Hello! How can I assist you today?"
            elif any(word in user_input.lower() for word in farewells):
                return "Goodbye! Have a great day!"
            return None

        def execute_query(user_input):
            response = check_greetings_and_farewells(user_input)
            if response:
                return response

            conn = connect_to_db()
            if not conn:
                return "Unable to connect to the database. Please try again later."

            cursor = conn.cursor()
            response = ""

            user_input_cleaned = user_input.strip().lower()

            try:
                if "list all the available books" in user_input_cleaned or "available books" in user_input_cleaned:
                    query = "SELECT title FROM books WHERE status = 'available'"
                    cursor.execute(query)
                    available_books = cursor.fetchall()
                    if available_books:
                        response = "Available Books:\n" + "\n".join([book[0] for book in available_books])
                    else:
                        response = "No available books found."
                    return response

                elif "list all the issued books" in user_input_cleaned or "issued books" in user_input_cleaned:
                    query = "SELECT title FROM books WHERE status = 'issued'"
                    cursor.execute(query)
                    issued_books = cursor.fetchall()
                    if issued_books:
                        response = "Issued Books:\n" + "\n".join([book[0] for book in issued_books])
                    else:
                        response = "No issued books found."
                    return response
                
                elif "list the staff who have signed up" in user_input_cleaned or "staff signed up" in user_input_cleaned:
                    query = "SELECT Fname, Lname FROM staffsignup"
                    cursor.execute(query)
                    staff_members = cursor.fetchall()
                    if staff_members:
                        response = "Staff Members (Signed Up):\n" + "\n".join([f"{fname} {lname}" for fname, lname in staff_members])
                    else:
                        response = "No staff members found who have signed up."
                    return response

                elif "list the staff who have logged in" in user_input_cleaned or "staff logged in" in user_input_cleaned:
                    query = "SELECT Sid FROM stafflogin"
                    cursor.execute(query)
                    staff_logins = cursor.fetchall()
                    if staff_logins:
                        response = "Staff Members (Logged In):\n" + "\n".join([f"Staff ID: {sid[0]}" for sid in staff_logins])
                    else:
                        response = "No staff members found who have logged in."
                    return response

                elif "list the staff" in user_input_cleaned or "list all the staff" in user_input_cleaned or "staff members" in user_input_cleaned:
                    query = "SELECT Fname, Lname FROM staffsignup"
                    cursor.execute(query)
                    staff_members = cursor.fetchall()
                    if staff_members:
                        response = "Staff Members:\n" + "\n".join([f"{fname} {lname}" for fname, lname in staff_members])
                    else:
                        response = "No staff members found."
                    return response

                elif "list all the books" in user_input_cleaned or "all books" in user_input_cleaned:
                    query = "SELECT title FROM books"
                    cursor.execute(query)
                    all_books = cursor.fetchall()
                    if all_books:
                        response = "All Books:\n" + "\n".join([book[0] for book in all_books])
                    else:
                        response = "No books found in the library."
                    return response

                book_title = None
                if "is" in user_input_cleaned and "available" in user_input_cleaned:
                    book_title = user_input_cleaned.split("is")[1].split("available")[0].strip()

                elif "is" in user_input_cleaned and "issued" in user_input_cleaned:
                    book_title = user_input_cleaned.split("is")[1].split("issued")[0].strip()

                if book_title:
                    query = "SELECT status FROM books WHERE title = %s"
                    cursor.execute(query, (book_title,))
                    book_result = cursor.fetchone()

                    query = "SELECT issuedto FROM books_issued WHERE bid = (SELECT bid FROM books WHERE title = %s)"
                    cursor.execute(query, (book_title,))
                    issued_result = cursor.fetchone()

                    if "issued" in user_input_cleaned:
                        if issued_result:
                            response = f"The book '{book_title}' is issued to {issued_result[0]}."
                        else:
                            response = f"The book '{book_title}' is not issued."
                    elif "available" in user_input_cleaned:
                        if book_result:
                            if book_result[0] == "available":
                                response = f"The book '{book_title}' is available."
                            else:
                                response = f"The book '{book_title}' is not available."
                        else:
                            response = f"The book '{book_title}' is not available in our records."

                else:
                    response = "I'm sorry, I didn't understand that. Please ask about a book or staff."

            except Error as db_error:
                response = f"Error executing query: {db_error}"
            finally:
                cursor.close()
                conn.close()

            return response

        def chatbot_response():
            user_input = entry_box.get()
            chat_window.configure(state='normal')
            chat_window.insert(END, "You: " + user_input + "\n")
            response = execute_query(user_input)
            chat_window.insert(END, "Bot: " + response + "\n\n")
            chat_window.configure(state='disabled')
            entry_box.delete(0, END)


        def beebot():
            global entry_box
            global chat_window
            window = Tk()
            window.geometry("480x490+426+180")
            window.title("BeeBot")
            window.config(bg="#b5d2ed")
            window.iconbitmap("C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\bee.ico")
            chat_window = scrolledtext.ScrolledText(window, wrap=WORD)
            chat_window.pack(pady=10)
            chat_window.configure(state='disabled')
            entry_box = Entry(window, width=70)
            entry_box.pack(pady=10)
            send_button = Button(window, text="Send",font=("times new roman",13), command=chatbot_response,fg="white",bg="black",width=10)
            send_button.pack()
            send_button.bind("<Enter>", on_enter1)
            send_button.bind("<Leave>", on_leave1)
            window.mainloop()

        def default_home():
            global txt2, count2, text2, label2,qr_code
            f2=Frame(frame2,width=1400,height=800,bg="white")
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\welcome32.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.place(x=0, y=0)
            btn_logout1=Button(frame2,bg="black",fg="white",bd=2,text="Logout",font=("times new roman",13),command=lgpage)
            btn_logout1.place(x=1200,y=25,width=150)
            btn_logout1.bind("<Enter>", on_enter1)
            btn_logout1.bind("<Leave>", on_leave1)

            txt2 = "Welcome to the Hive!"
            count2 = 0
            text2 = ''
            label2 = Label(f2, text=txt2, font=("arial", 39, "bold"), fg="grey", bg="white")
            label2.place(x=210, y=80)
            slider3()

            qr_code= Label(f2, font=("arial",11,"bold"),bg="white")
            qr_code.place(x=1220,y=485)
            various_color()

            img_path = "C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\bee.png"
            img3 = ImageTk.PhotoImage(Image.open(img_path))
            button =Button(f2, image=img3, border=0,command=beebot)
            button.place(x=1200, y=510, width=110, height=120)
            button.image = img3
         
   
        def home():
            f1.destroy()
            default_home()
            toggle_win()

        def bookregister():
            global insert_stmt1
            global data2
            global cursor_reg1

            tname1=tname.get()
            aname1=aname.get()
            bid1=bid.get()
            bstatus1=bstatus.get()


            if tname1=='' or aname1=='' or bid1=='' or bstatus1=='':
                tkinter.messagebox.showinfo('BookBee',"Please fill the empty filed!")
            else:
                cursor_reg1= mydb.cursor()
                sql="SELECT * FROM books where bid=%s"
                adr1=(bid1,)
                cursor_reg1.execute(sql,adr1)
                myresult1 = cursor_reg1.fetchall()        
                if myresult1:
                    tkinter.messagebox.showinfo('BookBee','Book already registered!')
                else:
                    insert_stmt1 = (
                                   "INSERT INTO books(bid,title,author,status)"
                                   "VALUES (%s,%s,%s,%s)"
                                   )
                    data2 = (bid1,tname1,aname1,bstatus1)
                    cursor_reg1.execute(insert_stmt1,data2)

                    mydb.commit()
                    tkinter.messagebox.showinfo('BookBee','Successfully registered!')

                    bid.set('')
                    tname.set('')
                    aname.set('')
                    bstatus.set('')
                                   

        def addbooks():
            global bid
            global tname
            global aname
            global bstatus
            f1.destroy()
            f2=Frame(frame2,width=1400,height=800,bg='white')
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add1.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.pack()
     
            bid=StringVar()
            tname=StringVar()
            aname=StringVar()
            bstatus=StringVar()

            b_head=Label(f2, text="ADD BOOKS",font=("cooper black", 30, "bold"),fg="black",bg="white").place(x=557,y=80)
            
            b_id=Label(f2, text="BOOK ID",font=("league spartan", 11, "bold"),fg="black",bg="white").place(x=540,y=190)
            bid_entry=Entry(f2,textvariable=bid,font=("league spartan",13),bg="white").place(x=540,y=218,width=300,height=30)

            t_name=Label(f2, text="TITLE",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=265)
            tname_entry=Entry(f2,textvariable=tname,font=("league spartan",13),bg="white").place(x=540,y=293,width=300,height=30)

            a_name=Label(f2, text="AUTHOR",font=("league spartan", 11, "bold"),fg="black",bg="white").place(x=540,y=350)
            aname_entry=Entry(f2,textvariable=aname,font=("league spartan",13),bg="white").place(x=540,y=378,width=300,height=30)

            b_status=Label(f2, text="BOOK STATUS",font=("league spartan", 11, "bold"),fg="black",bg="white").place(x=540,y=443)
            monthchoosen = ttk.Combobox(f2, width=47, textvariable=bstatus,state="readonly")
            monthchoosen['values'] = ('available','issued')
            monthchoosen.current()
            monthchoosen.place(x=540,y=471)

            btn_submit=Button(f2,bg='#3c8aff',fg="black",bd=2,text="Submit",font=("times new roman",13),command=bookregister)
            btn_submit.place(x=615,y=533,width=150)
            btn_submit.bind("<Enter>", on_enter)
            btn_submit.bind("<Leave>", on_leave)            
            toggle_win()


        def viewbooks():
            global cur
            f1.destroy()
            f2=Frame(frame2,width=1400,height=800,bg='white')
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.pack()

            b_vhead=Label(f2, text="VIEW BOOKS",font=("cooper black", 30, "bold"),fg="black",bg="white").place(x=557,y=60)

            canvas = Canvas(f2, bg='black')
            canvas.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.5)

            labelFrame = Frame(canvas, bg='black')
            
            scrollbar = Scrollbar(f2, orient="vertical", command=canvas.yview)
            scrollbar.place(relx=0.79, rely=0.2, relheight=0.5)

            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.create_window((0, 0), window=labelFrame, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            labelFrame.bind("<Configure>", on_configure)

            Label(labelFrame, text="%-10s%-30s%-30s%-23s" % (' Bid', 'Title', 'Author', 'Status'),
                  bg='black', fg='white', font=("Courier New", 12, "bold")).pack(anchor="w")
            Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                  bg='black', fg='white').pack(anchor="w")

            y = 0.1  

            try:
                cur = mydb.cursor()
                getBooks = "SELECT * FROM books"
                cur.execute(getBooks)

                for i in cur:
                    Label(labelFrame, text="%-10s%-30s%-30s%-23s" % (i[0], i[1], i[2], i[3]),
                          bg='black', fg='white', font=("Courier New", 12, "bold")).pack(anchor="w")
                    y += 0.1
            except Exception as e:
                tkinter.messagebox.showinfo("BookBee","Failed to fetch files from database", str(e))
            toggle_win()

        def deleteBook():
            bdelete1=bdelete.get()
            btitle1=title1.get()
            baname1=aname1.get()

            if not bdelete1 or not btitle1 or not baname1:
                tkinter.messagebox.showinfo("BookBee", "Please fill the empty field!")
                return

            try:
                cur1 = mydb.cursor()
                deleteSql = "DELETE FROM books WHERE bid = %s"
                deleteIssue = "DELETE FROM books_issued WHERE bid = %s"                
                cur1.execute(deleteSql, (bdelete1,))
                cur1.execute(deleteIssue, (bdelete1,))                
                mydb.commit() 
                tkinter.messagebox.showinfo("BookBee", "Book Record Deleted Successfully!")
            except Exception as e:
                tkinter.messagebox.showerror("BookBee", f"Failed to delete record: {e}")
            finally:
                cur1.close()
                bdelete.set('')
                title1.set('')
                aname1.set('')


        def delete():
            global bdelete,title1,aname1
            f1.destroy()
            f2=Frame(frame2,width=1400,height=800,bg='white')
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add3.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.pack()

            bdelete=StringVar()
            title1=StringVar()
            aname1=StringVar()
                      
            b_dhead=Label(f2, text="DELETE BOOKS",font=("cooper black", 30, "bold"),fg="black",bg="white").place(x=520,y=100)

            b_delete=Label(f2, text="BOOK ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=255)
            bdelete_entry=Entry(f2,textvariable=bdelete,font=("league spartan",13),bg="white").place(x=540,y=278,width=300,height=30)

            t_name=Label(f2, text="TITLE",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=348)
            tname_entry=Entry(f2,textvariable=title1,font=("league spartan",13),bg="white").place(x=540,y=376,width=300,height=30)

            a_name=Label(f2, text="AUTHOR",font=("league spartan", 11, "bold"),fg="black",bg="white").place(x=540,y=443)
            aname_entry=Entry(f2,textvariable=aname1,font=("league spartan",13),bg="white").place(x=540,y=471,width=300,height=30)

            btn_submit1=Button(f2,bg='#3c8aff',fg="black",bd=2,text="Submit",font=("times new roman",13),command=deleteBook)
            btn_submit1.place(x=615,y=533,width=150)
            btn_submit1.bind("<Enter>", on_enter)
            btn_submit1.bind("<Leave>", on_leave)
           
            toggle_win()

        def validate_not_email(emailid1):
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            pattern=re.compile(regex)
            if pattern.match(emailid1):
                return True
            else:
                return False

        def sendmail(email_recipient):
            cursor5 = mydb.cursor()
            sql = "SELECT * FROM books_issued WHERE email_id=%s"
            adr = (email_recipient,)
            cursor5.execute(sql, adr)
            myresult3 = cursor5.fetchall()

            if not myresult3:
                tkinter.messagebox.showinfo("BookBee", "No user found with the given details.")
                cursor5.close() 
                return
            receiver_email = myresult3[0][2] 
            user_name = myresult3[0][1] 
            sender_email = "ADD YOUR MAIL ID"
            password = "ADD YOUR PASSWORD"
            
            message = f'''Subject: BookBee Confirmation

Hello {user_name}, 

Thank you for borrowing a book from our library! Please note that this book is due back in 20 days. We hope you enjoy reading, and remember to return it on time to avoid incurring a fine.

Happy reading!'''

            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                    tkinter.messagebox.showinfo("BookBee", "Email sent successfully!")
            except Exception as e:
                tkinter.messagebox.showinfo("Error", f"Failed to send email: {str(e)}")
            
            cursor5.close()


        def show_calendar(event):
            global cal
            global f3
            f3=Frame(frame2,bg="lightgrey")
            f3.place(x=565,y=180)
            cal = Calendar(f3, selectmode='day')
            cal.pack(pady=20)
            btn_confirm =Button(f3, bg="black",fg="white",bd=2,text="Confirm Date",font=("times new roman",11),command=lambda: confirm_date(cal, f3))
            btn_confirm.pack(pady=6)
            btn_confirm.bind("<Enter>", on_enter1)
            btn_confirm.bind("<Leave>", on_leave1)
            btn_out =Button(f3, bg="black",fg="white",bd=0,text="X",font=("times new roman",11,"bold"),command=f3.destroy)
            btn_out.place(x=222,y=3,height=15)
            btn_out.bind("<Enter>", on_enter1)
            btn_out.bind("<Leave>", on_leave1)

        def confirm_date(cal, f3):
            selected_date = cal.get_date()
            month, day, year = selected_date.split('/')
            formatted_date = f'{year}-{month}-{day}'
            brdate_entry.delete(0, END)
            brdate_entry.insert(0, formatted_date)
            f3.destroy()
                
        def issue():
            global cur3, status, check
            global emailid1
            issueid1 = issueid.get()
            issueto1 = issueto.get()
            emailid1=emailid.get()
            returndate1=returndate.get()
            check1=validate_not_email(emailid1)

            ISSUE_TABLE = "books_issued"
            BOOK_TABLE = "books"

            if not issueid1 or not issueto1 or not emailid1 or not returndate1:
                tkinter.messagebox.showinfo("BookBee", "Please fill the empty field!")
                return
            
            if not check1:
                tkinter.messagebox.showinfo('BookBee','Invalid email id!')
                return
            allBid = []

            try:
                with mydb.cursor() as cur3:
                    cur3.execute("SELECT bid FROM {}".format(BOOK_TABLE))
                    allBid = [i[0] for i in cur3]
                    if issueid1 not in allBid:
                        tkinter.messagebox.showinfo("BookBee", "Book ID not present!")
                        return
                    cur3.execute("SELECT status FROM {} WHERE bid = %s".format(BOOK_TABLE), (issueid1,))
                    check = cur3.fetchone()
                    status = (check[0] == 'available') if check else False

                    if status:
                        cur3.execute("INSERT INTO {} VALUES (%s,%s,%s,%s)".format(ISSUE_TABLE), (issueid1,issueto1,emailid1,returndate1))
                        cur3.execute("UPDATE {} SET status = 'issued' WHERE bid = %s".format(BOOK_TABLE), (issueid1,))
                        mydb.commit()
                        sendmail(emailid1)
                        tkinter.messagebox.showinfo("BookBee", "Book Issued Successfully!")
                    else:
                        tkinter.messagebox.showinfo("BookBee", "Book Already Issued!")

            except Exception as e:
                tkinter.messagebox.showinfo("BookBee", f"An error occurred: {str(e)}")
            allBid.clear()
            issueid.set('')
            issueto.set('')
            emailid.set('')
            returndate.set('')


        def issueBook():
            global issueid
            global issueto
            global emailid
            global returndate
            global brdate_entry
            f1.destroy()
            f2=Frame(frame2,width=1400,height=800,bg='white')
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add1.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.pack()

            issueid=StringVar()
            issueto=StringVar()
            emailid=StringVar()
            returndate=StringVar()

            b_ihead=Label(f2, text="ISSUE BOOKS",font=("cooper black", 30, "bold"),fg="black",bg="white").place(x=547,y=80)

            b_issueid=Label(f2, text="BOOK ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=190)
            bissueid_entry=Entry(f2,textvariable=issueid,font=("league spartan",13),bg="white").place(x=540,y=218,width=300,height=30)
               
            b_issueto=Label(f2, text="PATRON ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=265)
            bissueto_entry=Entry(f2,textvariable=issueto,font=("league spartan",13),bg="white").place(x=540,y=293,width=300,height=30)

            b_email=Label(f2, text="EMAIL ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=350)
            bemail_entry=Entry(f2,textvariable=emailid,font=("league spartan",13),bg="white").place(x=540,y=378,width=300,height=30)

            b_rdate=Label(f2, text="RETURN DATE",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=443)
            brdate_entry=Entry(f2,textvariable=returndate,font=("league spartan",13),bg="white")
            brdate_entry.place(x=540,y=471,width=300,height=30)
            brdate_entry.bind("<Button-1>", show_calendar)

            
            btn_submit2=Button(f2,bg='#3c8aff',fg="black",bd=2,text="Submit",font=("times new roman",13),command=issue)
            btn_submit2.place(x=615,y=533,width=150)
            btn_submit2.bind("<Enter>", on_enter)
            btn_submit2.bind("<Leave>", on_leave)

            toggle_win()


        def returnn():
            global cur5
            bdelete1 = bdelete.get()
            pid2 = pid1.get()
            ISSUE_TABLE = "books_issued"
            BOOK_TABLE = "books"
            allBid = []
            if not bdelete1 or not pid2:
                tkinter.messagebox.showinfo("BookBee", "Please fill the empty field!")
                return
            try:
                with mydb.cursor() as cur5:
                    cur5.execute("SELECT bid FROM {}".format(ISSUE_TABLE))
                    allBid = [i[0] for i in cur5]
                    if bdelete1 not in allBid:
                        tkinter.messagebox.showinfo("BookBee", "Book ID not present in issued books!")
                        return
                    cur5.execute("SELECT status FROM {} WHERE bid = %s".format(BOOK_TABLE), (bdelete1,))
                    check = cur5.fetchone()
                    if check and check[0] == 'issued':
                        cur5.execute("DELETE FROM {} WHERE bid = %s".format(ISSUE_TABLE), (bdelete1,))
                        cur5.execute("UPDATE {} SET status = 'available' WHERE bid = %s".format(BOOK_TABLE), (bdelete1,))
                        mydb.commit()
                        tkinter.messagebox.showinfo("BookBee", "Book Returned Successfully!")
                    else:
                        tkinter.messagebox.showinfo("BookBee", "Book status is not 'issued'!")

            except Exception as e:
                tkinter.messagebox.showinfo("BookBee", f"An error occurred: {str(e)}")

            allBid.clear()
            bdelete.set('')
            pid1.set('')

        def returnBook():
            global bdelete,pid1
            
            f1.destroy()
            f2=Frame(frame2,width=1400,height=800,bg='white')
            f2.place(x=0,y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add4.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg  
            bg7.pack()
            bdelete=StringVar()
            pid1=StringVar()

            b_rhead=Label(f2, text="RETURN BOOKS",font=("cooper black", 30, "bold"),fg="black",bg="white").place(x=510,y=110)

            b_deleteid=Label(f2, text="BOOK ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=275)
            bdeleteid_entry=Entry(f2,textvariable=bdelete,font=("league spartan",13),bg="white").place(x=540,y=298,width=300,height=30)

            b_retid=Label(f2, text="PATRON ID",font=("league spartan", 12, "bold"),fg="black",bg="white").place(x=540,y=368)
            bretid_entry=Entry(f2,textvariable=pid1,font=("league spartan",13),bg="white").place(x=540,y=396,width=300,height=30)

            btn_submit4=Button(f2,bg='#3c8aff',fg="black",bd=2,text="Submit",font=("times new roman",13),command=returnn)
            btn_submit4.place(x=615,y=470,width=150)
            btn_submit4.bind("<Enter>", on_enter)
            btn_submit4.bind("<Leave>", on_leave)

            toggle_win()


        def sendmail2():
            cursor5 = mydb.cursor()
            sql = "SELECT * FROM books_issued WHERE return_date = CURDATE() + INTERVAL 1 DAY"
            cursor5.execute(sql)
            myresult3 = cursor5.fetchall()
            if not myresult3:
                tkinter.messagebox.showinfo("BookBee", "No users have books due tomorrow!")
                cursor5.close() 
                return
            sender_email = "ADD YOUR MAILID"
            password = "ADD YOUR PASSWORD" 
            message_template = """Subject: BookBee Reminder
Hello {name},

This is a reminder that the borrowed book is due tomorrow. Late returns will incur fees, so please ensure it is returned on time.

Thank you!
        """

            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender_email, password)

                    for record in myresult3:
                        user_name = record[1]
                        receiver_email = record[2]
                        message = message_template.format(name=user_name)
                        server.sendmail(sender_email, receiver_email, message)
                    tkinter.messagebox.showinfo("BookBee", "Reminder emails sent successfully to all users!")
            except Exception as e:
                tkinter.messagebox.showinfo("Error", f"Failed to send email: {e}")

            cursor5.close()

        def notify():
            f1.destroy()
            f2 = Frame(frame2, width=1400, height=800, bg='white')
            f2.place(x=0, y=0)
            f2_bg = ImageTk.PhotoImage(file="C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\add.jpg")
            bg7 = Label(f2, image=f2_bg)
            bg7.image = f2_bg 
            bg7.pack(fill='both', expand=True)

            Label(f2, text="DEADLINE", font=("Cooper Black", 30, "bold"), fg="black", bg="white").place(x=560, y=60)

            canvas = Canvas(f2, bg='black')
            canvas.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.5)

            labelFrame = Frame(canvas, bg='black')
            scrollbar = Scrollbar(f2, orient="vertical", command=canvas.yview)
            scrollbar.place(relx=0.79, rely=0.2, relheight=0.5)

            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.create_window((0, 0), window=labelFrame, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            labelFrame.bind("<Configure>", on_configure)

            Label(labelFrame, text="%-30s%-30s%-30s" % ('Bid', 'Patron ID', 'Return Date'),
                  bg='black', fg='white', font=("Courier New", 12, "bold")).pack(anchor="w")
            Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
                  bg='black', fg='white').pack(anchor="w")

            btn_notify = Button(f2, bg="black", fg="white", bd=2, text="Notify", font=("aptos", 13, "bold"), command=sendmail2)
            btn_notify.place(x=610, y=600, width=150)

            try:
                cur = mydb.cursor()
                getBooks = "SELECT bid, issuedto, return_date FROM books_issued WHERE return_date = CURDATE() + INTERVAL 1 DAY"
                cur.execute(getBooks)

                for i in cur:
                    Label(labelFrame, text="%-30s%-30s%-30s" % (i[0], i[1], i[2]),
                          bg='black', fg='white', font=("Courier New", 12, "bold")).pack(anchor="w")
            except Exception as e:
                messagebox.showerror("BookBee", f"Failed to fetch records from the database: {str(e)}")
            finally:
                cur.close()

            toggle_win()


        def toggle_win():
            global f1
            f1=Frame(frame2,width=145,height=800,bg="#b5d2ed")
            f1.place(x=0,y=0)
            
        
            def bttn(x,y,text,bcolor,fcolor,cmd):
             
                def on_entera(e):
                    myButton1['background'] = bcolor 
                    myButton1['foreground']= '#262626'  

                def on_leavea(e):
                    myButton1['background'] = fcolor
                    myButton1['foreground']= '#262626'

                myButton1 = Button(f1,text=text,
                               width=20,
                               height=3,
                               fg="black",
                               border=0,
                               bg=fcolor,
                               activeforeground="black",
                               activebackground=bcolor,            
                                command=cmd)
                              
                myButton1.bind("<Enter>", on_entera)
                myButton1.bind("<Leave>", on_leavea)

                myButton1.place(x=x,y=y)

            bttn(0,80,'H O M E',"#95c4ef","#b5d2ed",home)
            bttn(0,132,'ADD BOOKS',"#95c4ef",'#b5d2ed',addbooks)
            bttn(0,184,'VIEW BOOKS',"#95c4ef","#b5d2ed",viewbooks)
            bttn(0,236,'DELETE BOOKS',"#95c4ef","#b5d2ed",delete)
            bttn(0,288,'ISSUE BOOKS',"#95c4ef","#b5d2ed",issueBook)
            bttn(0,340,'RETURN BOOKS',"#95c4ef","#b5d2ed",returnBook)
            bttn(0,392,'NOTIFY',"#95c4ef","#b5d2ed",notify)

            
            def dele():
                f1.destroy()
                b2=Button(frame2,image=img1,
                       command=toggle_win,
                       border=0,
                       bg='#262626',
                       activebackground='#262626')
                b2.place(x=5,y=8)

            global img2
            img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\close.png"))

            Button(f1,
                   image=img2,
                   border=0,
                   command=dele,
                   bg="#b5d2ed",
                   activebackground="#b5d2ed").place(x=5,y=10)
            

        default_home()

        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\EBIN P P\\OneDrive\\Desktop\\dbms\\open.png"))

        global b2
        b2=Button(frame2,image=img1,
               command=toggle_win,
               border=0,
               bg="black",
               activebackground="white",
               relief="flat")
        b2.place(x=5,y=8)
        p_name1.set('')
        p_password1.set('')

    else:
        tkinter.messagebox.showinfo('BookBee', 'Invalid Staff ID or Password!') 
       

mainscreen()




