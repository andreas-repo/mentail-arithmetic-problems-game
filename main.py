import random
import time
import operator

def create_exercise_easy():
    # create random number between 1 and 10
    first_number = random.randint(1, 10)
    # create random number between 1 and 10
    second_number = random.randint(1, 10)
    # selects randomly between 3 possible operators
    random_operator = random.choice(["+", "-", "*"])
    # make a lookup table with operator function
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    # use lookup table to turn the randomly selected operator character in the correct usable operator with ops and creates the result of the calculation
    result = ops[random_operator](first_number, second_number)
    # build exercise string from first random number, operator and the second random number
    exercise = f'{first_number} {random_operator} {second_number}'
    # returns the exercise string and result
    return exercise, result

# method which checks the input for the correct type
def check_input(unchecked_input):
    try:
        # if the float() method doesnt throw an exception...
        float(unchecked_input)
        # True is returned to indicate that the input was correct
        return True
    # when an exception is produced...
    except ValueError:
        # a message informs the user about this fact and...
        print("Wrong input format! Please use only numbers")
        # returns False
        return False


# creates main game method
def create_game_flow():
    running = True

    print("Welcome to mental calculation the game!")
    print("Please input the correct solution to the shown math problem.")
    while(running):
        exercise_string, result = create_exercise_easy()
        print("Please solve the following exercise:")
        print(exercise_string)
        start_time = time.time()
        unchecked_input = input()

        # checks for the word "exit" to start the shutdown process for the application
        if (unchecked_input == "exit"):
            print("Program will be closed.")
            running = False
            exit()

        # if the check_input() method produces the correct True output then the input will be processed
        if(check_input(unchecked_input)):

            input_float = float(unchecked_input)
            end_time = time.time()
            print(f'Your answer is {input_float}.')
            if (float(result) == float(input_float)):
                print("CORRECT answer!")
                time_passed = end_time - start_time
                print("Time needed to solve exercise:", round(time_passed), "seconds.")
            else:
                print("WRONG answer! Try again!")


create_game_flow()

