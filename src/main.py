from agent.brain import stream_graph_updates


def main():
    print("Welcome to the AI agent! Type 'quit', 'exit', or 'q' to end the conversation.")
    while True:
        try:
            # Prompt user for input
            user_input = input("User: ")

            # Exit conditions
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            # Call the function to process user input and display responses
            stream_graph_updates(user_input)

        except Exception as e:
            # Handle any unexpected exceptions
            print(f"An error occurred: {str(e)}")
            break

if __name__ == "__main__":
    main()
