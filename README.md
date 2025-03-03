# 🏈 NFL Play Analysis Engine

## Visión General

El Sistema de Registros NFL es una plataforma computacional optimizada para el almacenamiento y recuperación eficiente de jugadas de fútbol americano mediante una arquitectura de dispersión hash adaptativa. El sistema implementa un modelo de acceso O(1) para consultas de alta velocidad sobre conjuntos extensos de datos de partidos NFL, con resolución de colisiones mediante encadenamiento externo.

## 🧠 Arquitectura Neural

El sistema implementa un paradigma de almacenamiento basado en un enfoque de dispersión hash personalizado que:

1. Transforma atributos multi-dimensionales (fecha, cuarto, equipo) en una representación vectorial compacta
2. Proyecta estos vectores en un espacio discreto de 750 posiciones mediante una función de transformación no-lineal
3. Resuelve colisiones mediante un mecanismo adaptativo de encadenamiento con persistencia en sistema de archivos

![Arquitectura del Sistema](https://via.placeholder.com/800x400)

## 🚀 Características Principales

- **Indexación Multidimensional**: Función hash que integra componentes temporales y categóricos para distribución uniforme
- **Resolución de Colisiones Adaptativa**: Sistema de archivos jerárquico para gestión óptima de colisiones
- **Persistencia Binaria Eficiente**: Almacenamiento de registros con tamaño fijo para acceso aleatorio O(1)
- **Interfaz de Consulta Flexible**: Recuperación inmediata por posición hash con soporte para resolución de colisiones
- **Pipeline de Carga ETL**: Procesamiento automatizado de datasets CSV de temporadas NFL

## 📋 Componentes Principales

| Módulo | Descripción | Función Principal |
|--------|-------------|-------------------|
| `file_manager.py` | Subsistema de E/S para persistencia binaria | Gestión de almacenamiento con resolución de colisiones |
| `hash_function.py` | Algoritmo de dispersión multidimensional | Transformación de atributos en índices de acceso |
| `punt_play.py` | Modelado de entidades y esquema de datos | Representación estructurada de jugadas NFL |
| `menu.py` | Interfaz de usuario y controlador | Orquestación de flujos de trabajo y visualización |

## 🛠️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/username/nfl-play-analysis.git

# Navegar al directorio del proyecto
cd nfl-play-analysis

# Crear directorios necesarios
mkdir -p data/segundaprogramada
mkdir -p collisions

# Preparar ambiente (opcional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 🔍 Uso

```python
# Iniciar el sistema
python main.py

# Flujo de trabajo típico:
# 1. Seleccionar opción 1 para cargar datos de la temporada
# 2. Seleccionar opción 2 para consultar registros por posición hash
# 3. Analizar resultados para identificar patrones de juego
```

## 📊 Ejemplos de Consulta

```
=== SISTEMA DE REGISTROS NFL ===
1. Cargar datos de temporada
2. Buscar por posición
3. Salir
Seleccione una opción: 2

Ingrese posición a buscar (0-749): 125

Registros encontrados en posición 125:
1. GameID: 2023102900 | Teams: SF@LAR | Yards: 45.0 | Quarter: 3 | Date: 2023-10-29 | Time: 5:28
2. GameID: 2023112600 | Teams: GB@DET | Yards: 52.3 | Quarter: 1 | Date: 2023-11-26 | Time: 12:45
```

## 🧮 Modelo de Dispersión Hash

La función de dispersión implementa una transformación vectorial de los atributos de cada jugada según la fórmula:

```
H(fecha, cuarto, equipo) = (∑digits(fecha) * cuarto * ∑ASCII(equipo)) mod 750
```

Donde:
- `∑digits(fecha)`: Suma de componentes numéricas de la fecha
- `cuarto`: Valor numérico del período de juego
- `∑ASCII(equipo)`: Suma de valores ASCII de los caracteres del equipo local
- `mod 750`: Proyección al espacio de direcciones disponible

## 🔄 Gestión de Colisiones

El sistema implementa un sofisticado mecanismo de resolución de colisiones basado en:

1. **Archivo Principal (`info.dat`)**: Almacenamiento primario de 750 registros de tamaño fijo
2. **Directorio de Colisiones (`/collisions/`)**: Contenedor para archivos secundarios
3. **Archivos de Desbordamiento**: Estructura `{posición}-col.dat` para cada posición con colisiones

Este enfoque garantiza la degradación lineal O(n) en el peor caso cuando múltiples registros colisionan en la misma posición hash.

## 🔬 Análisis de Rendimiento

El rendimiento del sistema está optimizado para:

- **Tiempo de Búsqueda**: O(1) en caso promedio, O(n) en peor caso con colisiones
- **Espacio de Almacenamiento**: Compromiso adaptativo entre memoria principal y secundaria
- **Escalabilidad**: Soporte para cientos de miles de registros con degradación controlada

## 🛣️ Roadmap

- [ ] Implementación de compresión de datos para optimización de almacenamiento
- [ ] Integración de algoritmos de rebalanceo para redistribución de colisiones
- [ ] Desarrollo de interfaces de consulta avanzadas (rango, multiatributo)
- [ ] Mecanismos de caché para consultas frecuentes

## 📜 Licencia

Este proyecto está licenciado bajo MIT License - vea el archivo LICENSE.md para detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios significativos antes de enviar un pull request.

---

Desarrollado con ❤️ para el análisis avanzado de jugadas NFL
