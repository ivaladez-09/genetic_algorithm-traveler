import time

solution_type = 'NP'

if solution_type == 'OOP':
    from oop.services import TravelerServices

elif solution_type == 'NP':
    from np.services import TravelerServices


POPULATION_SIZE = 200
GENERATIONS = 80
COORDINATES = [(1, 7), (2, 5), (4, 4), (2, 3), (3, 2),
                (1, 1), (5, 1), (7, 3), (6, 6), (10, 5),
                (9, 8), (13, 6), (12, 3), (13, 1)]

if __name__ == '__main__':
    t1 = time.time()
    traveler = TravelerServices(POPULATION_SIZE, COORDINATES)
    traveler.run(GENERATIONS)
    print(time.time() - t1)
    # print(traveler.aptitude_function_history)
