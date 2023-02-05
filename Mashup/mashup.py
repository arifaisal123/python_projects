print("This program messes up name! Input your, and your friend's name, and it will greet you!!!"+ "\n"+ "You have to input two names one after another in the format FIRST LAST")

first = []
last = []
count = 0

while True:
    try:
        firstname, lastname = input("Please enter the name: ").split(" ")
    except ValueError:
        print("Please input two names only separated by space, i.e.- David Beckham")
    else:
        first.append(firstname)
        last.append(lastname)
        count += 1

    if count == 2:
        break

mash_first1 = first[0][0:len(first[0])//2] + first[1][len(first[1])//2:]
mash_last1 = last[0][0:len(last[0])//2] + last[1][len(last[1])//2:]

mash_first2 = first[1][0:len(first[1])//2] + first[0][len(first[0])//2:]
mash_last2 = last[1][0:len(last[1])//2] + last[0][len(last[0])//2:]

print("Hello,", mash_first1, mash_last1 + ", and", mash_first2, mash_last2)
