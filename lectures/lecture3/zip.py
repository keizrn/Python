users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 6, 9, 14]
salary_2 = [111, 222, 333, "", ""]

data_1 = list(zip(users, ids, salary_2))
print(data_1)
print(list(enumerate(users)))