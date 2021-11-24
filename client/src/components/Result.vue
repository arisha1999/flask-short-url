<template>
  <form @submit="onSubmit">
    <div class="form-group row">
      <div class="input-group mb-3">
        <input class="form-control" type="text" v-model="shortUrl"
               id="shortUrl" ref="mylink" readonly>
        <div class="input-group-append">
          <button type="submit" class="btn btn-outline-secondary">Copy URL</button>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  props: ['shortUrl', 'message', 'showMessage', 'variant'],
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const Url = this.$refs.mylink;
      Url.innerHTML = window.location.href;
      Url.select();
      try {
        const successful = document.execCommand('copy');
        const msg = successful ? 'successfully' : 'unsuccessfully';
        this.showMessage = true;
        this.variant = 'success';
        this.message = (`Url was copied ${msg}`);
        this.$emit('update:showMessage', this.showMessage);
        this.$emit('update:variant', this.variant);
        this.$emit('update:message', this.message);
      } catch (error) {
        this.showMessage = true;
        this.variant = 'danger';
        this.message = 'Oops, unable to copy';
        this.$emit('update:showMessage', this.showMessage);
        this.$emit('update:variant', this.variant);
        this.$emit('update:message', this.message);
      }
    },
  },
};
</script>
