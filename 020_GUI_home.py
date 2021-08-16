from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('ID check')
root.geometry('700x400')
root.iconbitmap('ID_logo.gif')

image1 = PhotoImage(file='ID_logo.png')
myLabel = Label(root, image=image1)
myLabel.place(x=10, y=20)


dataFrame = LabelFrame(root, text='Please enter ID: ', padx=20, pady=20 )
dataFrame.place(x=180, y=20)

dataFrame2 = LabelFrame(root, borderwidth=0)
dataFrame2.place(x=180, y=180)

var = IntVar()

def onclick(chk1):
    Label(root, text=var.get()).pack()


chk1 = Checkbutton(dataFrame, text='Include ID validation', variable=var)
chk1.grid(row=0, column=2)


user_entry = Entry(dataFrame, width=20, bg='white', fg='black', borderwidth=1)
user_entry.insert(0, int())
user_entry.grid(row=0, column=1)


def onclick():
    idcode = user_entry.get()
    if len(idcode) == 11:
        Label(dataFrame2, text='You ID: ' + idcode).grid(row=0, sticky=W)
    else:
        messagebox.showerror(title='Error', message='Incorrect entry!')

    if int(idcode[0]) % 2 == 1:
        Label(dataFrame2, text='Gender: Male').grid(row=1, sticky=W)
    else:
        Label(dataFrame2, text='Gender: Female').grid(row=1, sticky=W)

    if idcode[0] in ('1', '2'):
        birth_year = '18'
    elif idcode[0] in ('3', '4'):
        birth_year = '19'
    elif idcode[0] in ('5', '6'):
        birth_year = '20'

    if int(idcode[7:10]) > 0 and int(idcode[7:10]) <= 10:
        region = 'Kuressaare haigla'
    elif int(idcode[7:10]) >= 11 and int(idcode[7:10]) <= 19:
        region = 'Tartu Ülikooli Naistekliinik'
    elif int(idcode[7:10]) >= 21 and int(idcode[7:10]) <= 150:
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(idcode[7:10]) >= 151 and int(idcode[7:10]) <= 160:
        region = 'Keila haigla'
    elif int(idcode[7:10]) >= 161 and int(idcode[7:10]) <= 220:
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(idcode[7:10]) >= 221 and int(idcode[7:10]) <= 270:
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(idcode[7:10]) >= 271 and int(idcode[7:10]) <= 370:
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(idcode[7:10]) >= 371 and int(idcode[7:10]) <= 420:
        region = 'Narva haigla'
    elif int(idcode[7:10]) >= 421 and int(idcode[7:10]) <= 470:
        region = 'Pärnu haigla'
    elif int(idcode[7:10]) >= 471 and int(idcode[7:10]) <= 490:
        region = 'Haapsalu haigla'
    elif int(idcode[7:10]) >= 491 and int(idcode[7:10]) <= 520:
        region = 'Järvamaa haigla (Paide)'
    elif int(idcode[7:10]) >= 521 and int(idcode[7:10]) <= 570:
        region = 'Rakvere haigla, Tapa haigla'
    elif int(idcode[7:10]) >= 571 and int(idcode[7:10]) <= 600:
        region = 'Valga haigla'
    elif int(idcode[7:10]) >= 601 and int(idcode[7:10]) <= 650:
        region = 'Viljandi haigla'
    elif int(idcode[7:10]) >= 651 and int(idcode[7:10]) <= 700:
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

    Label(dataFrame2, text='Date of birth: ' + idcode[5] + idcode[6] + '.' + idcode[3] + idcode[4] + '.' + birth_year + idcode[1] + idcode[2]).grid(row=2, sticky=W)
    Label(dataFrame2, text='Place of birth: ' + region).grid(row=3, sticky=W)


my_button = Button(root, text='Check ID', fg='black', bg='grey', padx=10, pady=10, command=onclick)
my_button.place(x=180, y=120)



root.mainloop()