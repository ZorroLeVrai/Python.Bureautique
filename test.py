class MyClass:
    def __init__(self):
        self.public_variable = "I am public"
        self._protected_variable = "I am protected"
        self.__private_variable = "I am private"

    # Public method
    def public_method(self):
        print("This is a public method")

    # Protected method
    def _protected_method(self):
        print("This is a protected method")

    # Private method
    def __private_method(self):
        print("This is a private method")

    # Method to access private method
    def access_private_method(self):
        self.__private_method()


# Creating an instance of the class
obj = MyClass()

# Accessing public variable
print(obj.public_variable)

# Accessing protected variable
print(obj._protected_variable)

# Trying to access private variable directly raises an error
# print(obj.__private_variable)  # This will raise an AttributeError

# Accessing public method
obj.public_method()

# Accessing protected method
obj._protected_method()

# Trying to access private method directly raises an error
# obj.__private_method()  # This will raise an AttributeError

# Accessing private method via a public method
obj.access_private_method()
