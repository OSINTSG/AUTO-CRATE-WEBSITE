import tkinter as tk
from tkinter import messagebox

class HTMLGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("HTML Generator")

        # Variables to store user inputs
        self.web_title = tk.StringVar()
        self.navbar_names = [tk.StringVar() for _ in range(5)]
        self.header_text = tk.StringVar()
        self.generate_css = tk.BooleanVar(value=False)

        # Frame for web title input
        self.web_title_frame = tk.Frame(master)
        self.web_title_frame.pack(pady=5)

        tk.Label(self.web_title_frame, text="Web Title:").pack(side=tk.LEFT)
        self.web_title_entry = tk.Entry(self.web_title_frame, textvariable=self.web_title)
        self.web_title_entry.pack(side=tk.LEFT)

        # Frames for navbar name inputs
        self.navbar_frames = []
        for i in range(5):
            navbar_frame = tk.Frame(master)
            navbar_frame.pack(pady=5)
            self.navbar_frames.append(navbar_frame)

            tk.Label(navbar_frame, text=f"Navbar {i+1} Name:").pack(side=tk.LEFT)
            self.navbar_entries = tk.Entry(navbar_frame, textvariable=self.navbar_names[i])
            self.navbar_entries.pack(side=tk.LEFT)

        # Frame for header text input
        self.header_frame = tk.Frame(master)
        self.header_frame.pack(pady=5)

        tk.Label(self.header_frame, text="Header Text:").pack(side=tk.LEFT)
        self.header_entry = tk.Entry(self.header_frame, textvariable=self.header_text)
        self.header_entry.pack(side=tk.LEFT)

        # Checkbox to generate CSS
        self.generate_css_checkbutton = tk.Checkbutton(master, text="Generate CSS", variable=self.generate_css)
        self.generate_css_checkbutton.pack(pady=5)

        # Button to generate HTML
        self.generate_button = tk.Button(master, text="Generate HTML", command=self.generate_html)
        self.generate_button.pack(pady=10)

        # Sign Up button
        self.signup_button = tk.Button(master, text="Sign Up", command=self.signup)
        self.signup_button.pack(side=tk.LEFT, padx=5)

        # Login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(side=tk.LEFT, padx=5)

    def generate_html(self):
        web_title = self.web_title.get()
        navbar_names = [name.get() for name in self.navbar_names]
        header_text = self.header_text.get()
        generate_css = self.generate_css.get()

        # Write HTML content to a file
        with open("index.html", "w") as file:
            file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                       <link rel="stylesheet" href="style.css">
    <title>{web_title}</title>
""")

            if generate_css:
                file.write("""
    <style>
        /* Your CSS Styles Here */
    </style>
""")

            file.write("""
</head>
<body>

<nav>
""")
            for name in navbar_names:
                file.write(f"    <div>{name}</div>\n")
            file.write("</nav>\n")

            file.write(f"""
<header>
    <h1>{header_text}</h1>
</header>

<!-- Add more HTML content here -->

</body>
</html>
""")
        messagebox.showinfo("Success", "HTML file generated successfully!")

    def signup(self):
        messagebox.showinfo("Sign Up", "Sign Up function called!")

    def login(self):
        messagebox.showinfo("Login", "Login function called!")

def main():
    root = tk.Tk()
    app = HTMLGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
