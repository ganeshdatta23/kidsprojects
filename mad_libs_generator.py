
def mad_libs_generator():
    print("Welcome to Mad Libs!")

    # Get words from the user
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")

    # Create the story
    story = f"\nToday I went to the {adjective1} zoo. I saw a {noun1} {verb1} {adverb1}. \
It was so {adjective2}! Then I saw a {noun2} that was {verb2}. It was a crazy day!"

    print(story)

if __name__ == "__main__":
    mad_libs_generator()

