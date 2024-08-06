import re

# Dictionary of emoji codes and their corresponding emojis
emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    ":1st_place_medal:": "🥇",
    ":candy:": "🍬",
    # Add more emoji codes and their corresponding emojis here
}

def emojize(text):
    # Regular expression pattern to match emoji codes or aliases
    pattern = r":\w+?:"

    # Find all matches of emoji codes or aliases in the text
    matches = re.findall(pattern, text)

    # Replace each emoji code or alias with its corresponding emoji
    for match in matches:
        emoji = emoji_dict.get(match, match)
        text = text.replace(match, emoji)

    return text

def main():
    # Prompt the user for input
    text = input("Enter a text in English: ")

    # Emojize the text
    emojized_text = emojize(text)

    # Output the emojized text
    print("Output:", emojized_text)

if __name__ == "__main__":
    main()
