class String:
    def __init__(self, text):
        self.text = text

    def to_lower(self):
        result = ""
        for ch in self.text:
            code = ord(ch)
            
            if 65 <= code <= 90:
                result += chr(code + 32)
            else:
                result += ch
        return result

    def to_upper(self):
        result = ""
        for ch in self.text:
            code = ord(ch)

            if 97 <= code <= 122:
                result += chr(code - 32)
            else:
                result += ch
        return result

    def is_lower(self):
        has_letter = False
        for ch in self.text:
            code = ord(ch)
            if 65 <= code <= 90:  
                return False
            if 97 <= code <= 122:
                has_letter = True
        return has_letter

    def is_upper(self):
        has_letter = False
        for ch in self.text:
            code = ord(ch)
            if 97 <= code <= 122: 
                return False
            if 65 <= code <= 90:
                has_letter = True
        return has_letter



s = String("Salom Dunyo")

print(s.to_lower())   
print(s.to_upper())   
print(s.is_lower())  
print(s.is_upper())   

s2 = String("HELLO")
print(s2.is_upper())  
