#student_list=[]
#def add_student():
       # student_size=int(input("Enter the number of students to add:"))
       # for i in range(1,student_size+1):
         #   print(f"Enter the number of student{i}:")
          #  name=input("Enter the name of Student:")
           # gender=input("Enter the gender:")
          #  mobile=(input("Enter the mobile number of student:"))
          #  experience=(input("Enter the experience in years:"))
         #   qualification=input("Enter the qualification details:")
        #    email=input("Enter the e-mail id of student:")
       #     password=input("Enter the password")
      #      student_data ={"name":name,"gender":gender,"mobile":mobile,
     #       "experience":experience,"qualification":qualification,
    #        "email":email,
   #         "password":password
  #          }
 #           student_list.append(student_data)
#        return student_list
#print(add_student())
#print(add_student())

# def add_module(self,module_name,duration):
    #    topic_list=[]
    #    key =random.randint(1.100)
    #    topic_size=int(input("enter the number of topics that you want to add:"))
    #    for i in range(topic_size):
    #       topic=input(f"Enter topic name{i}:")
    #       topic_list.append(topic)
    #    module_data={"Module Name":module_name,
    #                 "Duration":duration,
    #                 "Topic":topic_list}
     #   self.module_details[key]=module_data
     #   return self.module_details

import random
import json
class admin_panel:
    student_list=[]
    def __init__(self):
        self.module_details={}
        self.trainer_details={}
        self.batch_details={}
        self.student_details={}
    def admin_login(self,username,password):
        if username=="admin" and password=="1234":
            return True
        return False
    def add_module(self,module_name,duration):
        topic_list= []
        key=random.randint(1,100)
        topic_size=int(input("enter the number of topics that you want to add:"))
        for i in range(topic_size):          
            topic=input(f"Enter topic name{i}:")
            topic_list.append(topic)
            module_data={"Module_Name":module_name,
                         "Duration":duration,
                        "Topic":topic_list
                    }
        self.module_details[key]=module_data
        with open("add_module.json","w") as f:
            json.dump(self.module_details,f)
        return self.module_details
   
    def add_trainer(self):
        trainer_id=random.randint(1,100)
        name=input("Enter the name of trainer:")
        gender=input("Enter the gender:")
        mobile=int(input("Enter the mobile number of trainer:"))
        experience=int(input("Enter the experience in years:"))
        qualification=input("Enter the qualification details:")
        email=input("Enter the e-mail id of trainer:")
        password=input("Enter the password")
        trainer_data={"trainer_id":trainer_id,"name":name,"gender":gender,"mobile":mobile,
                        "experience":experience,"qualification":qualification,
                        "email":email,
                        "password":password
                    }
        self.trainer_details[trainer_id]=trainer_data
        with open("add_trainer.json","w") as f:
            json.dump(self.trainer_details,f)
        return self.trainer_details
    
    def add_batch(self,module,trainer,student):
        key=random.randint(1,100)
        batch_data={ "module":module,
                     "trainer":trainer,
                     "student":student  
                    }
        self.batch_details[key]=batch_data
        with open("add_batch.json","w") as f:
            json.dump(self.batch_details,f)
        return self.batch_details
   
    def add_student(self):
        key=random.randint(1,100)
        student_size=int(input("Enter the number of students to add:"))
        for i in range(1,student_size+1):
            print(f"Enter the number of student(i):")
            name=input("Enter the name of trainer:")
            gender=input("Enter the gender:")
            mobile=int(input("Enter the mobile number of trainer:"))
            experience=int(input("Enter the experience in years:"))
            qualification=input("Enter the qualification details:")
            email=input("Enter the e-mail id of trainer:")
            password=input("Enter the password")
            student_data ={"name":name,"gender":gender,"mobile":mobile,
            "experience":experience,"qualification":qualification,
            "email":email,
            "password":password
            }
            admin_panel.student_list.append(student_data)
            self.student_details[key]=admin_panel.student_list
            with open("add_student.json","w") as f:
                json.dump(self.student_details,f)
            return self.student_details
x=admin_panel()
print("First batch :",x.add_batch("Python","Prathyush","Krishna"))
print("Second batch :",x.add_batch("DSA","Prathyush","Krishna"))
print("-"*100)
print("First batch :",x.add_module("Python","8 weeks"))
print("Second batch :",x.add_module("DSA","1 week"))
print("-"*100)
print("First batch :",x.add_trainer())
print("Second batch :",x.add_trainer())
print("-"*100)
print("First batch :",x.add_student())
print("Second batch :",x.add_student())
print("-"*100)


        



