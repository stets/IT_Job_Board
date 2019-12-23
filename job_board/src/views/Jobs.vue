<template>
  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
  <div class='home'>
    <section class='hero is-medium is-bold is-primary'>
      <div class='hero-body'>
        <div class='container'>
          <h1 class='title'>This is an IT Support Group</h1>
          <h2 class='subtitle'>Official Job Board</h2>
        </div>
      </div>
    </section>
    <div class='columns'>
      <div class='column is-four-fifths is-offset-1'><br>
        <p>
          Hiring help desk, sys-admins, hackers, network engineers or any kind of IT staff?
          Reach our network of IT professionals today 👉
        </p>
        <a href='http://bit.ly/ITSupporthiring'>
          <u>Post a job directly via Google Forms</u>
        </a>
      </div>
    </div>
    <div class='columns'>
      <div class='column is-four-fifths is-offset-1'>
        <br />

        <div class='job-row' v-for='job in job_list.slice().reverse()' v-bind:key='job'>
          <h4>{{job.gsx$company.$t}}</h4>
          <h1 class='title is-4 role-title'>
            <b>{{job.gsx$role.$t}}</b>
          </h1>
          <b>🌍</b>
          {{job.gsx$location.$t}}
          <br />

          <b>Posted</b>
          {{job.gsx$timestamp.$t}}
          <a :href=job.gsx$url.$t>
            <button class='button is-danger is-pulled-right apply-button'>Apply</button>
          </a>
          <details>
            <summary>More Details</summary>
            <br />
            <b>posted by:</b>
            {{job.gsx$postedby.$t}}
            <br />
            <b>remote:</b>
            {{job.gsx$remote.$t}}
            <br />
            <b>salary range:</b>
            {{job.gsx$salaryrange.$t}}
            <br />
            <b>visa:</b>
            {{job.gsx$visasponsorship.$t}}
            <br />
            <b>contact:</b>
            {{job.gsx$contact.$t}}
            <br />
            <b>Description:</b>
            {{job.gsx$descriptionornotes.$t}}
            <br />
            <a :href=job.gsx$url.$t>
              <button class='button is-danger'>Apply</button>
            </a>
          </details>
          <hr />
        </div>
      </div>
      <div class='column'></div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';

export default {
  name: 'jobs',
  components: {},
  data() {
    return {
      job_list: '',
    };
  },
  methods: {
    get_jobs() {
      const vthis = this;

      Axios({
        method: 'get',
        url:
          'https://spreadsheets.google.com/feeds/list/1zBeYVkoyLavJIIBKJ9aG8ID_ZtLe-UHeKK72hk_ZKfE/1/public/values?alt=json',
      }).then(
        (response) => {
          vthis.job_list = response.data.feed.entry;
        },
      );
    },
  },
  mounted() {
    this.get_jobs();
  },
};
</script>

<style lang='scss'>
.banner {
  background-color: #eaeaea;
  border: 1px solid #323232;
  border-radius: 1rem;

  margin: 1rem;
}

.job-row {
  background-color: #f1f1f1;
  border: 1px solid #bebebe;
  border-radius: 1rem;

  padding: 1rem;
  margin: 1rem;

  &:hover {
    background-color: #e2e2e2;

    .apply-button {
      display: block;
    }
  }

  .apply-button {
    display: none;
  }

  .role-title {
    width: 100%;
    padding: 1rem;
  }
}
</style>
