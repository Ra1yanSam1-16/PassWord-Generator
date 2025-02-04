import string
import secrets
import tkinter as tk
from tkinter import ttk

# Global variables to keep count of attempts
invalid_attempts = 0
MAX_INVALID_ATTEMPTS = 15

def generate_password():
    global invalid_attempts

    # Get the desired password length
    try:
        num = int(entry_length.get())
        if num < 1 or num > 20:
            invalid_attempts += 1
            if invalid_attempts >= MAX_INVALID_ATTEMPTS:
                root.destroy()  # Close the application
                return # Stop execution
            label_result.config(text="Password length must be between 1 and 20.", fg="red", font=("Arial", 12, "bold"))
            return
    except ValueError:
        invalid_attempts += 1
        if invalid_attempts >= MAX_INVALID_ATTEMPTS:
            root.destroy()  # Close the application
            return # Stop execution
        label_result.config(text="Please enter a valid NUMBER.", fg="red", font=("Arial", 12, "bold"))
        return

    # Define character pools based on user selection
    character_pools = []
    if lowercase_var.get():
        character_pools.extend(list(string.ascii_lowercase))
    if uppercase_var.get():
        character_pools.extend(list(string.ascii_uppercase))
    if digits_var.get():
        character_pools.extend(list(string.digits))
    if symbols_var.get():
        character_pools.extend(list(string.punctuation))

    if not character_pools:
        label_result.config(text="Select at least one character type.", fg="red", font=("Arial", 12, "bold"))
        invalid_attempts += 1
        if invalid_attempts >= MAX_INVALID_ATTEMPTS:
            root.destroy()  # Close the application
            return  # Stop execution
        return

    # Generate the password
    password = []
    while len(password) < num:
        password.append(secrets.choice(character_pools))

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    # Display the password in the output label
    label_result.config(text=f"Generated Password: {final_password}", fg="black")
    global generated_password
    generated_password = final_password

    # Enable the "Copy to Clipboard" button
    button_copy.config(state=tk.NORMAL)

def copy_to_clipboard():
    # Copy the generated password to the clipboard using tkinter
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()

    # Show a small notification instead of a messagebox
    label_notification.config(text="Copied!", fg="blue")
    root.after(2000, lambda: label_notification.config(text=""))  # Clear notification after 2 seconds

def copy_on_hover(event):
    # Copy the password when the user hovers over it
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()
    label_notification.config(text="Copied!", fg="blue", font=("Arial", 10))
    root.after(5000, lambda: label_notification.config(text=""))  # Clear notification after 5 seconds

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.resizable(False, False)

# Add widgets
label_title = tk.Label(root, text="Secure Password Generator", font=("Arial", 16))
label_title.pack(pady=10)

# Password length input
frame_length = tk.Frame(root)
frame_length.pack(pady=5)
label_length = tk.Label(frame_length, text="Password Length (1-20):")
label_length.pack(side=tk.LEFT)
entry_length = tk.Entry(frame_length, width=10)
entry_length.pack(side=tk.LEFT, padx=5)

# Character type selection
frame_options = tk.Frame(root)
frame_options.pack(pady=10)
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame_options, text="Lowercase", variable=lowercase_var).pack(anchor=tk.W)
tk.Checkbutton(frame_options, text="Uppercase", variable=uppercase_var).pack(anchor=tk.W)
tk.Checkbutton(frame_options, text="Digits", variable=digits_var).pack(anchor=tk.W)
tk.Checkbutton(frame_options, text="Symbols", variable=symbols_var).pack(anchor=tk.W)

# Generate button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12), wraplength=450, fg="green")
label_result.pack(pady=10)

# Hover-to-copy feature
label_result.bind("<Enter>", copy_on_hover)

# Copy to clipboard button
button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
button_copy.pack(pady=5)

# Notification label
label_notification = tk.Label(root, text="", font=("Arial", 10), fg="blue")
label_notification.pack(pady=5)

# Run the application
root.mainloop()