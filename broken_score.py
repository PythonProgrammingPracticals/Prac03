
# Broken score exercise. Must input numbers and not letters!

def main():

    print("Hello There!")

    score = get_score()

    if score < 0 or score > 100:
        print("Invalid score")

    elif score >= 90:
        print("Great job, mate!")

    elif score >= 50:
        print("Don't worry. Still Passable.")

    else:
        print("Oh my! That's very Bad... Try again next time!")


def get_score():
    score = int(input("Enter score here: "))
    return score



main()