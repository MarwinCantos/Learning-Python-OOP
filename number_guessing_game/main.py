from controller import Game

def main():
    run = Game()
    run.process()

if __name__ == "__main__":
    main()











# number_generator = random.randint(1,10)
# while True:

#     try:
#         guess_number = int(input("Guess the Number: ").strip())

#         if guess_number == number_generator:
#             print("Correct")
#             break

#         elif guess_number > number_generator:
#             print("Wrong, try Lower Number")
            
#         else:
#             print("Wrong, try Higher Number")
    
#     except ValueError:
#         print("Use only Whole Numbers")

        

    