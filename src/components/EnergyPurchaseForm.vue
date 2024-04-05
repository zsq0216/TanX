<template>
  <div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.electricity_104kwh"
          type="number"
          label="购买电力—万千瓦时"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.heating_GJ"
          type="number"
          label="购买热能—千兆焦耳"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
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
import { useQuasar } from "quasar";
import { Notify } from "quasar";

const $q = useQuasar();

// 定义响应式数据
const formData = reactive({
  electricity_104kwh: 0,
  heating_GJ: 0,
});

const emit = defineEmits(["update:energyPurchase"]);
const isSaved = ref(false);

function handleSave() {
  // 假设处理保存逻辑...
  emit("update:energyPurchase", formData);
  isSaved.value = true;
}

</script>
