# try:
#     file = open("./day_30/a_file.txt")
#     print("Very good")
#     data = {"key": "data"}
#     print(data["val"])
# # except FileNotFoundError:
# #     file = open("./day_30/a_file.txt", "w")
# #     file.write("Something")
# except:
#     print(f"The key  doesnt exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")



# weight = float(input("What is your weight: "))
# height = int(input("What is your height: "))

# if height > 3:
#     raise ValueError("Human height is not over 3m")
# bmi = weight / height**2

# print(bmi)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
        total_likes = 0
        for post in posts:
            try:
                total_likes = total_likes + post['Likes']
            
        
            except KeyError:
                 pass
        return total_likes

print(count_likes(facebook_posts))

