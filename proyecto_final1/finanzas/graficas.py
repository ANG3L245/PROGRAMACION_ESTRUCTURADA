import matplotlib.pyplot as plt
import os


def construirGrafica(categorias, montos):
    plt.figure(figsize=(6, 4))
    plt.bar(categorias, montos, color="skyblue")
    plt.title("Gastos por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Monto ($)")
    plt.xticks(rotation=30)
    plt.tight_layout()


def verGrafica(categorias, montos):
    construirGrafica(categorias, montos)
    manager = plt.get_current_fig_manager()
    try:
        manager.resize(600, 400)
    except Exception:
        pass
    plt.show(block=False)
    plt.pause(0.1)
    input("\n\t\t\tPresiona ENTER para cerrar la grafica y continuar...")
    plt.close()


def guardarGrafica(categorias, montos, nombre_archivo="grafica_gastos.png"):
    os.makedirs("graficas_guardadas", exist_ok=True)
    ruta = os.path.join("graficas_guardadas", nombre_archivo)
    construirGrafica(categorias, montos)
    plt.savefig(ruta)
    plt.close()
    print(f"\n\t...Grafica guardada como {ruta}...")