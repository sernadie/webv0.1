<template>
    <div class="banner">
  <h1>PAGIUNA WEB</h1>
</div>
</template>

<script>
export default {
    name: 'Carousel',

}
</script>

<style scoped>
.banner {
    background-image: url('https://hdqwalls.com/wallpapers/geometry-abstract-minimalism-0x.jpg');
    background-size: cover;
    background-position: center;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 3px solid black;
    border-color: black;
    
  }

  .banner h1 {
    color: white;
    text-shadow: 1px 1px 2px black;
  }
</style>