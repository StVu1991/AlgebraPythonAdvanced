class Person:
    def __init__(self, vat_id, email):
        self.vat_id = vat_id
        self.email = email

    def display(self):
        print("Not implemented")
       # print(f"Vat ID: {self.vat_id}\ne-mail: {self.email}")


class Company(Person):
    def __init__(self, name, customer_type, vat_id, email):
        super(Company, self).__init__(vat_id, email)
        self.name = name
        self.customer_type = customer_type

    def __str__(self):
        return f"Company: {self.name}\nType: {self.customer_type}"

    def display(self):
        print(f"Company: {self.name}\nType: {self.customer_type}")


class Employee(Person):
    def __init__(self, first_name, last_name, vat_id, email):
        super(Employee, self).__init__(vat_id, email)
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name}{self.last_name}"

    def display(self):
        print(f"Ime: {self.first_name}\nPrezime: {self.last_name}")


company = Company("Algebra", "Kupac", "01234456", "info@algebra.hr")
employee = Employee("Pero", "Peric", "342313311", "pero@peric.com")

#print(company.vat_id)
#print(company.email)
#print(employee.vat_id)
#print(employee.email)

#print(employee)
#print(company)

#company.display_company()
company.display()
#employee.display_employee()
employee.display()