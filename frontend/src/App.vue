<script setup>
import Blog from "./components/Blog.vue";
</script>

<template>
  <div id="app">
    <h1>🧁 Mini Blog</h1>
    <Blog />

    <div class="test"></div>
  </div>
</template>

<style scoped>
.test {
  background: red;
  height: 20px;
  width: 100%;
}
</style>
