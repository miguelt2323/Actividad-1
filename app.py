from flask import Flask, render_template, request,redirect, url_for, flash
from database.conexion import obtener_conexion

app = Flask(__name__)
app.secret_key = "adso2026"

@app.route("/")
def inicio():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM productos
        ORDER BY codigo DESC
    """)

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("index.html", productos=productos)

@app.route("/productos")
def productos():
    conexion = obtener_conexion()

    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    cursor.close()

    conexion.close()

    return render_template("productos.html",productos=productos)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/registro_producto")
def registro_producto():
    return render_template("registro_producto.html")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    codigo = request.form["codigo"].strip()
    nombre = request.form["nombre"].strip()
    precio = request.form["precio"].strip()
    categoria = request.form["categoria"].strip()

    # ==========================
    # VALIDACIONES
    # ==========================

    # Campos obligatorios
    if not codigo or not nombre or not precio or not categoria:
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for("registro_producto"))

    # Longitud del código
    if len(codigo) > 20:
        flash("El código no puede tener más de 20 caracteres.", "error")
        return redirect(url_for("registro_producto"))

    # Longitud del nombre
    if len(nombre) > 80:
        flash("El nombre no puede tener más de 80 caracteres.", "error")
        return redirect(url_for("registro_producto"))

    # Longitud de la categoría
    if len(categoria) > 80:
        flash("La categoría no puede tener más de 80 caracteres.", "error")
        return redirect(url_for("registro_producto"))

    # Validar precio
    try:
        precio = float(precio)

        if precio <= 0:
            flash("El precio debe ser mayor que cero.", "error")
            return redirect(url_for("registro_producto"))

    except ValueError:
        flash("El precio debe ser un número válido.", "error")
        return redirect(url_for("registro_producto"))

    # Verificar si el código ya existe
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT codigo FROM productos WHERE codigo=%s",
        (codigo,)
    )

    existe = cursor.fetchone()

    if existe:
        cursor.close()
        conexion.close()
        flash("Ya existe un producto con ese código.", "error")
        return redirect(url_for("registro_producto"))

    # Guardar producto
    sql = """
        INSERT INTO productos
        (codigo, nombre, precio, categoria)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (codigo, nombre, precio, categoria))
    conexion.commit()

    cursor.close()
    conexion.close()

    flash("Producto registrado correctamente.", "success")
    return redirect(url_for("productos"))

@app.route("/editar_producto/<codigo>")
def editar_producto(codigo):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = """SELECT * FROM productos WHERE codigo=%s """

    cursor.execute(sql,(codigo,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template("editar_producto.html",producto=producto)

@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():

    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    # ==========================
    # VALIDACIONES
    # ==========================

    # Campos obligatorios
    if not codigo or not nombre or not precio or not categoria:
        flash("Todos los campos son obligatorios.", "error")
        return redirect(url_for("editar_producto", codigo=codigo))

    # Longitud del código
    if len(codigo) > 20:
        flash("El código no puede tener más de 20 caracteres.", "error")
        return redirect(url_for("editar_producto", codigo=codigo))

    # Longitud del nombre
    if len(nombre) > 80:
        flash("El nombre no puede tener más de 80 caracteres.", "error")
        return redirect(url_for("editar_producto", codigo=codigo))

    # Longitud de la categoría
    if len(categoria) > 80:
        flash("La categoría no puede tener más de 80 caracteres.", "error")
        return redirect(url_for("editar_producto", codigo=codigo))

    # Validar precio
    try:
        precio = float(precio)

        if precio <= 0:
            flash("El precio debe ser mayor que cero.", "error")
            return redirect(url_for("editar_producto", codigo=codigo))

    except ValueError:
        flash("El precio debe ser un número válido.", "error")
        return redirect(url_for("editar_producto", codigo=codigo))

    # Obtener la conexion
    conexion = obtener_conexion()

    # Crear el cursor
    cursor = conexion.cursor()

    # Consulta SQL
    sql = """UPDATE productos SET nombre = %s,precio = %s,categoria = %s WHERE codigo = %s """

    cursor.execute(sql,(nombre,precio,categoria,codigo))

    # Guardar los cambios
    conexion.commit()

    # Cerrar recursos
    cursor.close()
    conexion.close()

    # Mnesaje de éxito
    flash("Producto actualizado correctamente", "success")

    # Redireccionar al listado
    return redirect(url_for("productos"))

@app.route("/eliminar_producto/<codigo>")
def eliminar_producto(codigo):
    conexion = obtener_conexion()

    cursor = conexion.cursor()

    sql = """DELETE FROM productos WHERE codigo=%s"""
    cursor.execute(sql,(codigo,))

    conexion.commit()

    
    flash("Producto eliminado correctamente", "success")

    cursor.close()
    conexion.close()
    return redirect(url_for("productos"))

app.run(debug=True)

# TechStore/
# │
# ├── app.py
# │
# ├── templates/
# │   ├── index.html
# │   ├── registro_producto.html
# │   └── respuesta.html
# │
# └── static/