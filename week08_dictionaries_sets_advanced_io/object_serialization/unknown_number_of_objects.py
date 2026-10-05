import pickle

FILE_PATH = 'week08_sets_object_io_oop_i/object_serialization/data_files/'

# Pickleing 4 different dictionaries
store_a = {"Apples": 30, "Bananas": 45, "Oranges": 20}
store_b = { "Bananas": 50, "Grapes": 25, "Peaches": 15}
movie_ratings = {"Inception": 8.8, "The Matrix": 8.7, 
                 "Interstellar": 8.6, "The Prestige": 8.5}
product_catalog = {101: "Laptop", 102: "Smartphone", 103: "Tablet",
                   104: "Monitor", 105: "Keyboard"}

with open(FILE_PATH + 'unknown.bin', 'wb') as out_file:
    pickle.dump(store_a, out_file)
    pickle.dump(store_b, out_file)
    pickle.dump(movie_ratings, out_file)
    pickle.dump(product_catalog, out_file)


# Reading back an unknown number of pickled items into a list.
dictionary_list = []

with open(FILE_PATH + 'unknown.bin', 'rb') as in_file:
    end_of_file = False

    while not end_of_file:
        try:
            dictionary_list.append(pickle.load(in_file))
        except EOFError as err:
            print('Reached the end of file.')
            end_of_file = True

print(dictionary_list)