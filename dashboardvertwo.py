import tkinter as tk
import json
import os

DATA_FILE = "projects.json"

# ── Load data from file, or use defaults ─────────────────────────
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return [
        {"name": "Python",    "last": "Functions",  "next": "Learn if statements"},
        {"name": "Tool Cart", "last": "Top shelf",  "next": "Fit left drawer runners"}
    ]

# ── Save data to file ────────────────────────────────────────────
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(projects, f, indent=2)

# ── Open an edit window for one project ──────────────────────────
def open_edit_window(project, last_var, next_var):
    edit_win = tk.Toplevel(root)
    edit_win.title(f"Edit {project['name']}")
    edit_win.geometry("460x400")
    edit_win.config(bg="Blue")  # Blue background

    tk.Label(edit_win, text="Last completed:").pack(pady=(12, 0))
    last_entry = tk.Entry(edit_win, width=42)
    last_entry.insert(0, project["last"])
    last_entry.pack()

    tk.Label(edit_win, text="Next:").pack(pady=(10, 0))
    next_entry = tk.Entry(edit_win, width=42)
    next_entry.insert(0, project["next"])
    next_entry.pack()

    def apply_changes():
        project["last"] = last_entry.get()
        project["next"] = next_entry.get()
        last_var.set(f"Last completed:  {project['last']}")
        next_var.set(f"Next:  {project['next']}")
        edit_win.destroy()

    tk.Button(edit_win, text="Apply", command=apply_changes).pack(pady=12)

# ── Build the main window ────────────────────────────────────────
projects = load_data()
root = tk.Tk()
root.title("My Project Dashboard")
root.geometry("620x600")
root.config(bg="Light Blue")  # Light blue background

tk.Label(root, text="CURRENT PROJECTS", font=("Arial", 26, "bold"), fg="Purple", bg="Light Blue").pack(pady=15)

for i, project in enumerate(projects):
    last_var = tk.StringVar(value=f"Last completed:  {project['last']}")
    next_var = tk.StringVar(value=f"Next:  {project['next']}")

    tk.Label(root, text=project["name"], font=("Arial", 16, "bold"), fg="Black", bg="Green").pack()
    tk.Label(root, textvariable=last_var, fg="black").pack()
    tk.Label(root, textvariable=next_var, fg="black").pack()

    tk.Button(
        root,
        text=f"Edit {project['name']}",
        command=lambda p=project, lv=last_var, nv=next_var:
            open_edit_window(p, lv, nv)
    ).pack(pady=4)

    if i < len(projects) - 1:
        tk.Frame(root, height=2, bg="yellow").pack(fill="x", padx=20, pady=10)

# ── Save button ──────────────────────────────────────────────────
def save_and_confirm():
    save_data()
    save_btn.config(text="Saved! ✓")
    root.after(4000, lambda: save_btn.config(text="Save"))

save_btn = tk.Button(
    root, text="Save", command=save_and_confirm,
    bg="#4CAF50", fg="white", font=("Arial", 14, "bold")
)
save_btn.pack(pady=18)

root.mainloop()
