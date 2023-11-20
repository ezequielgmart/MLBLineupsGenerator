# import time

# original = list(range(1,1000001))
# aux = range(1,1000001, 2)

# start = time.time()

# new = [element for element in original if element not in aux]


# end = time.time()

# print(new)
# print(end-start)

import time

original = [
            {'power': 9.0, 'leadoff': 9.0, 'offroad': 7.0, 'fundamentals': 9.0, 'name': 'cody'},
            {'power': 8.0, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'mike'},
            {'power': 7.0, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'zack'},
            {'power': 5.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'jared'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'Randal'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'David'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'Randal'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'David'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 9.0, 'fundamentals': 9.0, 'name': 'shohei'}
]

aux = [
            {'power': 5.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'jared'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'Randal'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 8.0, 'fundamentals': 9.0, 'name': 'David'},
            {'power': 6.5, 'leadoff': 9.0, 'offroad': 9.0, 'fundamentals': 9.0, 'name': 'shohei'}
]

start = time.time()

new = [element for element in original if element not in aux]


end = time.time()

print(len(original))
print(len(new))
print(float(end-start))