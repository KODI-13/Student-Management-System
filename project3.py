#Student Details
#dictionary to store all student details
db = {}

#To print the school/collage name
print("-"*100)
print("\t\t\t\tStudent Management System")
print("-"*100) 

while True:            #To perform operations continuosly until we don't want to stop it
    #operations
    print("""
            \t\t\t\t1.Add
            \t\t\t\t2.Disply
            \t\t\t\t3.update
            \t\t\t\t4.Delete
            """)
    print("-"*100) 

    d = {}
    ch = int(input("Enter your choice : "))
    #To Add student details
    if ch == 1:
        #To add and check whether added roll number is in db or not
        while True:
            roll = int(input("Enter your roll number : "))
            if roll not in db:
                break
            else:
                print("The roll number is alreday present in db")
        name = input("Enter your name : ")
        city = input("Enter your city : ")
        #To check whether added mobile number is valid or invalid
        while True:
            mobile = int(input("Enter your mobile number : "))
            if len(str(mobile)) == 10:
                d["mobile"] = mobile
                break
            else:
                print("XXXXX Invalid mobile Number XXXXX")
                continue
        course = input("Enter your course : ") 
        #Storing each student details in private dictionary 
        d["name"] = name
        d["city"] = city       
        d["course"] = course
        ##Storing all student details(private dictionary) in one dictionary 
        db[roll] = d
    #To display student details
    elif ch == 2:
        print("-"*106)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("Roll no." , "Name" , "City" , "Mobile" , "Course"))
        print("-"*106)
        for roll in db:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(roll , db[roll]["name"] ,db[roll]["city"] , db[roll]["mobile"] , db[roll]["course"]))
            print("-"*106)
    #To update student details
    elif ch == 3:
        while True:
            roll = int(input("Enter your roll number : "))
            #Enter if loop when roll number is present in student dictionary ..i.e. roll in db
            if roll in db:
                while True:
                    print("""
                        \t\t\t\t| 1.name   |
                        \t\t\t\t| 2.city   |
                        \t\t\t\t| 3.mobile |
                        \t\t\t\t| 4.course |
                        """)
                    cho = int(input("Enter the field name which you wanna update : "))
                    #To update name
                    if cho == 1: 
                        un = input("Enter updated name : ")
                        db[roll]["name"] = un
                        print("Name of roll number",roll,"is updated successfully")
                        break
                    #To update city
                    elif cho == 2:
                        uc = input("Enter updated city : ")
                        db[roll]["city"] = uc
                        print("City of roll number",roll,"is updated successfully")
                        break
                    #To update mobile number
                    elif cho == 3:
                        #To check whether updated mobile number is valid or invalid
                        while True:
                            um = int(input("Enter updated mobile number : "))
                            if len(um) == 10 :
                                db[roll]["mobile"] = um
                                print("Mobile no. of roll number",roll,"is updated successfully")
                                break
                            else:
                                print("XXXXX Invalid mobile Number XXXXX")
                                continue
                    #To update course
                    elif cho == 4:
                        uco = input("Enter updated course : ")
                        db[roll]["course"] = uco
                        print("Course of roll number",roll,"is updated successfully")
                        break
                    #It enters when we give invalid choice number to update
                    else:
                        print("\n\n\t\t\t\t\t\tXXXXX Invaild Choise XXXXX")
                        print("\n\t\t\t\t\t\tXXXXX Try Again!! XXXXX")
                break
            #Enters when roll number is not present in student dictionary
            else:
                print("Roll number is not present in database")

    #To delete student details of given roll number from dictionary
    elif ch == 4: 
        roll = int(input("Enter your roll number : "))
        #we give if condition because it terminate the program when roll number is not present in dicionary.... but we have to continue the loop until we want
        if roll in db:
            del db[roll]
        else:
            print("Roll number is not present in database")
    #it enters when we give invalid choice number for operations
    else:
        print("Invalid choice") 

    #To break the while loop
    c = input("Do you want to continue (y/n) : ").lower()
    if c == "n":
        break
