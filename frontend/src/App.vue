<template>
  <div class="container">
      <div class="row">
          <div class="col">
              <button type="button" class="btn btn-primary" @click="getTime">Get time</button>
              <p class="lead" v-if="time">Time: {{ time }}</p>
          </div>
      </div>
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
