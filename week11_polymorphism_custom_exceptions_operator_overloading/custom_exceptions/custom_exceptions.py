class DivisionByZeroError(Exception): # Custom exception class

    def __init__(self, message):
       super().__init__(message)
       self.__message = message # message goes to the parent, but we also store
                                # it as an attribute in the subclass to make
                                # it easier to access
    def get_message(self):
        return self.__message

    def __str__(self):
        return f"{self.__message}"
    
class NegativeRootError(Exception):
    def __init__(self, message, value):
       super().__init__(message)
       self.__message = message
       self.__value = value

    def __str__(self):
        return f"{self.__message}\nThe discriminant {self.__value} is not valid."