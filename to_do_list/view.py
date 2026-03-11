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
