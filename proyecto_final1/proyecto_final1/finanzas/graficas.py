import matplotlib.pyplot as plt
import os

def construirGraficaHistorial(etiquetas, montos, tipo):
    plt.figure(figsize=(9, 5))
    
    color_barras = "lightgreen" if tipo == "ingreso" else "lightcoral"
    
    plt.bar(etiquetas, montos, color=color_barras, edgecolor='black')
    
    plt.title(f"Historial de {tipo}s (Individuales)")
    plt.xlabel("Movimientos")
    plt.ylabel("Monto ($)")
    plt.xticks(rotation=45, ha="right")
    
    # Cuadrícula solo en el eje Y para que la gráfica de barras se vea más limpia
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()


def verGraficaHistorial(etiquetas, montos, tipo):
    construirGraficaHistorial(etiquetas, montos, tipo)
    manager = plt.get_current_fig_manager()
    try:
        manager.resize(800, 500)
    except Exception:
        pass
    plt.show(block=False)
    plt.pause(0.1)
    input("\n\t\t\tPresiona ENTER para cerrar la grafica y continuar...")
    plt.close()


def guardarGraficaHistorial(etiquetas, montos, tipo):
    os.makedirs("graficas_guardadas", exist_ok=True)
    nombre_archivo = f"historial_{tipo}s_individuales.png"
    ruta = os.path.join("graficas_guardadas", nombre_archivo)
    
    construirGraficaHistorial(etiquetas, montos, tipo)
    plt.savefig(ruta)
    plt.close()
    print(f"\n\t...Grafica guardada como {ruta}...")