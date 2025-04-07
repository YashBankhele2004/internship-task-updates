import tkinter as tk
from tkinter import messagebox
from db_connector import get_connection

def submit():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    course = course_entry.get()

    if not name or not age or not email or not course:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, email, course) VALUES (%s, %s, %s, %s)",
                       (name, age, email, course))
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Student Registered Successfully!")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Student Registration")

# Form Labels and Entries
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Age").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Course").pack(pady=5)
course_entry = tk.Entry(root)
course_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()
