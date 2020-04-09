<template>
  <div>
    <b-alert variant="info"
             :show="dismissCountDown"
             dismissible
             @dismissed="dismissCountDown=0"
             @dismiss-count-down="countDownChanged">{{ message }}
    </b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
  data() {
    return {
      dismissSecs: 3,
      dismissCountDown: 0,
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};
</script>
