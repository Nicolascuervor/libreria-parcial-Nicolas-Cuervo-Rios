
PREGUNTAS DE SELECCIÓN MÚLTIPLE
Escribe el ID de la respuesta correcta y explica en una línea por qué las otras son incorrectas.



PREGUNTA 1:

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

INCORRECTO:  ya que, el cliente no es un actor que participara o tendra peso sobre como se hicieron las pruebas, eso lo decide el equipo tecnico     

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

INCORRECTO: Las pruebas pueden ser ejecutadas tanto en entornos de produccion o de desarrollo antes de subir a produccion

C. Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas. 

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.

INCORRECTO: El pipeline de CI/CD debe implementarse antes de tener cualquier modulo terminado si se busca realizar un correcto proceso de desarrollo basado en pruebas  


RESPUESTA CORRECTA: C 



PREGUNTA 2:

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

INCORRECTO: El paso de refactorización ocurre después de tener un test pasando en verde no se hace antes. 

B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.
 
C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

INCORRECTO: El concepto de Green consiste en escribir el código estrictamente necesario para que el test actual pase.

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.

INCORRECTO: Esta afirmación es falsa o erronea dentro de la disciplina de TDD ya que este exige de forma estricta que el test guíe el desarrollo.



RESPUESTA CORRECTA: B


PREGUNTAS ABIERTAS
Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

PA-1

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". 
Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

R: El TDD obliga a realizar esto en el green ya que en el se requiere implementar el codigo justo y necesario para que la prueba pase bajo el 
contexto que se requiere ya que sin esto no sabriamos cual es el minimo resultado esperado cuando la prueba se ejecute, si el desarrollador se 
aprovecha de esto y escribe código "limpio y completo" el proceso tendria demasiada complejidad desde un inicio 


---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.


TDD: El Test Driven Development se enfoca en realizar pruebas antes de cualquier escritura de linea de codigo bajo la metodologia de Red Green Refactor, 
esto con el objetivo de identificar desde un comienzo cuales serian las diferentes excepciones o errores a los que el sistema podria someterse y controlarlos en un temprano desarrollo. Esta dirigido principalmente al equipo tecnico

BBD: El Behavior driven development o desarrollo basado en comportamiento esta dirigido tanto para personas no tecnicas como los que si y ayuda al equipo a determinar si se esta
construyendo el producto correcto o esperado.


Tanto TDD como BDD buscan asegurar que el software sea útil y confiable ya que el BDD define la dirección y asegura que la aplicación haga exactamente lo que el cliente necesita TDD por otro lado
se encarga de que los cimientos internos de esa aplicación estén bien construidos y no fallen.

---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

R: tener una gran cobertura de código es util pero eso no significa o garantiza la ausencia de bugs. 

Una cobertura del 95% solo indica que casi todas las líneas se ejecutaron pero esto no verifica si la lógica las validaciones de datos o los casos extremos son correctos.

Ejemplo sencillo
def dividir(a, b):
    return a / b

Si el sistema intentara dividir algo como (10, 0) el programa claramente arrojará un error  de división por cero o devolverá un comportamiento inesperado. La prueba inicial jamás cubrió este escenario, lo que demuestra que cobertura de 
código no es lo mismo que cobertura de comportamiento.



---

**PA-4 (0.2 puntos)**

En el contexto de la regla: descuento entre 0% y 40%, un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

La lógica que se plantea es incorrecta porque ignora los errores en los límites y los fallos en la lógica de salto de rangos.
Probar únicamente el 20% no garantiza que el 1%, el 39% o el 40% funcionen correctamente. Un programador puede cometer un error tipográfico
que ocasione que el sistema rechace el descuento máximo permitido o acepte valores fuera de lo establecido.

Valores concretos que seria ideal implementar:

Valores límite de descuento (para probar los bordes de la regla):
El mínimo válido: 0% Justo debajo del límite válido -1% (Debería dar error o ser rechazado).
El máximo válido: 40%Justo por encima del límite válido: 41% (Debería dar error o ser rechazado).

Valores centrales:Un valor cualquiera dentro del rango válido, como el 20% sugerido por la persona.


---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 

¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?


Sin pruebas automatizadas un pipeline de CI/CD pierde su propósito principal y podria decirse que se convierte en un simple automatizador de despliegues caóticos. 
En lugar de garantizar calidad y velocidad, aumenta drásticamente el riesgo de introducir errores críticos directamente en producción.


---

