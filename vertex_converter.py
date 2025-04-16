import tkinter as tk
from tkinter import messagebox

def convert_eye(sphere, cylinder, vertex_mm):
    vertex_m = vertex_mm / 1000  # mm -> meters
    spherical_equiv = sphere + (cylinder / 2)
    contact_lens_power = spherical_equiv / (1 - (vertex_m * spherical_equiv))
    return spherical_equiv, contact_lens_power

def convert_prescription():
    try:
        # OD
        sphere_od = float(entry_sphere_od.get())
        cylinder_od = float(entry_cylinder_od.get())
        vertex_od = float(entry_vertex_od.get())

        # OS
        sphere_os = float(entry_sphere_os.get())
        cylinder_os = float(entry_cylinder_os.get())
        vertex_os = float(entry_vertex_os.get())

        # Υπολογισμοί
        se_od, cl_od = convert_eye(sphere_od, cylinder_od, vertex_od)
        se_os, cl_os = convert_eye(sphere_os, cylinder_os, vertex_os)

        result_text = (
            f"🔵 ΔΕΞΙ ΜΑΤΙ (OD):\n"
            f"Σφαιρικό Ισοδύναμο: {se_od:+.2f} D\n"
            f"Φακός Επαφής (Vertex {vertex_od}mm): {cl_od:+.2f} D\n\n"
            f"🟠 ΑΡΙΣΤΕΡΟ ΜΑΤΙ (OS):\n"
            f"Σφαιρικό Ισοδύναμο: {se_os:+.2f} D\n"
            f"Φακός Επαφής (Vertex {vertex_os}mm): {cl_os:+.2f} D"
        )

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Σφάλμα", "Παρακαλώ εισάγετε έγκυρους αριθμούς και για τα δύο μάτια.")

# GUI
root = tk.Tk()
root.title("Μετατροπή Συνταγής Γυαλιών σε Φακούς Επαφής")

# Δεξί μάτι (OD)
tk.Label(root, text="🔵 ΔΕΞΙ ΜΑΤΙ (OD)").grid(row=0, column=0, columnspan=2, pady=(10, 0))
tk.Label(root, text="Sphere:").grid(row=1, column=0)
entry_sphere_od = tk.Entry(root)
entry_sphere_od.grid(row=1, column=1)

tk.Label(root, text="Cylinder:").grid(row=2, column=0)
entry_cylinder_od = tk.Entry(root)
entry_cylinder_od.grid(row=2, column=1)

tk.Label(root, text="Vertex (mm):").grid(row=3, column=0)
entry_vertex_od = tk.Entry(root)
entry_vertex_od.insert(0, "12")
entry_vertex_od.grid(row=3, column=1)

# Αριστερό μάτι (OS)
tk.Label(root, text="🟠 ΑΡΙΣΤΕΡΟ ΜΑΤΙ (OS)").grid(row=4, column=0, columnspan=2, pady=(15, 0))
tk.Label(root, text="Sphere:").grid(row=5, column=0)
entry_sphere_os = tk.Entry(root)
entry_sphere_os.grid(row=5, column=1)

tk.Label(root, text="Cylinder:").grid(row=6, column=0)
entry_cylinder_os = tk.Entry(root)
entry_cylinder_os.grid(row=6, column=1)

tk.Label(root, text="Vertex (mm):").grid(row=7, column=0)
entry_vertex_os = tk.Entry(root)
entry_vertex_os.insert(0, "12")
entry_vertex_os.grid(row=7, column=1)

# Κουμπί Μετατροπής
tk.Button(root, text="Μετατροπή", command=convert_prescription).grid(row=8, column=0, columnspan=2, pady=15)

# Εμφάνιση αποτελεσμάτων
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), justify="left")
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
