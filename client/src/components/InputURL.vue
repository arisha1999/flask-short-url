<template>
  <div class="container">
    <div class="container">
      <br>
      <br>
      <div class="row align-items-center justify-content-center">
        <h1>Short URL generator</h1>
      </div>
      <br>
      <form method="POST" @submit="onSubmit">
        <div class="form-group row">
          <div class="input-group mb-3">
            <input class="form-control" type="text" placeholder="Enter URL"
                 v-model="originalUrl"
                   oninvalid="this.setCustomValidity('Please enter URL')"
                   oninput="setCustomValidity('')" required>
            <div class="input-group-append">
              <button type="submit" class="btn btn-primary " style="float:right ">Generate</button>
            </div>
          </div>
        </div>
      </form>
      <result :short-url=shortUrl :message.sync=message :show-message.sync=showMessage
              :variant.sync=variant v-if="showResult"></result>
      <alert :message=message :variant=variant v-if="showMessage"></alert>
    </div>
  </div>
</template>


<script>
import Alert from './Alert';
import Result from './Result';

export default {
  data() {
    return {
      shortUrl: '',
      message: '',
      showMessage: false,
      showResult: false,
      originalUrl: '',
      variant: 'danger',
    };
  },
  methods: {
    addNew() {
      const path = 'https://flask-short-url-be.herokuapp.com/';
      const orig = this.originalUrl;
      this.axios
        .post(path, { originalUrl: orig })
        .then((res) => {
          this.shortUrl = res.data.short_url;
          this.showResult = true;
        })
        .catch((error) => {
          this.showMessage = true;
          this.message = error;
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.showMessage = false;
      this.showResult = false;
      this.addNew();
    },
  },
  components: {
    alert: Alert,
    result: Result,
  },
};
</script>
