<template>
  <div id="App">
    <img alt="Vue logo" src="./assets/logo.png">
    <h2>Fetch data</h2>
    <Users />
  </div>
</template>

<script>
import Users from './components/Users.vue'
export default {
  name: "App",
  components: {
    Users
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  margin-top: 60px;
  height:200%

}
</style>

