def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return[task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.txt","w")as file:
      for task in tasks:
          file.write(task + "\n")
def add_task(tasks):
    task=input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks Avaliable.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def delete_task(tasks):
    view_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        task_no=int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            removed=tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def Todo_App():
    tasks=load_tasks()
    while True:
        print("\n......TO-DO LIST MENU......")
        print("1.Add Task")
        print("2.View Task")
        print("3.Remove Task")
        print("4.Exit")
        choice = input("Enter your choice: ")
        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_tasks(tasks)
        elif choice=="3":
            delete_task(tasks)
        elif choice=="4":
            print("Exiting the application. Thank You!")
            break
        else:
            print("Invalid choice. Please try again.")
Todo_App()