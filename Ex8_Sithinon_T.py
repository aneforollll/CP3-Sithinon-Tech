username = input("Username :")
password = input("Password :")
if username == "admin" and password == "1234":
    print("Welcome")
    print("1:Iphone;price 1000")
    print("2:Ipad; price 5000")
    product = int(input("choose your product:"))
    quantity = int(input("How many?: "))
    if product == 1:
        print("total: " , quantity*1000)
    elif product == 2:
        print("total: " , quantity*5000)