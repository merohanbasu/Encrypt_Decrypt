import random
import string

q = input("You want to code or decode? ")

match q.lower():
    case "code":
        s = input("Enter a word to code: ")
        words = s.split(" ")
        n = len(words)

        # coding

        randm_char1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        randm_char2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))

        if (n < 3):
            new_char = []
            for word in words:
                new_char.append(word[::-1])
            ans = "".join(new_char)
        else:
            new_char = []
            s = s[1:] + s[0]
            s = s.split()
            for word in s:
                new_char.append(word)
            ans = "".join(new_char)
            ans = randm_char1 + ans + randm_char2

        print(ans)
    case "decode":
        s = input("Enter a word to Decode: ")
        n = len(s)

        # decoding

        if(n < 3):
            new_char = s[::-1]
        else:
            s = s[3:-3]
            new_char = s[len(s) - 1] + s[:-1]
        print(new_char)
    case _:
        print("Invalid Input")

































