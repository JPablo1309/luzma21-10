#  Documento de Pruebas - Conversor de Temperatura

## 1. Prueba Unitaria
**Nombre:** Conversión Celsius → Fahrenheit  
**Objetivo:** Verificar que la función `celsius_a_fahrenheit` realice correctamente la conversión.  
**Entrada:** 0 °C  
**Salida esperada:** 32 °F  
**Resultado:** Correcto (la prueba pasa con `assertAlmostEqual`)

---

## 2. Prueba de Integración
**Nombre:** Conversión encadenada  
**Objetivo:** Comprobar que si se convierte de Celsius a Fahrenheit y luego de Fahrenheit a Celsius, se obtiene el mismo valor original (con un pequeño margen de error).  
**Ejemplo:**  
Entrada: 25 °C → F → C  
Salida esperada: ≈25 °C  
**Resultado:** Correcto (ambas funciones trabajan en conjunto)

---

## 3. Prueba de Rendimiento
**Nombre:** Conversión repetida  
**Objetivo:** Evaluar el rendimiento si se realizan miles de conversiones consecutivas.  
**Descripción:**  
Se ejecuta la conversión 1 millón de veces y se mide el tiempo.  
**Criterio:** El proceso debe completarse en menos de 2 segundos en un equipo promedio.  
**Código sugerido:**
```python
import time
start = time.time()
for _ in range(1000000):
    celsius_a_fahrenheit(100)
end = time.time()
print("Tiempo:", end - start, "segundos")
