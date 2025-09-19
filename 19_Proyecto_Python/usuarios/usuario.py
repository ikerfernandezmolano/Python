import mysql.connector as mysql

conexion = mysql.connect(host = "localhost", user = "root", passwd = "", database = "proyecto", port = "3306")
cursor = conexion.cursor()

class Usuario:
    _nombre: str
    _apellidos: str
    _email: str
    _passwd: str

    def __init__(self, pNombre: str, pApels: str, pEmail: str, pPasswd: str):
        self._nombre = pNombre
        self._apellidos = pApels
        self._email = pEmail
        self._passwd = pPasswd

    def registro(self):
        cursor.execute("INSERT INTO USUARIOS VALUES(null,%s,%s,%s,%s,null)",
                       self._nombre,self._apellidos,self._email,self._passwd)
        conexion.commit()
        return [cursor.rowcount, self]

    def identificar(self, pEmail: str, pPasswd: str):
        cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE EMAIL=%s",pEmail)
        comp = cursor.fetchall()
        if comp > 0 :
            cursor.execute("SELECT COUNT(*) FROM USUARIOS WHERE EMAIL=%s AND PASSWORD=%s",(pEmail,pPasswd))
            comp = cursor.fetchall()
            if comp > 0 :
                print(f"Usuario identificado correctamente.")
        else:
            raise NameError("Este correo no existe.")
        