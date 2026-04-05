# ==========================
# main.py
# ==========================
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTareas


def main():
    servicio = TareaServicio()
    app = AppTareas(servicio)
    app.mainloop()


if __name__ == "__main__":
    main()