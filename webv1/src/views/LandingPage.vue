<template>
    <div>
        <Carousel />
        <Cards />
    </div>
</template>

<script>
import Cards from '../components/Cards.vue';
import Carousel from '../components/Carousel.vue';
    export default{
        components: {
            Carousel,
            Cards
        }
    }
</script>

<style lang="scss" scoped>

</style>