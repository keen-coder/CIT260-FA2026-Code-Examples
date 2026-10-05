import pickle

FILE_PATH = 'week08_sets_object_io_oop_i/object_serialization/data_files/'

# Serializing a dictionary and writing to a file ==============================

# A dictionary
populations = {'New York': 8398748, 'Los Angeles': 3990456,
               'Chicago': 2705994, 'Houston': 2325502, 
               'Phoenix': 1660272, 'Philadelphia': 1584138}

# Open a file in BINARY MODE to write our object to:
with open(FILE_PATH + 'populations.bin', 'wb') as out_file:
    pickle.dump(populations, out_file)

# Complex / nested dictionaries can be 'pickled'

customers = {    
    "John": {"age": 39, "address": "123 Main St", "email": "john@example.com"},    
    "Mary": {"age": 19, "address": "678 First St", "email": "jane@example.com"}
}

with open(FILE_PATH + 'customers.bin', 'wb') as out_file:
    pickle.dump(customers, out_file)

# You can write multiple objects to the same file.
populations = {'New York': 8398748, 'Los Angeles': 3990456,
               'Chicago': 2705994, 'Houston': 2325502, 
               'Phoenix': 1660272, 'Philadelphia': 1584138}

customers = {    
    "John": {"age": 39, "address": "123 Main St", "email": "john@example.com"},    
    "Mary": {"age": 19, "address": "678 First St", "email": "jane@example.com"}
}

with open(FILE_PATH + 'combined.bin', 'wb') as out_file:
    pickle.dump(populations, out_file)
    pickle.dump(customers, out_file)
#==============================================================================