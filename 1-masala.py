class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age} yosh)"


class Kurs:
    def __init__(self, kurs_name, kurs_teacher):
        self.kurs_name = kurs_name
        self.kurs_teacher = kurs_teacher
        self.talabalar_soni = 0
        self.talabalar = []

    def add(self, new_student):
        self.talabalar.append(new_student)
        self.talabalar_soni += 1

    def delete(self, student):
        if student in self.talabalar:
            self.talabalar.remove(student)
            self.talabalar_soni -= 1
            print(f"{student.name} kursdan o‘chirildi.")
        else:
            print("Bunday talaba kursda yo‘q.")

    def info_kurs(self):
        print(f"\nKurs nomi: {self.kurs_name}")
        print(f"O‘qituvchi: {self.kurs_teacher}")
        print(f"Talabalar soni: {self.talabalar_soni}")
        print("Talabalar ro‘yxati:")
        for talaba in self.talabalar:
            print(" -", talaba)


kurs1 = Kurs("Python Backend", "Aliyev")
kurs2 = Kurs("Frontend React", "Karimova")


talabalar1 = [Talaba(f"Talaba_PB_{i}", 18 + i % 5) for i in range(1, 11)]
talabalar2 = [Talaba(f"Talaba_FR_{i}", 17 + i % 6) for i in range(1, 11)]

for t in talabalar1:
    kurs1.add(t)

for t in talabalar2:
    kurs2.add(t)

kurs1.delete(talabalar1[2])
kurs1.delete(talabalar1[5])

kurs2.delete(talabalar2[0])
kurs2.delete(talabalar2[7])

kurs1.info_kurs()
kurs2.info_kurs()
