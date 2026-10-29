class BalanceTooLowError(Exception):
    def __init__(self, message, balance, minimum):
        super().__init__(message)
        self.__message = message
        self.__balance = balance
        self.__minimum = minimum

    def __str__(self):
        output = f'{self.__message}\n' \
                 f'Balance ${self.__balance} is below the minimum required ${self.__minimum}'
        
        return output

def open_account(balance):
    if balance < 100:
        raise BalanceTooLowError('Balance Too Low', balance, 100)
    return "Account opened successfully"

try:
    open_account(75)
except BalanceTooLowError as be:
    print(be)
    print('Ask the user to try again') 