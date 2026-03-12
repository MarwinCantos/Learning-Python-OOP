from view import Start
from model import Menu
import os


class To_do:
    def __init__(self):
        self.display = Start()
        self.logic = Menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def process(self):
        self.display.welcome()

        input_user = self.display.pick_user()

        if input_user == 1:

            task = self.display.add_task_input()
            self.logic.add_task(task)
            self.clear_screen()
            self.display.message("Task added.")

        elif input_user == 2:

            tasks = self.logic.view_task()
            self.display.show_tasks(tasks)

            num = self.display.choose_task()

            if self.logic.mark_complete_task(num):
                self.clear_screen()
                self.display.message("Task marked complete.")
            else:
                self.clear_screen()
                self.display.message("Invalid task number.")

        elif input_user == 3:

            tasks = self.logic.view_task()
            self.display.show_tasks(tasks)

            num = self.display.choose_task()

            removed = self.logic.remove_task(num)

            if removed:
                self.clear_screen()
                self.display.message(f"Removed task: {removed['task']}")
            else:
                self.clear_screen()
                self.display.message("Invalid task number.")
        
        elif input_user == 4:
            tasks = self.logic.view_task()
            self.clear_screen()
            self.display.show_tasks(tasks)
        
        elif input_user == 5:
            exit()
        
        else:
            self.clear_screen()
            print("Choose Number that is on the Menu!")



