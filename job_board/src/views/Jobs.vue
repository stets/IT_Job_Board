<template>
  <!-- eslint-disable-next-line vue/max-attributes-per-line -->
  <div class='home'>
    <section class='hero is-medium is-bold is-primary'>
      <div class='hero-body'>
        <div class='container'>
          <h1 class='title'>This is an IT Support Group Job Board</h1>
          <h2 class='subtitle'>A no-bs Job-Board for IT professionals.</h2>
        </div>
      </div>
    </section>
    <div class='columns'>
    </div>
    <div class='columns'>
      <div class='column is-half is-gapless is-offset-1 section'>
        <br/>
        <h1 class='title'>Recent Jobs</h1>
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
        </div>
      </div>

        <div class='column is-gapless is-two-fifths section'><h1 class="subtitle">Why This is an IT Support Group?</h1> <p>
        <a href="https://thisisanitsupportgroup.com">This is an IT Support Group</a> is a rapidly-growing community for helpdesk technicians, sys-admins, hackers, network engineers or any kind of IT staff to connect with each other and advance their careers.
        <br>
        <br>
          Reach our network of >15,000 IT professionals today and find your next perfect hire 👇
        </p>
        <br>
          <a href='http://bit.ly/ITSupporthiring'>
          <button class="button is-danger">Post a job</button>
          </a>
          <div class="container"><br><br>
          <h1 class="subtitle">Partner</h1>
          If you're looking to reach a diverse crowd of IT professionals nationally, <a href="hello@heliositservices.com">contact us</a> for partnership information.</div>
          <div class="container"><br><br>
          <h1 class="subtitle">Open-Source</h1>
          Contribute to open-source and want to help improve this page?
          This page's VueJS source code is public on <a href="https://github.com/stets/IT_Job_Board">Github</a> and accepting pull requests.  </div>
        </div>
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
