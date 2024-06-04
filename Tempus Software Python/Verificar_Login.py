import mysql.connector

try:
    # Configura los detalles de conexión
    db_config = {
        "host": "localhost",  # Cambia esto al host correcto
        "user": "root",
        "password": "",
        "database": "registro",
    }

    # Crea la conexión
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor() 
    
    usuario = input("Ingresa el Usuario: ")
    password = input("Ingresa la Clave: ")

    cursor.execute("SELECT * FROM usuarios WHERE Cuenta = %s AND Clave = %s", (usuario, password))
    resultado = cursor.fetchone()
    if resultado:
        print("EXCELENTE, ERES TODO UN CRACK")
        # Aquí puedes ejecutar consultas o realizar otras operaciones

        # Cierra la conexión
        conn.close()
    else:
        print("NO SON DATOS VÁLIDOS, AMIGO")

except mysql.connector.Error as e:
    print(f"Error de conexión: {e}")
