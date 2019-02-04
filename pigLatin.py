from time import sleep

sentence = input("Hi, They call me latin pig translator. Enter a sentence to have fun with me:")
sleep(4)
print("Thanks for the input!! Fasten your seatbelt as you are about to enter into my world")
sleep(3)
print("I know my world is small, but it is mine!")
sleep(2)
say_something = input("Are you having Fun or not? Type(F/NF)")
if say_something in "Ff":
    print("You are great!")
    sleep(1)
    print("Now comes the translation")
    sleep(1)
#real code
    # split sentence into words
    words=sentence.strip().lower().split()
    new_words=[]
    #check for each word'
    for word in words:
        #check if the word start with a vowel
        if word[0] in "aeiou":
            #add 'Yay' to the word and add the word to a new list
            new_word = word +"Yay"
            new_words.append(new_word)
        else:
                vowel_pos =  0
                for letter in word:
                    if letter  not in "aeiou":
                        vowel_pos = vowel_pos+1
                    else:
                        break
                new_word = word[vowel_pos:]+word[:vowel_pos]+"Ay"
                new_words.append(new_word)
    new_sentence = " ".join(new_words)
print(new_sentence)  
else:
        print("You are rude!")
    sleep(1)
    print("It is my duty to serve. wait for another 2 seconds to get the translation")
    sleep(1)
    print("But don't get any ideas,coz I don't like you")
    sleep(2)
#real code
    # split sentence into words
    words=sentence.strip().lower().split()
    new_words=[]
    #check for each word'
    for word in words:
        #check if the word start with a vowel
        if word[0] in "aeiou":
            #add 'Yay' to the word and add the word to a new list
            new_word = word +"Yay"
            new_words.append(new_word)
        else:
                vowel_pos =  0
                for letter in word:
                    if letter  not in "aeiou":
                        vowel_pos = vowel_pos+1
                    else:
                        break
                new_word = word[vowel_pos:]+word[:vowel_pos]+"Ay"
                new_words.append(new_word)
    new_sentence = " ".join(new_words)
 print(new_sentence)
