# To-Do List implementation

tasks = []


def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")



def view_tasks():
    if not tasks:
        print("No tasks in the To-Do List.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")


def mark_completed(task_number):
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task(task_number):
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Example usage
add_task("Learn Python")
add_task("Build a To-Do List")
add_task("Study amply for examination")
add_task("Join the virtual training")

# Scenarios
view_tasks()

mark_completed(1)
view_tasks()

delete_task(3)
view_tasks()





'''def add_task(task):

tasks.append({"task": task, "completed": False})

print("Task added successfully!")

def view_tasks():

if not tasks:

print("No tasks in the To-Do List.")

else:

print("Tasks:")

for i, task in enumerate(tasks, 1):

status = "Completed" if task["completed"] else "Not Completed"

print(f"{i}. {task['task']} - {status}")'''

#ChatGPT. (n.d.). Python code for adding and viewing tasks in a To-Do List. [Source code].