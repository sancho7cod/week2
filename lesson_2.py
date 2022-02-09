#1. Вывести на экран все числа начиная с 0, пока сумма всех этих чисел не превысит 1000.

# i = 0
# b = 0
# num = [0]
# while b < 10:
#     i += 1
#     b += 1
#     num.append(i)
# print(num)
#dict - cловари dictionary
# new_dict = {"name": "Nazgul",
#             "y": 200
#             }
# print(new_dict["x"])

# new_dict = {"samat": {
#     "algebra": 80,
#     "biology": 90
#     }
# }
# print(new_dict["samat"]["algebra"])

# a = dict()
# a = {}
# print(type (a))

# a = dict([(10, 17), ("a", 1)])
# print(a)
#
# dicts = {
#     "a": 4,
#     "b": 7,
#     "c": 5,
# }
# print((len(dicts)))
# for i in dicts.values():
# for i in dicts.keys():

# for i, y in dicts.items():
#     print(i, y)

# subject = {
#     "algebra": 88,
#     "english": 81,
#     "biology": 90,
# }
# # print(subject.values())
# counter = 0
# for i in subject.values():
#     counter += i
#     # counter = counter + i
# print(counter / len(subject))
#  5! = 1*2*3*4*5
# b = 1
# a = int(input("введите число:"))
# for i in range(1, a + 1):
#     # a = a * i
# print(a)


# lists = [1, 2, 3]
# lists.pop(2)
# print(lists)

#
# subject = {
#     "algebra": 88,
#     "english": 81,
# #     "biology": 90,
# }
# a = subject.pop("algebra")
# print(a)
# print(subject)
# print(dir(subject))


# new_subject = {
#     "python": 100,
#     "java": 78,
# }
# subject.update(new_subject)
# subject.update({"geography": 63})
# print(subject)


# new = dict.fromkeys(["a", "s"], )
# print(new)

# lists = ["samat", "aktan", "baiel"]
# s = dict.fromkeys(lists, 50000)
# s["samat"] = 60000
# print(s)

# s = {1: 3, 4: 5}
# # a = s.get(8), 3
# print(s.setdefault(5))
# print(s)

#task

# n = {
#     "user1": {
#         "name": "User1",
#         "surname": "Usenov",
#         "age": 18,
#         "email": "user1@axsc"
#         },
#
#     "user2": {
#         "name": "User2",
#         "sername": "usenov11",
#         }
#     }
# # print(n.update("user2"))
# print(n.update({"user2": {"name": "user3"}}))
# print(n)
# print(n.setdefault("user3"))



# empoyees = {
#             1: {
#                 "name": "bek",
#                 "email": "test1@mail",
#                 "age": 18,
#                 "salary": 1200
#                 },
#             2: {
#                 "name": "uluk",
#                 "email": "test1@mail",
#                 "age": 19,
#                 "salary": 120
#                 },
#             3: {
#                 "name": "uli",
#                 "email": "test1@mail",
#                 "age": 34,
#                 "salary": 3211
#                 },
#             4: {
#                 "name": "uljan",
#                 "email": "test1@mail",
#                 "age": 25,
#                 "salary": 23400
#                 },
#             5: {
#                 "name": "ulish",
#                 "email": "test1@mail",
#                 "age": 26,
#                 "salary": 24990,
#                  }
# }
# # for i in empoyees:
# #     if empoyees[i]["age"] >= 20:
# #         print(empoyees[i])
# for i in empoyees:
#     if empoyees[i]["age"] < 20:
#         empoyees[i]["salary"] = 500
#     elif empoyees[i]["age"] > 20:
#         empoyees[i]["salary"] =200
# print(empoyees)