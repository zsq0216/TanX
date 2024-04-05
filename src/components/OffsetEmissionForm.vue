<template>
  <div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.green_electricity_104kwh"
          type="number"
          label="购买绿色电力-万千瓦时"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.otheroffset_t"
          type="number"
          label="其他碳排放抵消-吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.output_wyuan"
          type="number"
          label="月产值—万元"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input style="opacity: 0; pointer-events: none" />
      </div>
    </div>
    <div>
      <UploadComponent />
    </div>
    <div>
      <q-btn label="保存" color="primary" @click="handleSave" />
      <q-icon name="done" v-if="isSaved" class="q-ml-md"/>
    </div>
  </div>
</template>

<script setup>
import UploadComponent from "../components/UploadComponent.vue";

import { ref, reactive } from "vue";
import { useQuasar, Notify, is } from "quasar";

const $q = useQuasar();

// 定义响应式数据
const formData = reactive({
  green_electricity_104kwh: 0,
  otheroffset_t: 0,
  output_wyuan: 0,
});

const emit = defineEmits(["update:offsetEmission"]);
const isSaved = ref(false);
function handleSave() {
  // 假设处理保存逻辑...
  emit("update:offsetEmission", formData);
  isSaved.value = true;
}

</script>
