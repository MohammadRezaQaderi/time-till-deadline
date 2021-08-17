
class User:

    # The __init__ is like a constructor function do
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # change the password
    def change_password(self, new_password):
        self.password = new_password

    # change the Job title
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def user_get_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}. you can access him at {self.email}")


