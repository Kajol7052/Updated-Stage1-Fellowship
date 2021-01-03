from Doctor import Doctor
from Patient import Patient
import json
class CliniqueManagement:
    def __init__(self,doctorFilePath,patientFilePath):
        self.doctorFilePath = doctorFilePath
        self.patientFilePath = patientFilePath
        self.doctors =[]
        self.patients = []
        self.fetchDoctors()
        self.fetchPatients()

    def fetchDoctors(self):
        doctorDict = json.load(open(self.doctorFilePath,'r'))
        for doc in doctorDict.items():
            self.doctors.append(Doctor(doc[1]['id'],doc[1]['name'],doc[1]['spec'],doc[1]['avail']))
        return self.doctors
    
    def fetchPatients(self):
        patientDict = json.load(open(self.patientFilePath,'r'))
        for pat in patientDict.items():
            self.patients.append(Patient(pat[1]['id'],pat[1]['name'],pat[1]['phone'],pat[1]['age']))
        return self.patients

    def searchDoctor(self,search):
        for doc in self.doctors:
            if doc.getId() == search or doc.getSpec() == search:
                print(doc.getId(),doc.getName())

    def searchPatient(self,search):
        for pat in self.patients:
            if pat.getId() == search :
                print(pat.getId(),pat.getName())

    def takeAppointment(self):
        print("Appointment")

if __name__ == "__main__":
    cliniqueManagement = CliniqueManagement("/Users/kajol7052/Desktop/OOPS_Programs/CliniqueManagement/Doctor.json","/Users/kajol7052/Desktop/OOPS_Programs/CliniqueManagement/Patient.json")
    cliniqueManagement.takeAppointment()
    cliniqueManagement.searchDoctor("1")
    cliniqueManagement.searchPatient("1")