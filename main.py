# def test_jackpot(list):
#     for i in range(len(list)):
#         for j in range(i +1, len(list)):
#             if list[i] in list[j]:
#                 return True
#             else:
#                 return False
#
# print(test_jackpot(["@", "@", "@", "@"]))
# print(test_jackpot(["&&", "&", "&&&", "&&&&"]) )
#######################################################
# def arrayValuesTypes(arr):
#     valuesTypes = []
#     for i in range(len(arr)):
#         valuesTypes.append(type(arr[i]))
#     return valuesTypes
#
# print(arrayValuesTypes([1, 2, "null", []]))
######################################################
#
# class Country:
#     def __init__(self, country, population, area):
#         self.country = country
#         self.population = population
#         self.area = area
#
#         while(self.population > 250000000 or self.area > 3000000):
#             self.is_big = True
#
#     def compare_pd(self, country2):
#         if self.population/self.area > country2.population/country2.area:
#             print(f'{self.country} has a  larger population density than {country2.country}')
#         else:
#             print(f'{self.country} has a  smaller population density than {country2.country}')
#
# australia = Country('Australia', 23545500, 7692024)
# andorra = Country('Andorra', 76098, 468)
#
# andorra.compare_pd(australia)

#######################################################
# def sortByLength(arr):
#     arr.sort(key=len)
#     return arr
# print(sortByLength(["Google", "Apple", "Microsoft"]))
# print(sortByLength(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
# print(sortByLength(["Turing", "Einstein", "Jung"]))

