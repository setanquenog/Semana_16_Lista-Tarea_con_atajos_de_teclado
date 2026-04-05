# ==========================
# modelos/tarea.py
# ==========================
class Tarea:
    def __init__(self, id: int, descripcion: str, completado: bool = False):
        self.id = id
        self.descripcion = descripcion
        self.completado = completado

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        if not value or not value.strip():
            raise ValueError("La descripción no puede estar vacía")
        self._descripcion = value.strip()