import random

class Generate:

    def __init__(self, MIN_num=1, MAX_num=100):
        self.MIN_num = MIN_num
        self.MAX_num = MAX_num
        self.number_generator = random.randint(MIN_num,MAX_num)
    
    def player_result(self,guess_number):

        if guess_number > self.number_generator:
            return ("HIGH")
        elif guess_number < self.number_generator:
            return("LOW")
        else:
            return("Correct")