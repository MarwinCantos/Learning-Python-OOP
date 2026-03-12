class Start:
    def welcome(self):
        print("\n|        Welcome To yur To-do List       |")

        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")

    def pick_user(self):
        while True:
            try:
                input_user = int(input("Choose Number: ").strip())
                return input_user
            
            except ValueError:
                print("Choose only the Number")

    def add_task_input(self):
        return input("What task do you want to add: ").strip().upper()

    def choose_task(self):
        try:
            return int(input("Enter task number: ")) - 1
        except ValueError:
            return -1

    def show_tasks(self, tasks):

        if not tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

    def message(self, text):
        print(text)
