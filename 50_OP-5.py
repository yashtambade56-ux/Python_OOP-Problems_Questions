# Create a User class with private password and a method to validate login.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def validate_login(self, username, password):
        if self.username == username and self.__password == password:
            return True
        return False
    
# Example usage
user1 = User("rahul", "secure123")
print(user1.validate_login("rahul", "secure123"))  # Output: True
print(user1.validate_login("rahul", "wrongpass"))  # Output: False