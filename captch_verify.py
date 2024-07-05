import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

class CaptchaVerifier:
    def __init__(self, root):
        self.root = root
        self.root.title("Random CAPTCHA Verification")
        self.root.geometry("400x200")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Verify you are human by entering the CAPTCHA below:", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.captcha_str = self.generate_captcha()
        self.captcha_label = tk.Label(root, text=self.captcha_str, font=("Arial", 16, "bold"), bg="#ffffff")
        self.captcha_label.pack(pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=("Arial", 12), width=20)
        self.entry.pack(pady=10)

        self.verify_button = tk.Button(root, text="Verify", font=("Arial", 12), bg="#4caf50", fg="#ffffff", command=self.verify_captcha)
        self.verify_button.pack(pady=10)

    def generate_captcha(self):
        captcha_chars = random.choices(string.ascii_letters + string.digits, k=6)
        return ''.join(captcha_chars)

    def verify_captcha(self):
        user_input = self.entry_var.get()
        if user_input.lower() == self.captcha_str.lower():
            messagebox.showinfo("Verification", "CAPTCHA verification successful.")
        else:
            messagebox.showerror("Verification Failed", "CAPTCHA verification failed. Please try again.")
            self.captcha_str = self.generate_captcha()
            self.captcha_label.config(text=self.captcha_str)
            self.entry_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaVerifier(root)
    root.mainloop()
