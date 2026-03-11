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
            self.logic.add_task()
            self.clear_screen()

        elif input_user == 2:
            self.logic.mark_complete_task()
            self.clear_screen()

        elif input_user == 3:
            self.logic.remove_task()
            self.clear_screen()
        
        elif input_user == 4:
            self.clear_screen()
            self.logic.view_task()
        
        elif input_user == 5:
            self.logic.exit_task()
            self.clear_screen()
        
        else:
            self.clear_screen()
            print("Choose Number that is on the Menu!")


