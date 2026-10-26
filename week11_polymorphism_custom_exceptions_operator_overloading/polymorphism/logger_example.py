# This example has two classes defined in it FileLogger and NetworkLogger
# NOTE: When no __init__() method is supplied a default one is created when
# the code is compile. The default one simply instantiates the class without
# any data fields created.
#
# NO the classes do not have to be in the same file for polymorphism to work.

class FileLogger:
    def write(self, message):
        print("Writing to file:", message)

class NetworkLogger:
    def write(self, message):
        print("Sending over network:", message)

def main(): 

    file_logger1 = FileLogger()
    nw_logger1 = NetworkLogger()

    log(file_logger1)
    log(nw_logger1)

def log(writer):
    writer.write("System started")

if __name__ == '__main__':
    main()