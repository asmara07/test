class comment:
    def __init__(self,username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes
    def delete_comment(self):
        print(f"комментарий с текстом {self.text} удален")
class User:
    def __init__(self,username):
        self.user = username
user1 = User("Lily")
comment1 = comment("Lily", "omg")
comment2 = comment( "Lily", "how are you")
comment1.delete_comment()
comment2.delete_comment()
user1.delete_account()




