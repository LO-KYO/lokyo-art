def main():
    print("Welcome to the Beginner Game!")
    running = True

    while running:
        user_input = input("Enter 'q' to quit or 'p' to play: ").lower()
        
        if user_input == 'q':
            running = False
            print("Thanks for playing!")
        elif user_input == 'p':
            print("Starting the game...")
            # Game logic would go here
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()