def _valid_integer(prompt = 'Enter an integer : '):
    # while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            return value
        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled.")
            raise

number = _valid_integer("Please enter an integer: ")
print(f"{number} is the valid integer")

