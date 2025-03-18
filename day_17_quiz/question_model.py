class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User("001", "ExaltGod")

user_2 = User("002", "Faith")

user_1.follow(user_1)
user_2.follow(user_1)

print(user_1)



class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer