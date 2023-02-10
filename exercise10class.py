
# Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.
#
# emp = Employee(1, "coder")
# Use del property to first delete id attribute and then the entire object
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

emp = Employee(1, "coder")

# Delete the id attribute
del emp.id

# Verify that the id attribute has been deleted
try:
    print(emp.id)
except AttributeError as e:
    print("AttributeError:", e)

# Delete the entire object
del emp

# Verify that the object has been deleted
try:
    print(emp)
except NameError as e:
    print("NameError:", e)