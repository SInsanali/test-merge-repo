my_name = "sam"
age = 25

question = input("what is your name?").lower()

is_running = True

while is_running:
    if question == my_name:
        print(f"your name is {my_name}")
    else:
        print(f"you are not {my_name}")