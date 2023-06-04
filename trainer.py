from admin_panel import *
class trainer:
    def __init__(self):
        self.trainer=admin_panel()
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