""" CELINA KAESAR M. LUMAIN """

def main ():

    name = get_name()


    count = 0
    for each in list(name):
        if count % 2 != 0:
            print(each)
            count += 1
        else:
            count += 1

    for char in name:
        print(char, char.isalpha())


def get_name():
    name = str(input("Enter your name:"))
    status = error_check(name)
    while status != "for alphabetical letters and spaces: yes" :
        print(status)
        name = str(input("ERROR! Please try again. Enter your name:"))
        status = error_check(name)
    print(status)
    return name


def error_check(name):
    if all(x.isalpha() or x.isspace() for x in name):
        return "for alphabetical letters and spaces: yes"

    else:
        return "for alphabetical letters and spaces: no"


main ()