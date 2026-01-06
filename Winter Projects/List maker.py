import math 
import random 

# Initial task list 
tasks = []

# Auxiliary functions
def displayTasks(all_tasks):
    print('\nYour tasks: ')
    if len(all_tasks) <= 0:
        print('No Tasks to do!')
        print('\n')
    else:
        for index,tasks in enumerate(all_tasks):
            print(f'{index+1}: {tasks}')
        

def newOperations(all_tasks):
    operations = input("Press 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")

    if operations == 'A':
        addTask(all_tasks)
    elif operations == 'E':
        editTask(all_tasks)
    elif operations == 'R':
        removeTask(all_tasks)
    elif operations == 'F':
        return 
    else:
        newOperations(all_tasks)

def editTask(all_tasks):
    task_number = input("Enter the number of the task you want to edit: ")
    newTask = input('Edit task: ')
    all_tasks[int(task_number-1)] = newTask
    print(f'Item {task_number} has been edited!')
    displayTasks(all_tasks)
    newOperations(all_tasks)


def removeTask(all_tasks):
    task_number = input("Enter the number of the task you want to remove: ")
    all_tasks.remove(all_tasks[int(task_number)-1])
    print(f'\nItem {task_number} is removed from the list!')
    displayTasks(all_tasks)
    newOperations(all_tasks)

def addTask(all_tasks):
    newTask = input("Please enter in a new task that you want to add: ")
    all_tasks.append(newTask)

    displayTasks(all_tasks)

    newOperations(all_tasks)

# Start application 
addTask(tasks) 