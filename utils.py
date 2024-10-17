def get_number(indicator:str):
    while True: 
        try: 
            value = round(float(input(f"{indicator}: ")) * 4) / 4
            break

        except ValueError: 
            print("You must provide a number")
    return value