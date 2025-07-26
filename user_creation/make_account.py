import bisect
user_database = []

class CreateUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = []
    
    def add_to_database(self):
        '''Function for the CreateUser class, uses bisect module 
        to determine if username is taken, and adds it to sorted 
        user_database list'''

        result = bisect.bisect_left(user_database, [self.username, self.password, self.data]) #Find position it would be inserted
        if  result == len(user_database) or user_database[result][0] != self.username: #check if empty or end of list OR username doesn't exist already
            bisect.insort_left(user_database, [self.username, self.password, self.data])
        else: 
            return #need to add error throwing here

'''
FOR TESTING

User = CreateUser("kylynn", 90212)
User2 = CreateUser("someone", 90112)
User3 = CreateUser("ashakl", 89219384)

User.add_to_database()
User2.add_to_database()
User3.add_to_database()
'''
print(user_database)