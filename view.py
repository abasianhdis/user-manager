import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)

class AdminView(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.users_label = tk.Label(self, text="Users")
        self.users_label.pack()
        self.users_listbox = tk.Listbox(self)
        self.users_listbox.pack()

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        self.add_user_button.pack()

        self.remove_user_button = tk.Button(self, text="Remove User", command=self.remove_user)
        self.remove_user_button.pack()

        self.logout_button = tk.Button(self, text="Logout", command=self.controller.logout)
        self.logout_button.pack()

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.add_user(username, password)

    def remove_user(self):
        selected_user = self.users_listbox.get(tk.ACTIVE)
        self.controller.remove_user(selected_user)

    def update_user_list(self, users):
        self.users_listbox.delete(0, tk.END)
        for user in users:
            self.users_listbox.insert(tk.END, user)
