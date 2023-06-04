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
        key=random.randint(1,100000)
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
        trainer_id=random.randint(1,100000)
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
        key=random.randint(1,100000)
        batch_data={ "module":module,
                     "trainer":trainer,
                     "student":student  
                    }
        self.batch_details[key]=batch_data
        with open("add_batch.json","w") as f:
            json.dump(self.batch_details,f)
        return self.batch_details
   
    def add_student(self):
        key=random.randint(1,100000)
        student_size=int(input("Enter the number of students to add:"))
        for i in range(1,student_size+1):
            print(f"Enter the number of student(i):")
            name=input("Enter the name of student:")
            gender=input("Enter the gender of student:")
            mobile=int(input("Enter the mobile number of student:"))
            experience=int(input("Enter the experience in years:"))
            qualification=input("Enter the qualification details:")
            email=input("Enter the e-mail id of student:")
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
    def remove_module(self):
        with open("add_module.json","r") as f:
            content1=json.load(f)
        print(content1)
        print("content modules on the portal is: ")
        for k,v in content1.items():
            print(f"module id :{k}  data :{v}")
        module_key=str(input("enter the module id want to delete : "))
        del content1[module_key]
        print("module has been deleted sucessfully...")
        for k,v in content1.items():
            print(f"module id :{k}  data :{v}")
        with open("add_module.json","w") as f:
            json.dump(content1,f)
    def update_trainer(self):
        with open("add_trainer.json","r") as f:
            content1=json.load(f)
        print(content1)
        print("trainer details on the portal is: ")
        for k,v in content1.items():
            print(f"trainer_id :{k}  trainer_details :{v}")
        trainer_id=str(input("enter the trainer id want to delete : "))
        trainer_edit=input("enter which field you want to edit: ")
        trainer_updated_value=input("Enter the updated value: ")
        content1[trainer_id][trainer_edit]=trainer_updated_value
        print("trainer detail is updated successfully....")
        for k,v in content1.items():
            print(f"trainer_id :{k}  trainer_details :{v}")
        with open("add_trainer.json","w") as f:
            content1=json.load(f)
        print(content1)
    def Read_student(self):
        with open("add_student.json","r") as f:
            content1=json.load(f)
        print("student details on the portal is: ")
        for k,v in content1.items():
            print(f"batch_id :{k}  student_data :{v}")
    def Read_trainer(self):
        with open("add_trainer.json","r") as f:
            content1=json.load(f)
        print("trainer details on the portal is: ")
        for k,v in content1.items():
            print(f"trainer_id :{k}  trainer_data :{v}")
    def Read_batch(self):
        with open("add_batch.json","r") as f:
            content1=json.load(f)
        print("batch details on the portal is: ")
        for k,v in content1.items():
            print(f"batch_id :{k}  batch_data :{v}")
    def Read_module(self):
        with open("add_module.json","r") as f:
            content1=json.load(f)
        print("module details on the portal is: ")
        for k,v in content1.items():
            print(f"module_id :{k}  module_data :{v}")







x=admin_panel()
#print("First batch :",x.add_batch("Python","Prathyush","Krishna"))
#print("Second batch :",x.add_batch("DSA","Prathyush","Krishna"))
#print("-"*100)
#print("First batch :",x.add_module("Python","8 weeks"))
#print("Second batch :",x.add_module("DSA","1 week"))
#print("-"*100)
#print("First batch :",x.add_trainer())
#print("Second batch :",x.add_trainer())
#print("-"*100)
#print("First batch :",x.add_student())
#print("Second batch :",x.add_student())
#print("-"*100)
#x.remove_module()
#x.update_trainer()
x.Read_student()
#x.Read_trainer()
x.Read_batch()
x.Read_module()




        


