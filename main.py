import utils

def main(): 
    exercise = input("Exercise: ")
    sets = utils.get_number("Sets: ")
    reps = utils.get_number("Reps: ")
    weight = utils.get_number("Weight: ")

    workout_data = {
        "Exercise": exercise,
        "Sets": sets,
        "Reps": reps,
        "Weight": weight
    }

    



            



if __name__ == "__main__": 
    main()