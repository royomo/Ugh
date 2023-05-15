import tkinter as tk
from tkinter import messagebox
from tkinter import END

root= tk.Tk()

# Set the window size and title
root.geometry("500x500")
root.title("Moats Inc - Invoice Dash")

# Set the background image
bg_image = tk.PhotoImage(file="C:\\Users\\roshe\\Hello_World\\Project\\pltp5ptug02ov9qqsqju82sfro.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

class LoginWindow(tk.Toplevel):
    def __init__(self, root, bg_image, admin_username, admin_password, nonadmin_username, nonadmin_password):
        super().__init__(root)
        self.geometry("500x500")
        self.title("Login")

        # Set the background image for the login window
        self.bg_label = tk.Label(self, image=bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add some widgets to the login window
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.check_login)
        self.login_button.pack(pady=10)

        # Save the admin and non-admin usernames and passwords
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.nonadmin_username = nonadmin_username
        self.nonadmin_password = nonadmin_password

    def check_login(self):
        # Get the username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct
        if username == self.admin_username and password == self.admin_password:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.destroy()
        elif username == self.nonadmin_username and password == self.nonadmin_password:
            messagebox.showinfo("Login Successful", "Welcome, Non-Admin!")
            self.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            self.password_entry.delete(0, END)

login_window = LoginWindow(root, bg_image, "admin", "adminpassword", "user", "userpassword")



