from user import User
from post import Post

app_user_one = User("nn@nn.com", "Dan Stagg", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

# update user one job title
app_user_one.change_job_title("Dev opps trainer")
app_user_one.get_user_info()

# new user
app_user_two = User("pp@nn.com", "Paul Knight", "pwd2", "Facilities")
app_user_two.get_user_info()

new_post = Post("on a secret mission today!,", app_user_two.name)
new_post.get_post_into()
