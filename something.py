print("To start, type \'start\'")
fromUser = input()
while True:
    if fromUser == "start":
        print("Start game!")
    elif fromUser == "quit":
        print("Game over!")
        break
    elif fromUser == "go":
        print("go somewhere")
    else:
        print("To start, type 'start'")
    fromUser = input()
