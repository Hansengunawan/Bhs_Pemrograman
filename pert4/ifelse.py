#if else in python

def login():
    print("="*100)
    print("{:^100}".format("Silahkan Login"))
    print("="*100)
    user=input("Username : ")
    pw=input("Password : ")
    
    if user == "Hansen" and pw == "hansen":
        print("Login Berhasil")
    else:
        print("Coba Lagi")
login()
    
    

