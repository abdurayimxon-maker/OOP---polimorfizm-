class Taqvim:

    def grigoriyandan_hijriyga(self, year):
        return (year - 622) * 33 // 32

    def hijriydan_grigoriyanga(self, year):
        return year * 32 // 33 + 622

    def is_kabisa(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


t = Taqvim()

print(t.grigoriyandan_hijriyga(2025))
print(t.hijriydan_grigoriyanga(1447))
print(t.is_kabisa(2024))