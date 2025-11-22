# Building To-Do-List
import os
task_list = []
# Show the To-Do-List
def show_tasks():
    if len(task_list) == 0:
        print("No tasks yet")
    else:
        for i,task in enumerate(task_list,1):
            print(f"{i} : {task}")

# Adding tasks in To-Do-List at last
def add_task(task):
    task_list.append(task)
    print("Task added")

#Adding task at specific index
def extend_task(index,task):
    task_list.insert(index,task)
    print("Task added")

# Deleting a task
def delete_task(index):
    if len(task_list) == 0:
        print("To-do-List is empty.")
    elif index > 0 and len(task_list) > index:
        removed = task_list.pop(index-1)
        print(f"Deleted {removed} ")
    else:
        print("Invalid task number.")

while True:
    print("To DO List".center(30,"="))
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option(1-4): ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        question = input("Do you want to add task before previos tasks?(Yes/No)")
        if question == 'Yes':
            idx = int(input("Enter the task number at which task is add:")) - 1
            task = input("Enter task: ")
            extend_task(idx,task)
            print(idx)
        if question == "No":
            task = input("Enter task: ")
            add_task(task)
    elif choice == '3':
        show_tasks()
        try :
            idx = int(input("Enter task number to delete: "))
            delete_task(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option")
os.system('cls')



