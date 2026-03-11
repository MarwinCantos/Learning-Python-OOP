class Guess:

    def start_game(self):
        print("|        WELCOME TO THE GUESSING NUMBER      |")
        print("|        Guess the Number from 1 to 100      |")
    
    def player_guess_number(self):
        while True:
            try:
                guess_number = int(input("Guess the Number: ").strip())
                return guess_number
                
            except ValueError:
                print("Use only whole numbers.")
        
    def show_result(self,result):
        if result == "LOW":
            print("Wrong, Try Higher Number")
        elif result == "HIGH":
            print("Wrong, Try Lower Number")
        else:
            print("Correct")