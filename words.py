
def print_upper_words(words, must_start_with) : 
    # this should print "HELLO", "HEY", "YO", and "YES"

    upper_words  = [word.upper() for word in words if word[0] in must_start_with ]
    messaje  = ""
    last_word = len(upper_words) - 1  
    for word in upper_words : 
        if word  == upper_words[last_word]:
            messaje = messaje + f" and \"{word}\"" 
            print(messaje) 
            return messaje

        messaje = messaje + f"\"{word}\","    
        
    print(messaje)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})