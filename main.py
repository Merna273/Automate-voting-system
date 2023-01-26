import pymysql
from tkinter import *
passowordEntered = ""
#Main Page
root = Tk()
root.geometry("1000x700")
root.title("الانتخابات المصرية")
#Fonts
fontTuple1 = ("Times New Roman", 50, "bold")
fontTuple2 = ("Times New Roman", 30, "bold")
fontTuple3 = ("Times New Romn", 20)
def votingInfo():
   clearPage()
   con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
   try:
        with con.cursor() as cur:
         cur.execute('SELECT First_Name, Middle_Name, Last_Name, Vote_Count FROM Candidate')
        rows = cur.fetchall()
        c1 = StringVar()
        c2 = StringVar()
        c3 = StringVar()
        c1.set(rows[0])
        c1Label = Label(root, textvariable = c1, fg = "Black")
        c1Label.configure(font = fontTuple2)
        c1Label.place(anchor = "center",rely= 0.3, relx = 0.5) 
        c2.set(rows[1])
        c2Label = Label(root, textvariable = c2, fg = "Black")
        c2Label.configure(font = fontTuple2)
        c2Label.place(anchor = "center",rely= 0.5, relx = 0.5) 
        c3.set(rows[2])
        c3Label = Label(root, textvariable = c3, fg = "Black")
        c3Label.configure(font = fontTuple2)
        c3Label.place(anchor = "center",rely= 0.7, relx = 0.5) 
   finally: con.close() 
   root.after(5000, lambda:root.destroy()) 
def checkIfVoted():
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
    try:
        with con.cursor() as cur:
         cur.execute('SELECT National_ID, C_National_ID FROM Voter')
        rows = cur.fetchall()
        for i in rows:
          if(int(i[1]) == int(nationalIDEntered)):
             if(i[0] != None):
                votingAllowance = Label(root, text = "لقد انتخبت سابقاً، لا يمكنك الانتخاب مرة اخري", fg = "Red")
                votingAllowance.configure(font = fontTuple2)
                votingAllowance.place(anchor = "center",rely= 0.5, relx = 0.5)
                root.after(5000, lambda:root.destroy()) 
                return True
             else:
                return False
    finally: con.close()
def clearVotingPage():
    c1Label.destroy()
    c2Label.destroy()
    c3Label.destroy()
    votingButton1.destroy()
    votingButton2.destroy()
    votingButton3.destroy()
    voteLabel.destroy()
    confirmationLabel = Label(root, text = "تم الانتخاب بنجاح", fg = "Red")
    confirmationLabel.configure(font = fontTuple2)
    confirmationLabel.place(anchor = "center",rely= 0.5, relx = 0.5) 
    root.after(5000, lambda:root.destroy()) 
def vote1():
    votingButton1['state'] = 'disabled'
    votingButton2['state'] = 'disabled'
    votingButton3['state'] = 'disabled'
    print(nationalIDEntered)
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
    try:
        with con.cursor() as cur:
         cur.execute('UPDATE Candidate set Vote_Count = Vote_Count + 1  WHERE Last_Name = "Aly"')
         con.commit()
         sqlQuery = 'UPDATE Voter SET National_ID = "90012122345879" WHERE C_National_ID = %s'
         inputData = (nationalIDEntered)
         cur.execute(sqlQuery, inputData)
         con.commit()
         clearVotingPage()
    finally: con.close()
def vote2():
    votingButton1['state'] = 'disabled'
    votingButton2['state'] = 'disabled'
    votingButton3['state'] = 'disabled'
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
    try:
        with con.cursor() as cur:
         cur.execute('UPDATE Candidate set Vote_Count = Vote_Count + 1  WHERE Last_Name = "Youssed"')
         con.commit()
         sqlQuery = 'UPDATE Voter SET National_ID = "90018573913802" WHERE C_National_ID = %s'
         inputData = (nationalIDEntered)
         cur.execute(sqlQuery, inputData)
         con.commit()
         clearVotingPage()
    finally: con.close()
def vote3():
    votingButton1['state'] = 'disabled'
    votingButton2['state'] = 'disabled'
    votingButton3['state'] = 'disabled'
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
    try:
        with con.cursor() as cur:
         cur.execute('UPDATE Candidate set Vote_Count = Vote_Count + 1  WHERE Last_Name = "Mabrouk"')
         con.commit()
         sqlQuery = 'UPDATE Voter SET National_ID = "90019411201435" WHERE C_National_ID = %s'
         inputData = (nationalIDEntered)
         cur.execute(sqlQuery, inputData)
         con.commit()
         clearVotingPage()
    finally: con.close()
def clearPage():
    integrityLabel.destroy()
    myLabel1.destroy()
    nationalID.destroy() 
    nationalIDLabel.destroy()
    password.destroy()
    passwordLabel.destroy() 
    submitButton.destroy()
    minFrame.destroy()
    myLabel.destroy()
    resultButton.destroy()
    userQuestion.destroy()
    userQuestionLabel.destroy()
    userQuestionButton.destroy()
    nID.destroy()
    nIDLabel.destroy()
def click():
    global nationalIDEntered 
    nationalIDEntered = nationalID.get()
    passowordEntered = password.get()
    con = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'merna2732',
        db = 'automated_voting_system'
        )
    try:
        with con.cursor() as cur:
         cur.execute('SELECT * FROM Log_In')

        rows = cur.fetchall()

        existInDatabase = False
        for i in rows:
            if int(i[0]) == int(nationalIDEntered):
                if (i[1] == passowordEntered):
                    existInDatabase = True
                    clearPage()
                    voted = checkIfVoted()
                    if voted == False:
                        with con.cursor() as cur:
                         cur.execute('SELECT First_Name, Middle_Name, Last_Name, Description FROM Candidate')
                        rows = cur.fetchall()
                        print(rows[0])
                        c1 = StringVar()
                        c2 = StringVar()
                        c3 = StringVar()
                        global votingButton1
                        global votingButton2
                        global votingButton3 
                        global c1Label
                        global c2Label
                        global c3Label
                        global voteLabel
                        voteLabel = Label(root, text = "برجاء اختيار من ستنتخبه", fg = "red")
                        voteLabel.configure(font = fontTuple1)
                        voteLabel.place(anchor = "center",rely= 0.1, relx = 0.5) 
                        c1.set(rows[0])
                        c1Label = Label(root, textvariable = c1, fg = "Black")
                        c1Label.configure(font = fontTuple2)
                        c1Label.place(anchor = "center",rely= 0.3, relx = 0.5) 
                        votingButton1 = Button(root, text = "اختيار", command = vote1)
                        votingButton1.place(anchor = "center", rely = 0.4, relx = 0.5)
                        c2.set(rows[1])
                        c2Label = Label(root, textvariable = c2, fg = "Black")
                        c2Label.configure(font = fontTuple2)
                        c2Label.place(anchor = "center",rely= 0.5, relx = 0.5) 
                        votingButton2 = Button(root, text = "اختيار", command = vote2)
                        votingButton2.place(anchor = "center", rely = 0.6, relx = 0.5) 
                        c3.set(rows[2])
                        c3Label = Label(root, textvariable = c3, fg = "Black")
                        c3Label.configure(font = fontTuple2)
                        c3Label.place(anchor = "center",rely= 0.7, relx = 0.5) 
                        votingButton3 = Button(root, text = "اختيار", command = vote3)
                        votingButton3.place(anchor = "center", rely = 0.8, relx = 0.5)
                        root.after(300000, lambda:root.destroy()) 
                        break

        if not(existInDatabase):
            repeatLabel =  Label(root, text = "بياناتك غير صحيحة يرجي اعادة المحاولة", fg = "Black", bg = "orange")
            repeatLabel.configure(font = fontTuple2)
            repeatLabel.place(anchor = "center",rely= 0.6, relx = 0.5) 
            root.after(1500, repeatLabel.destroy)
    finally:
        con.close()
def callBack(input):
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        entryWrong = Label(root, text = "برجاء ادخال ارقام فقط", fg = "orange")
        entryWrong.configure(font = fontTuple2)
        entryWrong.place(anchor = "center",rely= 0.65, relx = 0.5)
        root.after(1500, entryWrong.destroy)
        return False
def acceptingMessage():
    if(nID.get() != "" and userQuestion.get() != ""):
        userQuestion['state'] = 'disabled'
        nID['state'] = 'disabled'
        userQuestionButton.destroy()
        messageLabel = Label(root, text = "تم ارسال رآيك", fg = "black")
        messageLabel.configure(font = fontTuple3)
        messageLabel.place(anchor = "center",rely= 0.95, relx = 0.1) 
        root.after(1500, messageLabel.destroy)
    elif(nID.get() == "" and userQuestion.get() == ""):
        errorLabel1 = Label(root, text = "برجاء كتابة الرقم القومي", fg = "black", bg = "orange")
        errorLabel1.place(anchor = "center", rely = 0.9, relx = 0.3)
        errorLabel1.configure(font = fontTuple3) 
        root.after(1500, errorLabel1.destroy)
        errorLabel2 = Label(root, text = "برجاء كتابة رآيك", fg = "black", bg = "orange")
        errorLabel2.place(anchor = "center", rely = 0.9, relx = 0.7)
        errorLabel2.configure(font = fontTuple3) 
        root.after(1500, errorLabel2.destroy)
    elif(nID.get() == ""):
        errorLabel = Label(root, text = "برجاء كتابة الرقم القومي", fg = "black", bg = "orange")
        errorLabel.place(anchor = "center", rely = 0.9, relx = 0.3)
        errorLabel.configure(font = fontTuple3) 
        root.after(1500, errorLabel.destroy)
    elif(userQuestion.get() == ""):
        errorLabel = Label(root, text = "برجاء كتابة رآيك", fg = "black", bg = "orange")
        errorLabel.place(anchor = "center", rely = 0.9, relx = 0.7)
        errorLabel.configure(font = fontTuple3) 
        root.after(1500, errorLabel.destroy)
    

        
#Add ministry photo
minFrame = Frame(root)
minFrame.pack()
minFrame.place(anchor = 'nw', relx = 0.2, rely = 0.1)
ministry = PhotoImage(file = "/Users/mernaabdelbadie/Downloads/a569f7d6-4ae8-468e-9f3c-f23fadb84cd9.png")
ministryLabel = Label(minFrame, image = ministry)
ministryLabel.pack()
#create the text
myLabel = Label(root, text = "مرحباً بكم في خدمة الانتخابات المصرية الالكترونية")
myLabel.configure(font = fontTuple1)
#putting it on the screen
myLabel.pack()
#create the text
myLabel1 = Label(root, text = "برجاء تسخيل الدخول للتمكن من الانتخاب", fg = "red")
myLabel1.configure(font = fontTuple2)
myLabel1.place(anchor = "center",rely= 0.6, relx = 0.5)
#logging in
nationalID = Entry(root, width = 20, bg = "white")
nationalIDEntered = nationalID.get()
nationalID.place(anchor = "center", rely = 0.7, relx = 0.45)
#validate the entry is numbers
reg = root.register(callBack)
nationalID.config(validate = "key", validatecommand = (reg,'%P'))
nationalIDLabel = Label(root, text = "الرقم القومي:", fg = "black")
nationalIDLabel.place(anchor = "center", rely = 0.7, relx = 0.6)
nationalIDLabel.configure(font =fontTuple3)
#password
password = Entry(root, width = 20, bg = "white")
password.place(anchor = "center", rely = 0.75, relx = 0.45)
passwordLabel = Label(root, text = "الرقم السري:", fg = "black")
passwordLabel.place(anchor = "center", rely = 0.75, relx = 0.6)
passwordLabel.configure(font = fontTuple3)
#Integrity statement
integrityLabel = Label(root, text = "بضغطك علي زر الدخول فأنت تؤكد ان المعلومات المدخلة هي معلوماتك و ليست معلومات شخص اخر", fg = "red")
integrityLabel.place(anchor = "center", rely = 0.8, relx = 0.5)
integrityLabel.configure(font = fontTuple3)
#submitting and saving the national ID and password
submitButton = Button(root, text = "دخول", command = click)
submitButton.place(anchor = "center", rely = 0.85, relx = 0.5)
resultButton = Button(root, text = "احصائيات التصويت", command = votingInfo)
resultButton.place(anchor = "center", rely = 0.9, relx = 0.5) 
userQuestion = Entry(root, width = 30, bg = "white")
userQuestion.place(anchor = "center", rely = 0.95, relx = 0.6)
nID = Entry(root, width = 15, bg = "white")
nID.place(anchor = "center", rely = 0.95, relx = 0.25)
reg = root.register(callBack)
nID.config(validate = "key", validatecommand = (reg,'%P'))
userQuestionLabel = Label(root, text = "رآيك يهمنا:", fg = "black")
userQuestionLabel.place(anchor = "center", rely = 0.95, relx = 0.8)
userQuestionLabel.configure(font = fontTuple3) 
nIDLabel = Label(root, text = "الرقم القومي:", fg = "black")
nIDLabel.place(anchor = "center", rely = 0.95, relx = 0.38)
nIDLabel.configure(font = fontTuple3) 
userQuestionButton = Button(root, text = "ارسال", command = acceptingMessage)
userQuestionButton.place(anchor = "center", rely = 0.95, relx = 0.1)  
#loop the application
root.mainloop()