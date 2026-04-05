# ==========================
# servicios/tarea_servicio.py
# ==========================
from modelos.tarea import Tarea
from supabase import create_client
import os
from dotenv import load_dotenv


class TareaServicio:
    def __init__(self):
        load_dotenv()  # 🔥 CARGA el .env

        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")

        print("URL:", url)
        print("KEY:", key[:10] if key else None)

        if not url or not key:
            raise ValueError("Variables de entorno no cargadas")

        self.supabase = create_client(url, key)

    def agregar_tarea(self, descripcion: str):
        self.supabase.table("tareas").insert({
            "tarea": descripcion,
            "completada": False
        }).execute()

    def obtener_todas(self):
        response = self.supabase.table("tareas").select("*").execute()

        tareas = []
        if response.data:
            for t in response.data:
                tareas.append(
                    Tarea(
                        id=t["id"],
                        descripcion=t["tarea"],
                        completado=t["completada"]
                    )
                )
        return tareas

    def completar_tarea(self, id_tarea: int):
        self.supabase.table("tareas").update({
            "completada": True
        }).eq("id", id_tarea).execute()

    def eliminar_tarea(self, id_tarea: int):
        self.supabase.table("tareas").delete().eq("id", id_tarea).execute()