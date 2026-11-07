import json

tasks = []

class Storage:
    @staticmethod
    def save_tasks():
        with open("tasks.json","w") as file:
            json.dump(tasks,file,indent=4)
            return

    @staticmethod
    def load_tasks():
        try:
            with open("tasks.json","r") as file:
                 return (json.load(file))
        except FileNotFoundError:
            print("File Doesnot Exist!!")
            return []
            

tasks=Storage.load_tasks()

class Manage:
    
    @staticmethod
    def add_tasks():
        a = input("\nTask: ").strip()
        if not a:
            print("Task Cannnot be Empty!!")
            return
        tasks.append({"Task": a, "Completed": False})
        print("Task Added Successfully")
        Storage.save_tasks()
    
    @staticmethod
    def view_tasks():
        if not tasks:
            print("\nThere are no Tasks!")
            return
        
        for index, t in enumerate(tasks, start=1):
            status = "✓ Done" if t["Completed"] else "✗ Pending"
            print(f"{index}. {t['Task']} [{status}]")


    @staticmethod
    def complete_tasks():
        found = False
        task_name = input("\nEnter Task you want to Mark Complete: ").strip()

        for t in tasks:
            if t["Task"].lower() == task_name.lower():   
                if t["Completed"] == True:
                    print("Task is already Completed!!")
                    return
                else:
                    t["Completed"] = True
                    found = True
                    print("Task Is Marked Completed!!")
                    Storage.save_tasks()
                    return
        if not found:
            print("No Such Task Found!!")
            return    

    @staticmethod 
    def delete_tasks():
        found = False
        name = input("\nEnter Task you want to Delete: ").strip()
        for t in tasks:
            if t["Task"].lower() == name.lower():
                tasks.remove(t)
                found = True
                print("Task Deleted Successfully!")
                Storage.save_tasks()
                return
        if not found:
            print("Task Not Found!!")
            return
            
while True:
    print("============TASK MANAGER===========")
    print("1. ADD TASK")
    print("2. REMOVE TASK")
    print("3. MARK TASK")
    print("4. VIEW TASK")
    print("5. EXIT")

    try:
        a = int(input("\nEnter Choice: "))
    except ValueError:
        print("Please Enter a Valid Number!")
        continue
    
    if a == 5:
        print("Program Exited Successfully!!")
        break
        
    match a:
            case 1:
                Manage.add_tasks()
            case 2:
                Manage.delete_tasks()
            case 3:
                Manage.complete_tasks()
            case 4:
                Manage.view_tasks()
            case _:
                print("Enter a Valid Choice!!")

