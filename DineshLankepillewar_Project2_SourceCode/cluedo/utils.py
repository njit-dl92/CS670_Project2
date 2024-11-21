def validate_input(prompt, options):
    while True:
        response = input(prompt).strip()
        if response in options:
            return response
        print("Invalid input. Please try again.")
