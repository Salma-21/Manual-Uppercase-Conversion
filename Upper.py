
class mystr(str):
    def __init__(self, txt):
        self.txt = txt

    def upper(self):
        res=""
        for c in self.txt:
            if 97 <= ord(c) <= 122:
                res+=chr(ord(c) - 32)
            else:
                res+=c
        return res

input_string = input("Enter a sentence: ")
t1=mystr(input_string)

print(t1.upper())