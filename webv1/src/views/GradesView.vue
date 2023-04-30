<template>

    <div class="body">

        <img src="@/assets/gradesBackground.png" alt="">

    </div>

    <div class="contentBox"></div> 




    <div class="container">
      <h1>Calculadora de Notas</h1>
      <form>
        <div v-for="(item, index) in notas" :key="index">
          <label for="nota">Nota:</label>
          <input type="text" id="nota" v-model="item.nota">
          <label for="porcentaje">Porcentaje:</label>
          <input type="text" id="porcentaje" v-model="item.porcentaje">
          <button @click.prevent="borrarNota(index)">Borrar</button>
        </div>
        <br>
        <button @click.prevent="agregarNota">Agregar Nota</button>
        <button @click.prevent="calcularNotaFinal">Calcular Nota Final</button>
        <button @click.prevent="limpiarFormulario">Borrar todo</button>
      </form>
      <p id="notaFinal" v-if="notaFinal">Tu nota final es: {{ notaFinal }}</p>
    </div>
  </template>
  
<script>
export default {
    data() {
        return {
            notas: [{ nota: 0, porcentaje: 0 }],
            notaFinal: null
        };
    },
    methods: {
        agregarNota() {
            this.notas.push({ nota: 0, porcentaje: 0 });
        },
        borrarNota(index) {
            this.notas.splice(index, 1);
        },
        calcularNotaFinal() {
            let sumaNotas = 0;
            let sumaPorcentajes = 0;
            for (let i = 0; i < this.notas.length; i++) {
                sumaNotas += parseFloat(this.notas[i].nota) * (parseFloat(this.notas[i].porcentaje) / 100);
                sumaPorcentajes += parseFloat(this.notas[i].porcentaje);
            }
            this.notaFinal = sumaNotas.toFixed(2);

        },

        limpiarFormulario() {
            this.notas = [{ nota: 0, porcentaje: 0 }];
        }

    }
};
</script>
  

<style>

body{
    font-family: 'Roboto', sans-serif;
}

label {
}


.contentBox {
    position: fixed;
    width: 50%;
    height: 100vh;
    min-height: 10000px;
    z-index: -1;
    background-color: rgb(248, 248, 248);
    opacity: 0.5;
    left: 25%;
    background-repeat: repeat-y;
}



.body {
    z-index: -1;
    position: fixed;
    filter: blur(2px);
}


.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 12%;
}

form {
    display: flex;
    flex-direction: column;
    padding: 5%;
    font-weight: 700;
    font-size: larger;
    overflow: auto;

}

#notaFinal {
    font-size: 5rem;

}
</style>
  