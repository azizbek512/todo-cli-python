tasks = []

while True:
    print("=== TO-DO LIST ===\n",
        "1. Add task\n",
        "2. See tasks\n",
        "3. Mark as done\n",
        "4. Delete task\n",
        "5. Exit\n")

    choice = int(input("Choose: "))

    if choice == 1:
        print("=== ADD NEW TASK ===")
        task = input("Insert new task: ")
        tasks.append({"task": task, "done": False})
        print("New task added successfully!")

    elif choice == 2:
        print("=== EXISTING TASKS ===")
        for index, item in enumerate(tasks, start=1):
            mark = "✅" if item["done"] else " "
            print(f"{index}. [{mark}] {item['task']}")

    elif choice == 3:
        print("=== MARK AS DONE ===")
        num = int(input("Select task to mark as done: "))  
        tasks[num-1]["done"] = True 

    elif choice == 4:
        print("=== DELETE TASK ===")
        num = int(input("Select task to delete: ")) 
        del tasks[num-1] 
        

    elif choice == 5:
        break

    else:
        print("Incorrect choice!\nPlease try again...")