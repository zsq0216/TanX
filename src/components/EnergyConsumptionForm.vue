<template>
  <div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.rawcoal_t"
          type="number"
          label="原煤—吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.cleanedcoal_t"
          type="number"
          label="洗精煤—吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.coke_t"
          type="number"
          label="焦炭—吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.naturalgas_104m3"
          type="number"
          label="天然气—万立方米"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.gasoline_t"
          type="number"
          label="汽油—吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.diesel_t"
          type="number"
          label="柴油—吨"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.others_t"
          type="number"
          label="生产过程中的其他二氧化碳排放—吨"
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
import { useQuasar,Notify } from "quasar";
import { computed } from "vue";
import { useStore } from "vuex";
import axios from "axios";

const $q = useQuasar();
const store = useStore();
//const token = computed(() => store.getters.token);
const token = localStorage.getItem('userToken');
const isLoading = ref(true); // 用于表示加载状态

// 定义响应式数据
const formData = reactive({
  rawcoal_t: 0,
  cleanedcoal_t: 0,
  coke_t: 0,
  naturalgas_104m3: 0,
  gasoline_t: 0,
  diesel_t: 0,
  others_t: 0,
});
const isSaved = ref(false); // 用于表示是否保存成功
const emit = defineEmits(["update:energyConsumption"]);

function handleSave() {
  // 假设处理保存逻辑...
  emit("update:energyConsumption", formData);
  isSaved.value = true;
}

</script>
