import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.child_blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        # Memilih satu alel dari ayah dan satu dari ibu
        father_allele = random.choice(list(self.father.blood_type))
        mother_allele = random.choice(list(self.mother.blood_type))

        # Menggabungkan alel untuk menentukan golongan darah anak
        child_alleles = sorted([father_allele, mother_allele])
        child_blood_type = ''.join(child_alleles)

        # Menentukan golongan darah berdasarkan alel
        if child_blood_type == 'AA':
            return 'A'
        elif child_blood_type == 'AO' or child_blood_type == 'OA':
            return 'A'
        elif child_blood_type == 'BB':
            return 'B'
        elif child_blood_type == 'BO' or child_blood_type == 'OB':
            return 'B'
        elif child_blood_type == 'AB' or child_blood_type == 'BA':
            return 'AB'
        elif child_blood_type == 'OO':
            return 'O'
        else:
            return 'Unknown'

# Input golongan darah dari pengguna
father_blood_type = input("Masukkan golongan darah ayah (contoh: AO, AB, BO, dll): ").upper()
mother_blood_type = input("Masukkan golongan darah ibu (contoh: AO, AB, BO, dll): ").upper()

# Membuat objek Father dan Mother
father = Father(father_blood_type)
mother = Mother(mother_blood_type)

# Membuat objek Child dan menentukan golongan darah anak
child = Child(father, mother)

# Menampilkan hasil
print(f"Golongan darah ayah: {father.blood_type}")
print(f"Golongan darah ibu: {mother.blood_type}")
print(f"Golongan darah anak: {child.child_blood_type}")