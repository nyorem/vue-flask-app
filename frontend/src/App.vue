<template>
  <div id="app">
      <button @click="getTime">Get time</button>
      <p v-if="time">{{ time }}</p>
  </div>
</template>

<script>
export default {
    data() {
        return {
            time: null,
        }
    },
    methods: {
        getTime() {
            this.$http.get("time").then(response => {
                this.time = response.body.time;
            }, () => {
            });
        }
    }
}
</script>

<style>
</style>
