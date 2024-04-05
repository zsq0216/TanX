<template>
  <div class="q-pa-md">
    <div class="q-gutter-md row items-start">
      <q-uploader
        style="max-width: 300px"
        url="http://47.122.24.142:7766/upload"
        label="上传文件"
        multiple
        auto-upload
        max-file-size="4096"
        accept=".jpg, .pdf, image/*"
        @rejected="onRejected"
      />
    </div>
  </div>
</template>

<script setup>
import { useQuasar,Notify } from 'quasar';

const $q = useQuasar();

function onRejected(rejectedEntries) {
  // Notify plugin needs to be installed
  // https://quasar.dev/quasar-plugins/notify#Installation
  Notify.create({
    type: 'negative',
    message: `${rejectedEntries.length} file(s) did not pass validation constraints`
  });
}
</script>

