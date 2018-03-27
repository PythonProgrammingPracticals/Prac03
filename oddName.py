""" CELINA KAESAR M. LUMAIN """

def main ():

# Get user's name and frequency

    name = get_name()
    freq = int(input("Input the frequency of letters to print: "))
    print_letters_of_freq(name, freq)

def get_name():
    name = str(input("Enter your name:"))
    status = error_check(name)
    while status != "for alphabetical letters and spaces: yes" :
        print(status)
        name = str(input("ERROR! Please try again. Enter your name:"))
        status = error_check(name)
    print(status)
    return name

# Perform Error Checking on Name:

def error_check(name):
    if all(x.isalpha() or x.isspace() for x in name):
        return "for alphabetical letters and spaces: yes"

    else:
        return "for alphabetical letters and spaces: no"

# Identify the frequency of letters

def print_letters_of_freq(name,freq):
    for i in range(len(name)):
        if i % freq == 0:

            print(name[i], end=" ")




main ()