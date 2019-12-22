<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <h1>what up my jobbers</h1>
  </div>
</template>

<script>
import Axios from 'axios';

export default {
  name: 'jobs',
  components: {},
  methods: {
    get_jobs() {
      Axios({
        method: 'get',
        url:
          'https://spreadsheets.google.com/feeds/list/1zBeYVkoyLavJIIBKJ9aG8ID_ZtLe-UHeKK72hk_ZKfE/1/public/values?alt=json',
      }).then(
        (response) => {
          console.log(response);
        },
        (error) => {
          console.log(error);
        },
      );
    },
  },
  mounted() {},
};
</script>
