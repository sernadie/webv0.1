<template>
    <div>
        <div class="card" style="width: 18rem;">
            <img src="https://th.bing.com/th/id/OIP.59VA8AYb5pxKMuJRLYnjhgHaFE?pid=ImgDet&rs=1" class="card-img-top" alt="...">
        <div class="card-body">
             <h5 class="card-title">Calculadora de notas</h5>
            <p class="card-text">Tienes problemas calculando tu promedio calculando basado en porcentajes?</p>
            <router-link to="notas">
     <a href="#" class="btn btn-primary">Calcula acá</a>
        </router-link>
     
  </div>
</div>
    </div>
</template>

<script>
    export default {
        name: 'Cards',
        
    }
</script>

<style>

.btn-primary{
    border-color: black;
}

   

</style>