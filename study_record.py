from patient_record import PatientRecord

class StudyRecord(PatientRecord):  # Hereda de PatientRecord
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type, 
                 modality, study_date, study_time, study_instance_uid, series_number, number_of_frames):
        # Llamar al constructor de la superclase (PatientRecord)
        super().__init__(name, age, birth_date, sex, weight, patient_id, id_type)
        
        # Atributos específicos de StudyRecord
        self.modality = modality
        self.study_date = study_date
        self.study_time = study_time
        self.study_instance_uid = study_instance_uid
        self.series_number = series_number
        self.number_of_frames = number_of_frames

    # Método para obtener información del estudio
    def get_study_info(self):
        return {
            "Modality": self.modality,
            "Study Date": self.study_date,
            "Study Time": self.study_time,
            "Study Instance UID": self.study_instance_uid,
            "Series Number": self.series_number,
            "Number of Frames": self.number_of_frames
        }

    # Método para establecer nueva información del estudio
    def set_study_info(self, modality, study_date, study_time, study_instance_uid, series_number, number_of_frames):
        self.modality = modality
        self.study_date = study_date
        self.study_time = study_time
        self.study_instance_uid = study_instance_uid
        self.series_number = series_number
        self.number_of_frames = number_of_frames

    # Sobrescribir el método de impresión de información
    def get_full_info(self):
        patient_info = self.get_patient_info()  # Llama al método de la superclase
        study_info = self.get_study_info()
        return {**patient_info, **study_info}  # Combina la información del paciente y del estudio
    
    