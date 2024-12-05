class Usuario:
    def __init__(self, idUsuario, nombreUsuario, correo, contraseña):
        self.idUsuario = idUsuario
        self.nombreUsuario = nombreUsuario
        self.correo = correo
        self.contraseña = contraseña

    def insertar(self):
        print(f"Usuario '{self.nombreUsuario}' insertado correctamente.")

    def modificar(self, nuevo_nombre=None, nuevo_correo=None):
        if nuevo_nombre:
            self.nombreUsuario = nuevo_nombre
        if nuevo_correo:
            self.correo = nuevo_correo
        print(f"Usuario '{self.nombreUsuario}' modificado correctamente.")

    def eliminar(self):
        print(f"Usuario '{self.nombreUsuario}' eliminado correctamente.")

    def buscar(self):
        print(f"Buscando al usuario '{self.nombreUsuario}'.")

class RegistroSueno:
    def __init__(self, idRegistro, usuario, fecha, horaInicio, horaFin):
        self.idRegistro = idRegistro
        self.usuario = usuario
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin

    def registrar(self):
        print(f"Registro de sueño del usuario {self.usuario.nombreUsuario} guardado para la fecha {self.fecha}.")

class Diagnostico:
    def __init__(self, idDiagnostico, usuario, descripcion, fecha):
        self.idDiagnostico = idDiagnostico
        self.usuario = usuario 
        self.descripcion = descripcion
        self.fecha = fecha

    def emitir(self):
        print(f"Diagnostico '{self.descripcion}' emitido para el usuario {self.usuario.nombreUsuario}.")

class Tratamiento:
    def __init__(self, idTratamiento, diagnostico, nombre, descripcion):
        self.idTratamiento = idTratamiento
        self.diagnostico = diagnostico
        self.nombre = nombre
        self.descripcion = descripcion

    def prescribir(self):
        print(f"Tratamiento '{self.nombre}' prescrito para el diagnostico '{self.diagnostico.descripcion}'.")

class Recomendacion:
    def __init__(self, idRecomendacion, usuario, contenido):
        self.idRecomendacion = idRecomendacion
        self.usuario = usuario
        self.contenido = contenido

    def emitir(self):
        print(f"Recomendacion emitida al usuario {self.usuario.nombreUsuario}: {self.contenido}")

class Rol:
    def __init__(self, idRol, nombreRol):
        self.idRol = idRol
        self.nombreRol = nombreRol

    def mostrar(self):
        print(f"Rol: {self.nombreRol}")

class UsuarioRol:
    def __init__(self, usuario, rol):
        self.usuario = usuario
        self.rol = rol

    def asignar(self):
        print(f"El rol '{self.rol.nombreRol}' fue asignado al usuario '{self.usuario.nombreUsuario}'.")

class Sintoma:
    def __init__(self, idSintoma, nombreSintoma, descripcion):
        self.idSintoma = idSintoma
        self.nombreSintoma = nombreSintoma
        self.descripcion = descripcion

    def detallar(self):
        print(f"Sintoma '{self.nombreSintoma}': {self.descripcion}")

class RecomendacionSintoma:
    def __init__(self, recomendacion, sintoma):
        self.recomendacion = recomendacion 
        self.sintoma = sintoma

    def asociar(self):
        print(f"Asociando recomendacion '{self.recomendacion.contenido}' con el sintoma '{self.sintoma.nombreSintoma}'.")


class UsuarioRol:
    def __init__(self, usuario, rol):
        self.usuario = usuario
        self.rol = rol

    def asignar(self):
        print(f"El rol '{self.rol.nombreRol}' fue asignado al usuario '{self.usuario.nombreUsuario}'.")

