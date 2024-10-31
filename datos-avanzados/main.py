alumnos = []

datos_alumnos = [
    {
        "nombre": "Juan", 
        "apellido": "Pérez",
        "edad": 18, 
        "curso": ("Matemáticas",)
    },
    {
        "nombre": "Ana", 
        "apellido": "García", 
        "edad": 19, 
        "curso": ("Física",)
    },
    {
        "nombre": "Luis", 
        "apellido": "Martínez", 
        "edad": 20, 
        "curso": ("Química",)
    },
    {
        "nombre": "Marta", 
        "apellido": "Sánchez", 
        "edad": 21, 
        "curso": ("Biología",)
    },
]

cursos = []

datos_cursos = [
    {("2023", "A"): {"cantidad_alumnos": 30, "preceptor": "Sra. López"}},
    {("2023", "B"): {"cantidad_alumnos": 28, "preceptor": "Sr. García"}},
    {("2023", "C"): {"cantidad_alumnos": 26, "preceptor": "Sra. Méndez"}},
    {("2023", "D"): {"cantidad_alumnos": 29, "preceptor": "Sr. Díaz"}},

    {("2024", "A"): {"cantidad_alumnos": 25, "preceptor": "Sra. Martínez"}},
    {("2024", "B"): {"cantidad_alumnos": 32, "preceptor": "Sr. Pérez"}},
    {("2024", "C"): {"cantidad_alumnos": 27, "preceptor": "Sra. Herrera"}},
    {("2024", "D"): {"cantidad_alumnos": 31, "preceptor": "Sr. Blanco"}},

    {("2025", "A"): {"cantidad_alumnos": 24, "preceptor": "Sra. López"}},
    {("2025", "B"): {"cantidad_alumnos": 29, "preceptor": "Sr. Díaz"}},
    {("2025", "C"): {"cantidad_alumnos": 28, "preceptor": "Sra. Méndez"}},
    {("2025", "D"): {"cantidad_alumnos": 30, "preceptor": "Sra. Herrera"}},

    {("2026", "A"): {"cantidad_alumnos": 33, "preceptor": "Sr. García"}},
    {("2026", "B"): {"cantidad_alumnos": 26, "preceptor": "Sra. Martínez"}},
    {("2026", "C"): {"cantidad_alumnos": 27, "preceptor": "Sr. Pérez"}},
    {("2026", "D"): {"cantidad_alumnos": 25, "preceptor": "Sra. Herrera"}},

    {("2027", "A"): {"cantidad_alumnos": 28, "preceptor": "Sra. López"}},
    {("2027", "B"): {"cantidad_alumnos": 30, "preceptor": "Sr. Blanco"}},
    {("2027", "C"): {"cantidad_alumnos": 31, "preceptor": "Sr. García"}},
    {("2027", "D"): {"cantidad_alumnos": 29, "preceptor": "Sra. Méndez"}},

    {("2028", "A"): {"cantidad_alumnos": 26, "preceptor": "Sra. Herrera"}},
    {("2028", "B"): {"cantidad_alumnos": 32, "preceptor": "Sr. Díaz"}},
    {("2028", "C"): {"cantidad_alumnos": 28, "preceptor": "Sra. López"}},
    {("2028", "D"): {"cantidad_alumnos": 27, "preceptor": "Sr. Pérez"}}
]

un_set = set()
lista_preseptores = set()

for clase in datos_cursos:
    for (clave, valor) in clase.items():
        lista_preseptores.add(valor['preceptor'])
    
print(lista_preseptores)
