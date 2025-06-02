import sqlite3
conn=sqlite3.connect('usad.db')
cur=conn.cursor()

def menu():
    print("Welcome to Airline Management")
    print("---------------------------------------------")
    print("1. Log in")
    print("2. Sign up")
    print("3. Exit Airlines")
    print("---------------------------------------------")

admin_emails=["arunsan2012@gmail.com","arunsan.v@tcs.com"]

cur.execute('''create table if not exists user(
        name text not null,
        idn integer not null,
        email text not null unique)
''')

def admin():
    print("---------------------------------------------")
    print("1. Carrier management ")
    print("2. Flight management ")
    print("3. User Management ")
    print("3. booking management ")
    print("4. Return to menu")
    print("---------------------------------------------")

def usser():
    print("---------------------------------------------")
    print("1. View Flights ")
    print("2. Book Flights ")
    print("3. Cancel Booking ")
    print("4. Return to menu")
    print("---------------------------------------------")

def log_in():
    idn=int(input("Enter ur id:"))
    email=input("Enter ur email:")
    cur.execute('Select * from user where idn=? and email=?',(idn,email))
    user=cur.fetchone()
    if user:
        if email in admin_emails:
            print("admin")
            admin()
        else:
            print("user")
            usser()
            
    else:
        print("Log in invalid")
    

def sign_up():
    try:
        name=input("Enter ur name:")
        idn=int(input("Enter the id :"))
        mail=input("Enter ur mail:")
        cur.execute(''' Insert into user(name,idn,email) values(?,?,?)''',(name,idn,mail))
        conn.commit()
        print("user created")
        print("---------------------------------------------")
    except Exception as e:
        print("Invalid user/credentials :",e)
        print("---------------------------------------------")

while True:
    menu()
    choice = int(input())
    if choice==1:
        log_in()
    elif choice==2:
        sign_up()
    else:
        print("Invalid choice")
        conn.close()
        break
