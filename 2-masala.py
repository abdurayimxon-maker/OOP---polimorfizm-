class Convertor:
    def __init__(self):
        self.en_to_ru_map = {
            'a': 'а', 'b': 'б', 'c': 'ц', 'd': 'д', 'e': 'е',
            'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ж',
            'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
            'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т',
            'u': 'у', 'v': 'в', 'w': 'в', 'x': 'кс', 'y': 'й',
            'z': 'з',

            'A': 'А', 'B': 'Б', 'C': 'Ц', 'D': 'Д', 'E': 'Е',
            'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ж',
            'K': 'К', 'L': 'Л', 'M': 'М', 'N': 'Н', 'O': 'О',
            'P': 'П', 'Q': 'Қ', 'R': 'Р', 'S': 'С', 'T': 'Т',
            'U': 'У', 'V': 'В', 'W': 'В', 'X': 'КС', 'Y': 'Й',
            'Z': 'З',

            "yo": "ё", "yu": "ю", "ya": "я",
            "Yo": "Ё", "Yu": "Ю", "Ya": "Я"
        }

        self.ru_to_en_map = {v: k for k, v in self.en_to_ru_map.items()}

    def en_to_ru(self, text):
       
        text = text.replace("yo", "ё").replace("yu", "ю").replace("ya", "я")
        text = text.replace("Yo", "Ё").replace("Yu", "Ю").replace("Ya", "Я")

        result = ""
        for ch in text:
            result += self.en_to_ru_map.get(ch, ch)
        return result

    def ru_to_en(self, text):
        result = ""
        for ch in text:
            result += self.ru_to_en_map.get(ch, ch)
        return result



conv = Convertor()

matn_en = "Salom dunyo"
matn_ru = conv.en_to_ru(matn_en)
print(matn_ru)       

print(conv.ru_to_en(matn_ru))  
