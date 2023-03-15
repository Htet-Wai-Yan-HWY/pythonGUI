from tkinter import *
import tkinter.messagebox as msg




def main():
    app = Tk()
    app.wm_title('Data collection form')
    app.wm_geometry('450x400')

    global name_entry
    global age_entry
    global email_entry
    global address_entry
    global phone_no_entry
    global city_entry

    name_entry = Entry(app, width=50)
    age_entry = Entry(app, width=50)
    email_entry = Entry(app, width=50)
    address_entry = Entry(app, width=30)
    phone_no_entry = Entry(app, width=50)
    city_entry = Entry(app, width=15)


    Label(app, text='Enter your name').place(x=20, y=30)
    Label(app, text='Enter your age').place(x=20, y=90)
    Label(app, text="Enter your email").place(x=20, y=150)
    Label(app, text="Enter your address").place(x=20, y=210)
    Label(app, text="Enter your city").place(x=300, y=210)

    Label(app, text="Enter your phone number").place(x=20, y=270)

    name_entry.place(x=20, y=60)
    age_entry.place(x=20, y=120)
    email_entry.place(x=20 ,y=180)
    address_entry.place(x=20 ,y=240)    
    city_entry.place(x=300 ,y=240)

    phone_no_entry.place(x=20 ,y=300)

    Button(app, text='Register', bg='green', fg='white', command=register_user).place(x=350, y=350)
    Button(app, text="Quit", bg="red",fg="white", command=lambda:app.quit()).place(x=20 , y=350)



    app.mainloop()


def age_error():
    msg.showerror(title='Invalid age',
                  message='Please enter a valid age')
    
def email_error():
    msg.showerror(title="Invalid email",
                  message="Please enter a valid email")
    
def check_email(string):
    if "@"in string:
        return True
    else:
        return False
def check_phone(string):
    if "+95"in string():
        return True
    else:
        return False




def register_user():

    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    phone_no = phone_no_entry.get()

    if name.strip()=="":
        msg.showerror(title='No name entered', message='Please enter your name')
    elif age.strip()=="":
        msg.showerror(title='No age entered',
                      message='Please enter your age')
    elif (not age.isnumeric()):
        age_error()
    elif int(age)>100 or int(age)<0:
        age_error()
    elif email.strip()=="":
        msg.showerror(title="No email entered",
                      message="Please enter your email")
    elif not check_email(email):
        msg.showerror(title="Wrong format email entered",
                      message="Please enter valid email")
        
    elif phone_no.strip()=="":
        msg.showerror(title="No phone number entered",
                      message="Please enter your phone number")

        
    elif not check_phone(phone_no):
        msg.showerror(title="Invalid phone number",
                      message="Please enter local phone number")

    else:
        with open(f'/home/zyme/users/_{name}_.txt', 'w') as text_file:
            text_file.write(f"Name : {name}\nAge : {age}\nemail :{email}\naddress:{address} city:{city}\nphone number:{phone_no}")
            msg.showinfo('Registration success!', message='Your information have been registered successfully')


    
if __name__ == "__main__":

     main()
