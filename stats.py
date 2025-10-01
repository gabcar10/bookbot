def word_count(full_text):
    #text is split & counted
    word_count = len(full_text.split())
    return word_count

def char_count(inp_string):
    char_count = {}
    for current_char in inp_string: 
        #print(current_char.lower())     #debug OK
        if current_char.lower() in char_count: #IF found (TRUE)
            char_count[current_char.lower()] += 1   #increment current char
            #print(f"add {current_char.lower()}; count {char_count[current_char.lower()]}")
        else:                                       #create new record for the current character
            char_count[current_char.lower()] = 1
            #print(f"new char: {current_char.lower()}")
    return char_count

#-------------------------------------------------------------------------------------

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items): 
    return items['num']     

def sort_by_count(dict):        #(dict{key, value})
    #OK: Each dictionary should have two key-value pairs: one for the character itself and one for that character's count 
    #(e.g. {"char": "b", "num": 4868}).
    #print(f"nice! {dict['char']}, {dict['num']}")
    current_dict = {}     #{"char": x, "num": 12} 
    # .sort() method works on a list! So I need a list of dictionaries (see below).
    list_dict = []       #[{"char": x, "num": 12}, {"char": y, "num": 40}]
    for char in dict:
        #discard non alphanumerical characters
        #if char.isalpha():
        current_dict["char"] = char
        current_dict["num"] = dict[char]
        list_dict.append({"char": char, "num": dict[char]})     #doesn't work WHEN list_dict.append(current_dict)
            #print(current_dict)    #OK, 31 lines w/ good values
            #print(list_dict)    #KO, if appending current_dict; OK when writing the dict (not the variable)
    #print(list_dict)    #KO, if appending current_dict; OK when writing the dict (not the variable)
    list_dict.sort(reverse=True, key=sort_on)
    #print(list_dict)   #OK
    return list_dict
