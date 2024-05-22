# Aprendizaje-por-refuerzo
El aprendizaje por refuerzo es una técnica en la cual un agente aprende a tomar decisiones en un entorno para maximizar una recompensa acumulada. Mediante la exploración y la explotación de diferentes acciones, el agente recibe retroalimentación en forma de recompensas o penalizaciones. 
## Aprendizaje por Refuerzo con Q-Learning
Este proyecto implementa un algoritmo simple de Q-Learning en un entorno de rejilla para aprender las acciones óptimas para que un agente maximice sus recompensas. El entorno es una rejilla de 7x7 donde el agente puede moverse hacia arriba, abajo, izquierda o derecha, con estados específicos que proporcionan recompensas o penalizaciones especiales.

### Configuración del Entorno
El entorno consiste en:

1. Una rejilla de 7x7.
* Acciones: 'arriba', 'abajo', 'izquierda', 'derecha'.
2. Recompensas: Cada estado tiene una recompensa de 10, con estados específicos que proporcionan recompensas más altas o penalizaciones.
(6, 6) tiene una recompensa de 500.
* Varios estados tienen una penalización de -50.
* Chocar con el borde de la rejilla resulta en una recompensa de -10.
### Parámetros del Q-Learning
* α (alfa): Tasa de aprendizaje, establecida en 0.9.
* γ (gamma): Factor de descuento, establecido en 0.8.
* ε (epsilon): Tasa de exploración, comienza en 1 y disminuye a 0.01.
* Niter: Número de iteraciones, establecido en 50,000.
## Algoritmo de Q-Learning
El algoritmo sigue estos pasos:

1. Inicializar los valores Q de manera arbitraria para todos los pares estado-acción.
2. Para cada episodio, comenzar desde un estado aleatorio.
3. Seleccionar una acción usando la política ε-greedy. https://www.geeksforgeeks.org/epsilon-greedy-algorithm-in-reinforcement-learning/
4. Tomar la acción, observar la recompensa y hacer la transición al siguiente estado.
5. Actualizar el valor Q usando la regla de actualización de Q-Learning.
6. Repetir hasta el número máximo de pasos por episodio o hasta llegar a un estado final.
