import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

# Configuración de la conexión a MySQL (cambia según tu setup)
db_config = {
    'host': 'localhost:3306', 
    'user': 'root',  # Cambia a tu usuario
    'password': '123456',  # Cambia a tu contraseña
    'database': 'agenda_docentes'
}

# Función para conectar a la DB
def conectar_db():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a MySQL: {e}")
        return None

# Función para agregar curso
def agregar_curso():
    nombre = entry_curso.get()
    docente = entry_docente.get()
    if nombre and docente:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cursos (nombre_curso, docente) VALUES (%s, %s)", (nombre, docente))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Curso agregado.")
            cargar_cursos()
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")

# Función para cargar cursos en la lista
def cargar_cursos():
    lista_cursos.delete(0, tk.END)
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cursos")
        for row in cursor.fetchall():
            lista_cursos.insert(tk.END, f"ID: {row[0]} - {row[1]} (Docente: {row[2]})")
        conn.close()

# Función para agregar alumno
def agregar_alumno():
    nombre = entry_alumno_nom.get()
    apellido = entry_alumno_ape.get()
    curso_id = entry_alumno_curso.get()
    if nombre and apellido and curso_id:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO alumnos (nombre, apellido, curso_id) VALUES (%s, %s, %s)", (nombre, apellido, int(curso_id)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Alumno agregado.")
            cargar_alumnos()
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")

# Función para cargar alumnos
def cargar_alumnos():
    lista_alumnos.delete(0, tk.END)
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT a.id, a.nombre, a.apellido, c.nombre_curso FROM alumnos a JOIN cursos c ON a.curso_id = c.id")
        for row in cursor.fetchall():
            lista_alumnos.insert(tk.END, f"ID: {row[0]} - {row[1]} {row[2]} (Curso: {row[3]})")
        conn.close()

# Función para agregar asistencia
def agregar_asistencia():
    alumno_id = entry_asistencia_alum.get()
    fecha = entry_asistencia_fecha.get()
    presente = 1 if var_presente.get() else 0
    if alumno_id and fecha:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO asistencias (alumno_id, fecha, presente) VALUES (%s, %s, %s)", (int(alumno_id), fecha, presente))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Asistencia registrada.")
            cargar_asistencias()
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")

# Función para cargar asistencias
def cargar_asistencias():
    lista_asistencias.delete(0, tk.END)
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT a.id, al.nombre, al.apellido, a.fecha, a.presente FROM asistencias a JOIN alumnos al ON a.alumno_id = al.id")
        for row in cursor.fetchall():
            status = "Presente" if row[4] else "Ausente"
            lista_asistencias.insert(tk.END, f"ID: {row[0]} - {row[1]} {row[2]} ({row[3]}: {status})")
        conn.close()

# Función para agregar nota
def agregar_nota():
    alumno_id = entry_nota_alum.get()
    curso_id = entry_nota_curso.get()
    nota = entry_nota_valor.get()
    desc = entry_nota_desc.get()
    if alumno_id and curso_id and nota:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notas (alumno_id, curso_id, nota, descripcion) VALUES (%s, %s, %s, %s)", (int(alumno_id), int(curso_id), float(nota), desc))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Nota agregada.")
            cargar_notas()
    else:
        messagebox.showwarning("Advertencia", "Completa todos los campos.")

# Función para cargar notas
def cargar_notas():
    lista_notas.delete(0, tk.END)
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT n.id, al.nombre, al.apellido, c.nombre_curso, n.nota, n.descripcion FROM notas n JOIN alumnos al ON n.alumno_id = al.id JOIN cursos c ON n.curso_id = c.id")
        for row in cursor.fetchall():
            lista_notas.insert(tk.END, f"ID: {row[0]} - {row[1]} {row[2]} ({row[3]}): {row[4]} - {row[5] or 'Sin descripción'}")
        conn.close()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda de Docentes")
ventana.geometry("600x500")

# Crear pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill=tk.BOTH, expand=True)

# Pestaña Cursos
tab_cursos = ttk.Frame(notebook)
notebook.add(tab_cursos, text="Cursos")

tk.Label(tab_cursos, text="Nombre del Curso:").pack()
entry_curso = tk.Entry(tab_cursos)
entry_curso.pack()

tk.Label(tab_cursos, text="Docente:").pack()
entry_docente = tk.Entry(tab_cursos)
entry_docente.pack()

tk.Button(tab_cursos, text="Agregar Curso", command=agregar_curso).pack(pady=5)
lista_cursos = tk.Listbox(tab_cursos)
lista_cursos.pack(fill=tk.BOTH, expand=True)
cargar_cursos()

# Pestaña Alumnos
tab_alumnos = ttk.Frame(notebook)
notebook.add(tab_alumnos, text="Alumnos")

tk.Label(tab_alumnos, text="Nombre:").pack()
entry_alumno_nom = tk.Entry(tab_alumnos)
entry_alumno_nom.pack()

tk.Label(tab_alumnos, text="Apellido:").pack()
entry_alumno_ape = tk.Entry(tab_alumnos)
entry_alumno_ape.pack()

tk.Label(tab_alumnos, text="ID del Curso:").pack()
entry_alumno_curso = tk.Entry(tab_alumnos)
entry_alumno_curso.pack()

tk.Button(tab_alumnos, text="Agregar Alumno", command=agregar_alumno).pack(pady=5)
lista_alumnos = tk.Listbox(tab_alumnos)
lista_alumnos.pack(fill=tk.BOTH, expand=True)
cargar_alumnos()

# Pestaña Asistencias
tab_asistencias = ttk.Frame(notebook)
notebook.add(tab_asistencias, text="Asistencias")

tk.Label(tab_asistencias, text="ID del Alumno:").pack()
entry_asistencia_alum = tk.Entry(tab_asistencias)
entry_asistencia_alum.pack()

tk.Label(tab_asistencias, text="Fecha (YYYY-MM-DD):").pack()
entry_asistencia_fecha = tk.Entry(tab_asistencias)
entry_asistencia_fecha.pack()

var_presente = tk.BooleanVar()
tk.Checkbutton(tab_asistencias, text="Presente", variable=var_presente).pack()

tk.Button(tab_asistencias, text="Registrar Asistencia", command=agregar_asistencia).pack(pady=5)
lista_asistencias = tk.Listbox(tab_asistencias)
lista_asistencias.pack(fill=tk.BOTH, expand=True)
cargar_asistencias()

# Pestaña Notas
tab_notas = ttk.Frame(notebook)
notebook.add(tab_notas, text="Notas")

tk.Label(tab_notas, text="ID del Alumno:").pack()
entry_nota_alum = tk.Entry(tab_notas)
entry_nota_alum.pack()

tk.Label(tab_notas, text="ID del Curso:").pack()
entry_nota_curso = tk.Entry(tab_notas)
entry_nota_curso.pack()

tk.Label(tab_notas, text="Nota:").pack()
entry_nota_valor = tk.Entry(tab_notas)
entry_nota_valor.pack()

tk.Label(tab_notas, text="Descripción:").pack()
entry_nota_desc = tk.Entry(tab_notas)
entry_nota_desc.pack()

tk.Button(tab_notas, text="Agregar Nota", command=agregar_nota).pack(pady=5)
lista_notas = tk.Listbox(tab_notas)
lista_notas.pack(fill=tk.BOTH, expand=True)
cargar_notas()

# Ejecutar la app
ventana.mainloop()
