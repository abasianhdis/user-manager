import tkinter as tk
from model import UserModel
from view import LoginView, AdminView

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = UserModel()
        self.login_view = LoginView(master=root, controller=self)
        self.admin_view = None

    def login(self, username, password):
        if self.model.validate_user(username, password):
            self.show_admin_view()
        else:
            tk.messagebox.showerror("Login Failed", "Invalid username or password")

    def show_admin_view(self):
        self.login_view.pack_forget()
        self.admin_view = AdminView(master=self.root, controller=self)
        self.update_user_list()

    def logout(self):
        self.admin_view.pack_forget()
        self.login_view.pack()

    def add_user(self, username, password):
        if self.model.add_user(username, password):
            self.update_user_list()
        else:
            tk.messagebox.showerror("Add User Failed", "User already exists")

    def remove_user(self, username):
        if self.model.remove_user(username):
            self.update_user_list()
        else:
            tk.messagebox.showerror("Remove User Failed", "User does not exist")

    def update_user_list(self):
        users = self.model.get_users()
        self.admin_view.update_user_list(users)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("User Management System")
    app = Controller(root)
    root.mainloop()
