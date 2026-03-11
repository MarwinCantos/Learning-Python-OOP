from view import Guess
from model import Generate

import os

class Game:

    def __init__(self):
        self.logic = Generate()
        self.display = Guess()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def process(self):

        while True:

            self.display.start_game()

            while True:
                guess = self.display.player_guess_number()

                result = self.logic.player_result(guess)

                self.display.show_result(result)

                if result == "Correct":
                    self.clear_screen()
                    break

            while True:
                user_try = input("Do you want to Play again? Y/N: ").strip().upper()

                if user_try == "Y":
                    self.logic = Generate()  # generate new number
                    break

                elif user_try == "N":
                    self.clear_screen()
                    print("Thank You for Playing")
                    return

                else:
                    print("Please only type Y or N")