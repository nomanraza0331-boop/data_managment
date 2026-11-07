
import csv
'''
field=["Empid","Empname","Gender","Age","Deparment","Role","Salary"]

def create_file():
    with open ("employees.csv","a",newline="")as file:
        csvwriter=csv.DictWriter(file,fieldnames=field)
        csvwriter.writeheader()
        file.close

def write_records():
    with open ("emplyees.csv","a",newline="")as file:
        csvWriter=csv.DictWriter(file,fieldnames=field)

        emp=dict()
        empid=int(input("enter your Employee Id: "))
        empname=(input("enter your Employee name: "))
        Gender=(input("enter your Employee gender: "))
        if Gender in ("Male","Female"):
            emp.update({"Gender":Gender})
        else:
            print("Invalid Gender")
        age=int(input("enter your Employee age: "))
        if age>=20 and age<55:
            emp.update({"age":age})
        else:
            print("Invalid Age")
        department=(input("enter your Employee department: "))
        if department in ("sales","logistics","Maketing","IT","Support","Devlopement"):
            emp.update({"department":department})
        else:
            print("Invalid department")
        role=(input("enter your Employee role: "))
        if role in ("software engineer","fron end devloper","Data analyst","back end devloper"):
            emp.update({"role":role})
        else:
            print("Invalid role")

        salary=(float(input("enter your salary")))
        if salary>=20000 and salary<=100000:
            emp.update({"salary":salary})
        else:
            print("Invalid salary")

        print(emp)
        csvWriter.writerow(emp)
        file.close


def display_records():
    with open ("employees.csv","r")as infile:
        csvreader=csv.DictReader(infile)
        records=list(csvreader)

        if len(records)==0:
            print("no records!")
        else:
            return records

def checkEmpid(id):
    found=False
    allrecord=display_records()
    for r in allrecord:
        if id==int(r["empid"]):
            print(r)
            found=True

    if found==False:
        print("no records found!")


create_file()
write_records()
display_records()
checkEmpid(120)


'''
#==============================================================================================================================


field = ["Empid", "Empname", "Gender", "Age", "Department", "Role", "Salary"]


def create_file():
    with open("employees.csv", "a", newline="") as file:
        csvwriter = csv.DictWriter(file, fieldnames=field)

        if file.tell() == 0:
            csvwriter.writeheader()


def write_records():
    with open("employees.csv", "a", newline="") as file:
        csvWriter = csv.DictWriter(file, fieldnames=field)

        emp = dict()

        empid = int(input("Enter your Employee Id: "))
        emp.update({"Empid": empid})

        empname = input("Enter your Employee name: ")
        emp.update({"Empname": empname})

        Gender = input("Enter your Employee gender: ")
        if Gender in ("Male", "Female"):
            emp.update({"Gender": Gender})
        else:
            print("Invalid Gender")
            return

        age = int(input("Enter your Employee age: "))
        if 20 <= age < 55:
            emp.update({"Age": age})
        else:
            print("Invalid Age")
            return

        department = input("Enter your Employee department: ")
        if department in ("sales", "logistics", "Marketing", "IT",
                          "Support", "Development"):
            emp.update({"Department": department})
        else:
            print("Invalid department")
            return

        role = input("Enter your Employee role: ")
        if role in ("software engineer", "front end developer",
                    "Data analyst", "back end developer"):
            emp.update({"Role": role})
        else:
            print("Invalid role")
            return

        salary = float(input("Enter your salary: "))
        if 20000 <= salary <= 100000:
            emp.update({"Salary": salary})
        else:
            print("Invalid salary")
            return

        print(emp)
        csvWriter.writerow(emp)


def display_records():
    with open("employees.csv", "r", newline="") as infile:
        csvreader = csv.DictReader(infile)
        records = list(csvreader)

        if len(records) == 0:
            print("No records!")
        else:
            return records


def checkEmpid(id):
    found = False
    allrecord = display_records()

    if allrecord is None:
        return

    for r in allrecord:
        if id == int(r["Empid"]):
            print(r)
            found = True

    if found == False:
        print("No records found!")


def display_ascending():
    record=display_records()
    temp=dict()
    for i in range(len(record)):
        for j in range(i+1,len(record)):
            if record[i]["empname"]>record[j]["empname"]:
                temp=record[i]
                record[i]=record[j]
                record[j]=temp

    for r in record:
        print(r)


def increment():
    records=display_records()
    for r in records:
        if r["department"]=="support":
            r["salary"]=float(r["salary"])+float(r["salary"])*0.2
            
            
            for r in records:
                print(r)






















create_file()
write_records()
display_records()
checkEmpid(120)


