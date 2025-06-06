import sqlite3


class BaseDeDatos:
    url_base_de_datos = 'postgres://mfqmsfrbpxqmfx:25f62f09b8a73ed69b0a7467522e4d62d423a5fe2dfa5bd8484d326e7e92e160@ec2-44-193-188-118.compute-1.amazonaws.com:5432/dhoijfehi423o'

    def _crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDeDatos.url_base_de_datos)
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        self.conexion.commit()
        self._cerrar_conexion()

        return filas
