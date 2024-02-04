import pyfiglet

# title
def print_title(text):
    font = pyfiglet.Figlet()
    title = font.renderText(text)
    print(title)

# main menu
def main_menu():
    print("What do you want to do")
    print("Add tak : Add")
    print("See all tak : see")
    print("Remove tak : Remove")
    user_operation = input("enter here : ")
    user_operation.lower()
    if user_operation not in ["add", "see", "remove"]:
        print("Invalid operation")
        exit()
    else:
        return user_operation

# add task
def add_task(task_list):
    print("Add your task")
    user_task = input("Here : ")
    task_list.append(user_task)
    print("Task added successfully")
# see task
def see_task(task_list):
    for task in task_list:
        print(task)

# remove task
def remove_task(task_list):
    for task in task_list:
        print(task)
    print("Enter task you want to remove")
    task_remove = input("Here : ")
    task_list.remove(task_remove)
    print("task removed")
    
# what task to perform
def perform_task(user_operation,task_list):
    match  user_operation:
        case "add":
            add_task(task_list)
        case "see":
            see_task(task_list)
        case "remove":
            remove_task(task_list)
        case _: 
            print("Invalid task")

# calling title
print_title("To Do List")
# list for holding tasks
task_list = []
while True:
    # calling main menu
    user_operation = main_menu()
    # calling task performer function
    perform_task(user_operation,task_list)
    print("Enter exit for exit : Enter continue for continue")
    exitt = input("Here : ")
    exit = exitt.lower()
    if exitt == "exit":
        break
