import sys
from admin_panel import*
admin=admin_panel()
while True:
    print("press 1 for admin login :")
    print("press 2 for trainer login :")
    print("press 3 for student login :")
    print("press 4 for exit")
    print("-"*100)
    choice=int(input("enter the choice for login: "))
    if choice==1:
        print("****************************adminlogin**********************")
        username=input("enter the username: ")
        password=input("enter the password: ")
        temp=admin.admin_login(username,password)
        if temp:
            print("*********************welcome to adminpanel*************************")
            print("press 1 for add module")
            print("press 2 for add trainer")
            print("press 3 for add batch")
            print("press 4 for add student")
            print("press 5 for add remove module")
            print("press 6 for add update tainer")
            print("press 7 for add trainer details")
            print("press 8 for add sudents details")
            print("press 9 for add modules details")
            print("press 10 for add batch details")
            print("-"*100)
            option=int(input("enter the option: "))
            print("-"*100)
            if(option==1):
                module_name=input("enter the module which want to change: ")
                duration=input("enter the duration to change: ")
                admin.add_module(module_name,duration)
                print("module added successfully...")
                print("-"*100)
            elif option==2:
                admin.add_trainer()
                print("trainer added successfully...")
                print("-"*100)
            elif option==3:
                module=input("enter the module to add: ")
                trainer=input("enter the trainer to add: ")
                student=input("enter the student to add: ")
                admin.add_batch(module,trainer,student)
                print("batch has been added successfully")
                print("-"*100)
            elif option==4:
                admin.add_student()
                print("student added successfully...")
                print("-"*100)
            elif option==5:
                admin.remove_module()
                print("module removed successfully..")
                print("-"*100)
            elif option==6:
                admin.update_trainer()
                print("trainer updated successfully..")
                print("-"*100)
            elif option==7:
                admin.Read_trainer()
                print("-"*100)
            elif option==8:
                admin.Read_student()
                print("-"*100)
            elif option==9:
                admin.Read_module()
                print("-"*100)
            elif option==10:
                admin.Read_batch()
                print("-"*100)
        else:
            print("please enter a valid input")
            print("-"*100)
        if choice==2:
            print("**************welcome to student panel******************")
            print("press 1 for add sudents details")
            print("press 2 for add modules details")
            print("press 3 for add batch details")
            print("-"*100)
            if option==1:
                admin.Read_student()
                print("-"*100)
            elif option==2:
                admin.Read_module()
                print("-"*100)
            elif option==3:
                admin.Read_batch()
                print("-"*100)
        else:
            print("please enter a valid input")
            print("-"*100)
        if choice==3:
            print("*********************welcome to trainer panel*************************")
            print("press 1 for add trainer details")
            print("press 2 for add sudents details")
            print("press 3 for add modules details")
            print("press 4 for add batch details")
            if option==1:
                admin.Read_trainer()
                print("-"*100)
            elif option==2:
                admin.Read_student()
                print("-"*100)
            elif option==3:
                admin.Read_module()
                print("-"*100)
            elif option==4:
                admin.Read_batch()
                print("-"*100)
        else:
            print("please enter a valid input")
            print("-"*100)
        if choice==4:
            print("thank you for visiting")
            sys.exit()
        else:
            print("please enter a valid input")



                
            
            


                

            
         












