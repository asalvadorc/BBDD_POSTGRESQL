from fpdf import FPDF

class DQLPresentation(FPDF):
    def header(self):
        # Background Gradient (Simulated with rectangles for simplicity and reliability)
        self.set_fill_color(250, 128, 114) # Salmon
        self.rect(0, 0, 297, 210, 'F')
        
        # Subtle accent at the bottom
        self.set_fill_color(255, 99, 71) # Tomato
        self.rect(0, 190, 297, 20, 'F')

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f'Página {self.page_no()} | Curso de Bases de Datos - PostgreSQL DQL', 0, 0, 'C')

    def slide_title(self, title):
        self.set_font('helvetica', 'B', 40)
        self.set_text_color(255, 255, 255)
        self.set_y(80)
        self.cell(0, 20, title, 0, 1, 'C')
        self.set_fill_color(255, 255, 255)
        self.rect(73, 105, 150, 2, 'F')

    def section_title(self, title):
        self.set_font('helvetica', 'B', 32)
        self.set_text_color(255, 255, 255)
        self.set_y(20)
        self.cell(0, 15, title, 0, 1, 'L')
        self.ln(10)

    def slide_content(self, content_list):
        self.set_font('helvetica', '', 18)
        self.set_text_color(255, 255, 255)
        self.set_x(20)
        for item in content_list:
            # Bullet point
            self.set_font('helvetica', 'B', 18)
            self.cell(10, 10, chr(149), 0, 0)
            self.set_font('helvetica', '', 18)
            self.multi_cell(0, 10, item)
            self.ln(5)

    def slide_code(self, code_text):
        self.set_fill_color(50, 50, 50)
        self.set_text_color(0, 255, 0) # Green code
        self.set_font('courier', 'B', 14)
        self.set_x(30)
        self.multi_cell(237, 10, code_text, fill=True, border=1)
        self.ln(10)

def create_presentation():
    pdf = DQLPresentation(orientation='L', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)

    # Slide 1: Title
    pdf.add_page()
    pdf.slide_title("PostgreSQL DQL")
    pdf.set_font('helvetica', '', 20)
    pdf.set_y(120)
    pdf.cell(0, 10, "Consultas y Filtrado de Datos", 0, 1, 'C')

    # Slide 2: What is DQL?
    pdf.add_page()
    pdf.section_title("¿Qué es DQL?")
    pdf.slide_content([
        "Data Query Language: El lenguaje para realizar peticiones a la Base de Datos.",
        "La instrucción central es SELECT.",
        "Es el alma de SQL: nos permite extraer, filtrar y transformar información.",
        "Crucial para reportes, análisis de datos y apps interactivas."
    ])

    # Slide 3: Basic Syntax
    pdf.add_page()
    pdf.section_title("Sintaxis Básica")
    pdf.slide_content([
        "SELECT: Define qué campos queremos.",
        "FROM: Indica la tabla de origen.",
        "Alias (AS): Renombra columnas o tablas para mayor legibilidad."
    ])
    pdf.slide_code("SELECT nombre, precio AS coste\nFROM articulos;")

    # Slide 4: Filtering with WHERE
    pdf.add_page()
    pdf.section_title("Filtrado con WHERE")
    pdf.slide_content([
        "Establece condiciones para las filas.",
        "Operadores de comparación: =, <, >, <=, >=, <>, !=.",
        "LIKE: Para patrones de texto (% para muchos caracteres, _ para uno).",
        "BETWEEN: Para rangos inclusivos.",
        "IN: Para listas de valores."
    ])
    pdf.slide_code("SELECT *\nFROM clientes\nWHERE ciudad = 'Castellón' AND edad > 18;")

    # Slide 5: Logic and Nulls
    pdf.add_page()
    pdf.section_title("Lógica y Nulos")
    pdf.slide_content([
        "AND, OR, NOT: Para combinar condiciones.",
        "NULL: Representa la ausencia de valor.",
        "Tratamiento especial: IS NULL e IS NOT NULL.",
        "¡OJO! ciudad = NULL nunca será cierto."
    ])
    pdf.slide_code("SELECT *\nFROM facturas\nWHERE descuento IS NOT NULL;")

    # Slide 6: Ordering and Limits
    pdf.add_page()
    pdf.section_title("Ordenación y Límites")
    pdf.slide_content([
        "ORDER BY: Ordena por uno o más campos (ASC / DESC).",
        "LIMIT: Restringe el número de filas devueltas.",
        "OFFSET: Salta un número determinado de filas iniciales."
    ])
    pdf.slide_code("SELECT *\nFROM productos\nORDER BY precio DESC\nLIMIT 10;")

    # Slide 7: Aggregation Functions
    pdf.add_page()
    pdf.section_title("Funciones de Agregado")
    pdf.slide_content([
        "Operan sobre un conjunto de filas devolviendo un único valor.",
        "COUNT(*): Cuenta filas.",
        "SUM(col), AVG(col): Suma y media.",
        "MAX(col), MIN(col): Valores extremos."
    ])
    pdf.slide_code("SELECT COUNT(*), AVG(precio)\nFROM articulos;")

    # Slide 8: Grouping
    pdf.add_page()
    pdf.section_title("GROUP BY y HAVING")
    pdf.slide_content([
        "GROUP BY: Agrupa filas con valores iguales en columnas específicas.",
        "HAVING: Filtra el resultado de las agrupaciones (similar a WHERE pero para grupos).",
        "Regla de oro: Todo lo que no esté en una función de agregado debe ir en el GROUP BY."
    ])
    pdf.slide_code("SELECT categoria, SUM(stock)\nFROM articulos\nGROUP BY categoria\nHAVING SUM(stock) > 100;")

    # Slide 9: Joins (Combinación)
    pdf.add_page()
    pdf.section_title("Combinación de Tablas (JOINs)")
    pdf.slide_content([
        "Permiten unir datos de múltiples tablas relacionadas.",
        "INNER JOIN: Filas con coincidencia en ambas tablas.",
        "LEFT JOIN: Todas las de la izquierda + coincidencias de la derecha.",
        "RIGHT JOIN: Todas las de la derecha + coincidencias de la izquierda."
    ])
    pdf.slide_code("SELECT P.nombre, I.nombre\nFROM POBLACIONES P\nINNER JOIN INSTITUTOS I ON P.cod_m = I.cod_m;")

    # Slide 10: Subqueries
    pdf.add_page()
    pdf.section_title("Subconsultas")
    pdf.slide_content([
        "Una consulta dentro de otra.",
        "Pueden ir en el FROM (como tabla temporal), WHERE (filtro dinámico) o SELECT.",
        "Predicados útiles: IN, EXISTS, ALL, ANY.",
        "Permiten resolver problemas complejos en un solo paso."
    ])
    pdf.slide_code("SELECT *\nFROM articulos\nWHERE precio > (SELECT AVG(precio) FROM articulos);")

    # Slide 11: Best Practices
    pdf.add_page()
    pdf.section_title("Mejores Prácticas")
    pdf.slide_content([
        "Usa mayúsculas para las palabras clave (SELECT, FROM...) para legibilidad.",
        "Usa Alias descriptivos.",
        "Evita el Producto Cartesiano (siempre combina con ON o WHERE).",
        "Formatea tus consultas para facilitar el mantenimiento."
    ])
    
    output_path = "c:/Antigravity/BBDD_POSTGRES_DQL_ES/docs/PostgreSQL_DQL_Presentation.pdf"
    pdf.output(output_path)
    print(f"Presentación generada en: {output_path}")

if __name__ == "__main__":
    create_presentation()
