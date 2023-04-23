# get sentence from user

original = input("Please enter a sentence: ").strip().lower()

# split sentence into words
# use string method called .split()

words = original.split()

# loop through words and convert to pig latin

new_words = []
vowels = "aeiou"

for word in words:
    # if starts with vowel, just add "yay"
    if word[0] in vowels:
        new_word = word + "yay"
        new_words.append(new_word)
    # otherwise, move first consonant cluster to end and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in vowels:
                vowel_pos = vowel_pos + 1
            else:
                break # breaks out of loop - can also use continue (skips rest of loop)
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick words back together

output = " ".join(new_words)

# output the final string 

print(output)
