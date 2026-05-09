class Patient:
    total_patients=0
    def __init__(self,name,age,medical_record):
        self.__name=name
        self.age=age
        self.__medical_record=medical_record
        Patient.total_patients+=1
    def show_details(self):
        return f"name {self.__name} | age {self.age}"
    @property
    def name(self):
        return self.__name;
    def get_medical_record(self):
        return self.__medical_record
    def set_medical_record(self,record):
         self.__medical_record = record
class Doctor:
    def __init__(self,name,age,salary,specialization):
        self.name=name
        self.age=age
        self.specialization = specialization       # ✅ added

        self.__salary=salary
    def show_details(self):
        return f"name {self.name} | age {self.age}"
    @staticmethod
    def hospital_description():
        return "Welcome to City Hospital — Caring for You Always"
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
       if type(salary)==str:
            print("Salary should always by int")
       elif salary<0:
            print("Salary cannot be negative")
       elif salary==0:
           print("Salary cannot be 0")
       else:
        self.__salary=salary
    def describe(self):
        return "I am a doctor"
class specialist(Doctor):
    def __init__(self,year_of_experience,name,age):
        super().__init__(name,age)
        self.year_of_experience=year_of_experience
    def describe(self):
        return "I am a specialist"
   
   
   
class Operator:
    def __init__(self, operation_type):             # ✅ added __init__
        self.operation_type = operation_type

    def perform_operation(self):
        print(f"Performing {self.operation_type} operation")
   
class Surgeon(specialist,Operator):
    def __init__(self,name, age, salary, specialization, year_of_experience):
        super().__init__(name, age, salary, specialization, year_of_experience)
        
    def describe(self):
        return f"I am a Surgeon specialized in {self.operation_type}"
def perform_operation(self):
        print(f"Performing {self.operation_type} operation")
        print(f"Experience: {self.year_of_experience} years")     
        
        
        
               
# --- Testing ---
my_patient = Patient("Ali", 18, "Fever")           # ✅ 3 arguments
print(my_patient.show_details())                   # → Patient Name: Ali | Age: 18
print(my_patient.get_medical_record())             # → Fever
my_patient.set_medical_record("Cold")
print(my_patient.get_medical_record())             # → Cold
print(Patient.total_patients)                      # → 1

my_doctor = Doctor("Dr. Ali", 40, 80000, "Cardiology")
print(my_doctor.show_details())                    # → Doctor Name: Dr. Ali | Specialization: Cardiology
print(my_doctor.describe())                        # → I am a General Doctor
print(Doctor.hospital_description())              # → Welcome to City Hospital...

my_specialist = specialist("Dr. Sara", 35, 90000, "Neurology", 10)
print(my_specialist.describe())                    # → I am a Specialist in Neurology with 10 years of experience

my_surgeon = Surgeon("Dr. Ahmed", 45, 120000, "Brain", 15, "Brain Surgery")
print(my_surgeon.describe())                       # → I am a Surgeon specialized in Brain Surgery
my_surgeon.perform_operation()                     # → Performing Brain Surgery operation
                                                   # → Experience: 15 years

# isinstance() checks
print(isinstance(my_doctor, Doctor))               # True
print(isinstance(my_specialist, Doctor))           # True
print(isinstance(my_specialist, specialist))       # True
print(isinstance(my_surgeon, Doctor))              # True
print(isinstance(my_surgeon, Operator))            # True
print(isinstance(my_doctor, specialist))           # False
    