str1 ="hello"
str2 = "hello"
str3 = "hi"
str4=("jokol")
str5 = "morna jens"


def check_equal(str1,str2):
    if len(str1) != len(str2):
        return False

    list1 = list(str1)
    list2 = list(str2)
    for i in range(0,len(list1)):
            if list1[i] != list2[i]:
                return False
    return True


print(check_equal(str1,str4))

def reversed_word(str):
    list1 = list(str)
    list1_reversed = list1[:: -1]
    return ''.join(list1_reversed)


print(reversed_word(str5))

def check_palindrome(str):
    string_reversed = reversed_word(str)
    if check_equal(str,string_reversed) == True : return True
    else: return False

palindrome = "agnes i senga"
print(check_palindrome(palindrome))
print(check_palindrome(str1))

str5 = "pepperkake"
str6 = "per"




def contains_string(str1,str2):
    return str1.find(str2)

print(contains_string(str5,str6))



