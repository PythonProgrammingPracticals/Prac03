""" CELINA KAESAR M. LUMAIN """


def get_name(prompt):
    result = str(input(prompt))
    return result

def main():
    name = str(input("Enter your name:"))

    count = 0
    for each in list(name):
        if count % 2 != 0:
            print(each)
            count += 1
        else:
            count += 1

    for char in name:
        print(char, char.isalpha())

    if all(x.isalpha() or x.isspace() for x in name):
        print("for alphabetical letters and spaces: yes")

    else:
        print("for alphabetical letters and spaces: no")