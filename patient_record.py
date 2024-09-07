import logging

class PatientRecord:
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.sex = sex
        self.weight = weight
        self.patient_id = patient_id
        self.id_type = id_type

    # Métodos para establecer la información
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_sex(self, sex):
        self.sex = sex

    def set_weight(self, weight):
        self.weight = weight

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def set_id_type(self, id_type):
        self.id_type = id_type

    # Métodos para obtener la información
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_birth_date(self):
        return self.birth_date

    def get_sex(self):
        return self.sex

    def get_weight(self):
        return self.weight

    def get_patient_id(self):
        return self.patient_id

    def get_id_type(self):
        return self.id_type

    # Método para mostrar toda la información del paciente
    def display_info(self):
        info = f"Patient Name: {self.name}\n" \
               f"Age: {self.age}\n" \
               f"Birth Date: {self.birth_date}\n" \
               f"Sex: {self.sex}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Patient ID: {self.patient_id} (ID Type: {self.id_type})"
        print(info)

# Ejemplo de uso
patient = PatientRecord("John Doe", 45, "1978-05-14", "M", 78.5, "123456", "Passport")
patient.display_info()