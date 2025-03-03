import os
import struct
from punt_play import PuntPlay

# Tamaño de registro basado en estructura de PuntPlay
REGISTRO_SIZE = 256
FORMATO_REGISTRO = '256s'
REGISTRO_VACIO = b'\x00' * REGISTRO_SIZE

# Directorio para archivos de colisión
COLLISION_DIR = "collisions"

def inicializar_tabla():
    """Crea/Carga el archivo info.dat con 750 registros vacíos y asegura existencia del directorio de colisiones"""
    if not os.path.exists("info.dat"):
        with open("info.dat", "wb") as f:
            f.write(REGISTRO_VACIO * 750)
    
    # Crear directorio de colisiones si no existe
    if not os.path.exists(COLLISION_DIR):
        os.makedirs(COLLISION_DIR)

def registro_ocupado(posicion: int) -> bool:
    """Verifica si una posición en la tabla está ocupada"""
    with open("info.dat", "rb") as f:
        f.seek(posicion * REGISTRO_SIZE)
        return f.read(REGISTRO_SIZE) != REGISTRO_VACIO

def escribir_registro(posicion: int, registro: PuntPlay):
    """Escribe un registro en la posición especificada"""
    registro_str = str(registro)
    registro_bytes = registro_str.ljust(REGISTRO_SIZE).encode()
    
    try:
        with open("info.dat", "r+b") as f:
            f.seek(posicion * REGISTRO_SIZE)
            actual = f.read(REGISTRO_SIZE)
            if actual == REGISTRO_VACIO:
                f.seek(posicion * REGISTRO_SIZE)  # Reposicionar puntero
                f.write(registro_bytes)
                return True
    except IOError:
        pass
    
    # Manejo de colisión usando el directorio específico
    colision_file = os.path.join(COLLISION_DIR, f"{posicion}-col.dat")
    with open(colision_file, "ab") as f:
        f.write(registro_bytes)
    return False

def buscar_registros(posicion: int) -> list:
    """Recupera todos los registros en una posición"""
    registros = []
    
    # Leer registro principal
    with open("info.dat", "rb") as f:
        f.seek(posicion * REGISTRO_SIZE)
        dato = f.read(REGISTRO_SIZE)
        if dato != REGISTRO_VACIO:
            registros.append(dato.decode().strip('\x00'))
    
    # Leer colisiones desde el directorio específico
    colision_file = os.path.join(COLLISION_DIR, f"{posicion}-col.dat")
    if os.path.exists(colision_file):
        with open(colision_file, "rb") as f:
            while True:
                dato = f.read(REGISTRO_SIZE)
                if not dato:
                    break
                registros.append(dato.decode().strip('\x00'))
    
    return registros

def obtener_estadisticas_colisiones():
    """Analiza y retorna estadísticas sobre las colisiones en el sistema"""
    total_colisiones = 0
    max_colisiones = 0
    posicion_max_colisiones = -1
    
    # Contar archivos de colisión y analizar sus tamaños
    for archivo in os.listdir(COLLISION_DIR):
        if archivo.endswith("-col.dat"):
            ruta_completa = os.path.join(COLLISION_DIR, archivo)
            tamanio = os.path.getsize(ruta_completa)
            num_registros = tamanio // REGISTRO_SIZE
            total_colisiones += num_registros
            
            if num_registros > max_colisiones:
                max_colisiones = num_registros
                posicion_max_colisiones = int(archivo.split('-')[0])
    
    return {
        "total_colisiones": total_colisiones,
        "max_colisiones_en_posicion": max_colisiones,
        "posicion_max_colisiones": posicion_max_colisiones
    }