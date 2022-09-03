# Kenneth

def translate(text):
    translation = ""
    for letter in text:
        if letter in "ñÑ": translation = translation + "h"
        elif letter in "çÇ": translation = translation + "e"
        elif letter in "ß": translation = translation + "o"
        elif letter in "ö": translation = translation + "l"
        elif letter in "µ": translation = translation + ":)"
        elif letter in "ü": translation = translation + " "
        else: translation = translation + letter

    return translation




def encode(text):
    translation = ""
    for letter in text:
        if letter in "h": translation = translation + "ñ"
        elif letter in "e": translation = translation + "ç"
        elif letter in "o": translation = translation + "ß"
        elif letter in "l": translation = translation + "ö"
        else: translation = translation + letter

    return translation


#-----------------------------------------------------------------------------------------------------------


print(translate("hello"))


# Philip

# Grade
