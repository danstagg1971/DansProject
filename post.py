class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_into(self):
        print(f"Post {self.message} written by {self.author}")
