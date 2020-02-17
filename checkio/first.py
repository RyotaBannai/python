import re
def checkio(text: str) -> str:
    
    print(text)
    chars = sorted(re.findall('[a-zA-Z]', text))
    num = len(chars)
    temp = ''
    
    for i, v in enumerate(chars):
        if i == 0 : 
            temp = v
            continue
        print(i ,v)
        if temp.upper() == v.upper() : 
            print('second if',temp) # but the letter which comes first
            return temp
        if i == num: 
            print('last if',v)
            return v
        temp = v
        

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")