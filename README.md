# Proyecto: Criptografía Post-Cuántica con Kyber y ECDH Híbrido (Jupyter Notebook)

Este repositorio contiene una implementación en Jupyter Notebook de dos esquema de cifrado  el algoritmo post-cuántico **Kyber** (un Mecanismo de Encapsulamiento de Clave - KEM) y el algoritmo clásico **Elliptic Curve Diffie-Hellman (ECDH)** para el intercambio de claves. 

## Descripción

En este repositorio se analiza ambos esquemas, en rendimiento  y se hacen implementaciones experimentales de ambos.



Este proyecto implementa un esquemaambos  simplificados:

1.  **Intercambio de claves ECDH:** Se utiliza ECDH para establecer una clave secreta compartida de forma clásica.
2.  **Encapsulamiento de clave Kyber:** Se utiliza Kyber para encapsular una clave secreta *diferente*.
3.  **Clave final:** La clave secreta compartida final se deriva combinando (por ejemplo, mediante una función hash criptográfica como SHA-256) las claves secretas obtenidas de ECDH y Kyber.

Esta clave final se puede usar luego para cifrar y descifrar mensajes con un algoritmo de cifrado simétrico (como AES), que no se implementa en este proyecto. El foco está en el intercambio *seguro* de claves.

## Contenido del Repositorio

*   **`proyecto.ipynb`:**  Este es el archivo principal.  Es un Jupyter Notebook que contiene:
    *   **Introducción:** Breve explicación de la criptografía post-cuántica, Kyber, ECDH y la motivación para los esquemas híbridos.
    *   **Implementación de ECDH:**  Código Python que implementa el intercambio de claves ECDH (utilizando una biblioteca criptográfica existente, *no desde cero* - ver más abajo).
    *   **Implementación de Kyber:** Código Python que implementa el encapsulamiento y desencapsulamiento de clave con Kyber (utilizando una biblioteca criptográfica existente, *no desde cero*). Se especifica el nivel de seguridad utilizado (Kyber512, Kyber768 o Kyber1024).
    *   **Esquema Híbrido:** Código que combina ECDH y Kyber para generar la clave secreta compartida final.
    *   **Ejemplo de Uso:** Demostración de cómo se encapsula y desencapsula una clave, y cómo se deriva la clave híbrida.
    *   **Conclusiones:**  Discusión sobre las ventajas y desventajas del esquema híbrido.
    *   **Referencias:**  Enlaces a documentación relevante (especificaciones de Kyber, documentación de las bibliotecas utilizadas, artículos sobre criptografía post-cuántica).
 
*   **`kyber.ipynb`:**  Este es el archivo principal.  Es un Jupyter Notebook que contiene:
*   En este archivo está únicamente la implementación del  kyber 
 
 

 


* **`README.md`:** Este archivo, que proporciona una descripción general del proyecto.

* **`requirements.txt` (opcional):**  Si el proyecto utiliza bibliotecas externas (y es *altamente probable* que las use), este archivo lista las dependencias para que otros usuarios puedan instalarlas fácilmente (por ejemplo, usando `pip install -r requirements.txt`).

## Requisitos

*   **Python 3.7+ (recomendado 3.9+):** El código está escrito en Python.
*   **Jupyter Notebook/JupyterLab:** Para ejecutar el notebook interactivo.
*   **Bibliotecas de python requeridas :**
    *   **`cryptography` (para ECDH):**  La biblioteca `cryptography` de Python es *excelente* para la implementación de ECDH.  Proporciona una API de alto nivel segura y fácil de usar.  *No intentes implementar 

## Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio:**
    ```bash
    git clone <https://github.com/macaluzate/cripto-proyecto.git>
    ```
2.  **Ejecutar las celdas:** Ejecuta las celdas del notebook en orden, desde el principio hasta el final.  Las celdas de código están comentadas para explicar lo que está sucediendo.

## Advertencias y Consideraciones

*   **Este proyecto es una demostración educativa:**  Está diseñado para ilustrar los conceptos de Kyber, ECDH y esquemas híbridos.  No está pensado para ser utilizado en entornos de producción sin una revisión exhaustiva por parte de expertos en criptografía.
*   **No implementes criptografía desde cero:**  La implementación segura de algoritmos criptográficos es extremadamente difícil.  *Siempre* utiliza bibliotecas criptográficas bien establecidas y revisadas por expertos, como `cryptography` y `pyoqs`.
*   **Mantén las bibliotecas actualizadas:**  Las vulnerabilidades se descubren y corrigen constantemente.  Asegúrate de utilizar las últimas versiones de las bibliotecas criptográficas.
*   **Consulta a expertos:**  Si necesitas implementar criptografía post-cuántica en un sistema real, consulta a expertos en seguridad informática y criptografía.
*   Se usan generadores pseduoaleatorios inadecuados: Se debe usar generadores especializados para criptografía. No se usaron debido a que se trata de una demostración académica 

## Licencia

Este proyecto se distribuye bajo la licencia MIT (o la licencia de tu elección).  Consulta el archivo `LICENSE` (si lo incluyes) para más detalles.  Si no incluyes un archivo `LICENSE`, es una buena práctica especificar la licencia en el README.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras errores, omisiones, o tienes sugerencias, por favor, abre un *issue* o envía un *pull request*.
