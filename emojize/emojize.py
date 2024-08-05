from emoji import emojize

def main():
    input_str = input("Input: ")
    emojized_str = emojize(input_str) # Remove the `use_aliases=True` here
    print(f"Output: {emojized_str}")

if __name__ == "__main__":
    main()
