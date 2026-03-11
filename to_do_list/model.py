class Menu:

    def __init__(self):
        self.tasks = []

    def add_task(self):
        input_task = input("What task do you want to add: ").strip().upper()
        self.tasks.append({"task": input_task, "completed": False})
        print("Task added.")

    def view_task(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

    def mark_complete_task(self):
        self.view_task()
        num = int(input("Enter task number to mark complete: "))
        if 0 < num <= len(self.tasks):
            self.tasks[num-1]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")

    def remove_task(self):
        self.view_task()
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(self.tasks):
            removed = self.tasks.pop(num-1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")

    def exit_task(self):
        print("Exiting program.")
        exit()