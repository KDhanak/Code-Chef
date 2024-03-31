# cook your dish here

def canPronounce():
    cases = int(input("Please enter the number of test-cases: "))
    
    for _ in range(cases):
        length = int(input("Please enter the lenth of the word: "))
        word = input("Please enter the word: ")
        if length < 4:
            print("YES")
        
        else:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            found = False
            
            for j in range(length - 3):
                if all(letter not in vowels for letter in word[j:j+4]):
                    found = True
                    break
            
            if found:
                print("NO")
            else:
                print("YES")
    
canPronounce()