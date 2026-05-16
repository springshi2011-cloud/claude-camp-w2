#work with the todo list, we can add, delete, and mark tasks as done. this section need more work later
#work through json file to save and load the todo list, we can use json module to read and write the todo list to a file. this way we can persist the data even after the program is closed.
import json
TODO_FILE = "todos.json"
todo_list = []

#define the functions to manage the todo list 
def save_todo_list(filename):   
     with open(filename, "w") as f:
        json.dump(todo_list, f, indent=4)  # Save with indentation for readability

def load_todo_list(filename):
    global todo_list
    
    try:
        with open(filename, "r") as f:
            todo_list = json.load(f)  

    except FileNotFoundError:
        todo_list = []  # Start with an empty list if file doesn't exist
    
    except json.JSONDecodeError:
        print(f"[Error] Invalid JSON in file '{filename}'")

def add_task(task):    
    todo_list.append({"task": task, "done": False})
    print(f"[OK] Added task: '{task}'")
    save_todo_list(TODO_FILE)  # Save after adding a task

def delete_task(task):    
     for item in todo_list:
        if item["task"] == task:
            todo_list.remove(item)
            print(f"[OK] Deleted task: '{task}'")
            save_todo_list(TODO_FILE)  # Save after deleting a task
            return
     print(f"[Error] Task '{task}' not found")   
        
def mark_done(task):    
    for item in todo_list:
        if item["task"] == task:
            item["done"] = True
            print(f"[OK] Marked task as done: '{task}'")
            save_todo_list(TODO_FILE)  # Save after marking a task as done
            return
    print(f"[Error] Task '{task}' not found")

def list_tasks():    
    if not todo_list:
        print("[Info] Todo list is empty")      
        return  
    
    print("\nTodo List:")    
    for idx, item in enumerate(todo_list, 1):        
        status = "Done" if item["done"] else "Not Done"
        print(f"{idx}. {item['task']} [{status}]") 

#define the menu to interact with the todo list, we can use a simple text-based menu to allow the user to choose different options for managing their tasks. this will make it easier for users to navigate and use the program effectively.    

def show_menu():
            print("\nTodo Menu:")
            print("1. View tasks")
            print("2. Add task")
            print("3. Delete task")
            print("4. Mark task as done")
            print("5. Exit")

#define the main function to run the program, we can use a while loop to continuously show the menu and process user input until they choose to exit. this will allow users to manage their todo list in a seamless and interactive way.

def main():    
    print("Welcome to the Todo List Manager!")   
    load_todo_list(TODO_FILE)

    while True:  
        show_menu()
        choice = input("Choose an option: ").strip()    

        if choice == "1":
            list_tasks()

        elif choice == "2":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:            
                print("[Error] Task cannot be empty")

        elif choice == "3":
            task = input("Enter task to delete: ").strip()
            if task:
                delete_task(task)     
            else:            
                print("[Error] Task cannot be empty")
        
        elif choice == "4":
            task = input("Enter task to mark as done: ").strip()
            if task:
                mark_done(task)     
            else:            
                print("[Error] Task cannot be empty")   
                
        elif choice == "5":
            save_todo_list(TODO_FILE)  # Save before exiting
            print("Exiting...")
            break   
        else:
            print("[Error] Task cannot be empty")    
        
#run the main function when the script is executed, this will start the program and allow users to interact with their todo list right away. this is a common practice in Python to ensure that the main logic of the program is only executed when the script is run directly, and not when it is imported as a module in another script.

if __name__ == "__main__":    
    main()           
