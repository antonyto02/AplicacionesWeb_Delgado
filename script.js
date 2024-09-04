/* Pregunta: ¿Cuál es la función de 'document.getElementById' en JavaScript? */
        /* Para seleccionar un objeto y poder manipularlo*/
        function checkAnswer() {
            /* Pregunta: ¿Qué hace 'prompt' y cómo se puede usar en lugar de 'alert'? */
            /* Prompt muestra un cuadro de dialogo para ingresar valores, mientras que alert muestra un mensaje */
            let answer = prompt("Enter your answer:");

            /* Pregunta: ¿Cuál es el propósito de la instrucción 'if' en este fragmento de código? */
            /* Verifica si la variable answer es "paris" en minúsculas se muestre un mensaje de "correcto", si no, "try again"*/
            if (answer.toLowerCase() === 'paris') {
                alert("Correct!");
            } else {
                alert("Try again!");
            }
        }

        /* Pregunta: ¿Cómo se puede manipular el DOM usando JavaScript para cambiar el contenido de un elemento? */
        /* Se seleciona el elemento y usando la función innerText se modifica su valor */
        document.getElementById("question").innerText = "What is the capital of France?";