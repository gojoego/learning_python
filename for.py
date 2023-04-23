# makes an iterable [1,2,3,4,5,6,7,8,9,10] - range iterable 
# range_iterable = range(1,11,2)

# for number in range_iterable:
#    print(number)

# vowels = 0
# consonants = 0

# for letter in "Hello":
#    if letter.lower() in "aeiou":
#        vowels = vowels + 1
#    elif letter == " ":
#        pass
#    else:
#        consonants = consonants + 1

# print("There are {} vowels".format(vowels))
# print("There are {} consonants".format(consonants))

students = {
    "male": [   "Tom",
                "Charlie",
                "Harry",
                "Frank"],
    "female": [ "Sarah",
                "Huda",
                "Samantha",
                "Emily",
                "Elizabeth"]
    }

            # iterable 
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
