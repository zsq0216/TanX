<template>
  <div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.plane_kyuan"
          type="number"
          label="差旅机票费—千元"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.CRH_kyuan"
          type="number"
          label="差旅高铁费—千元"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.train_kyuan"
          type="number"
          label="差旅火车费—千元"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.urbantransport_kyuan"
          type="number"
          label="市内交通费—千元"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
    </div>
    <div class="row justify-evenly">
      <div class="col-5">
        <q-input
          v-model.number="formData.selfdriving_per"
          type="number"
          label="日常通勤选择自驾的员工数—人"
          :lazy-rules="true"
          :rules="[(val) => val >= 0 || '值不能为负数']"
        />
      </div>
      <div class="col-5">
        <q-input
          v-model.number="formData.publictransport_per"
          type="number"
          label="日常通勤选择公共交通的员工数—人"
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
import { useQuasar, Notify, is } from "quasar";

const $q = useQuasar();

// 定义响应式数据
const formData = reactive({
  plane_kyuan: 0,
  CRH_kyuan: 0,
  train_kyuan: 0,
  urbantransport_kyuan: 0,
  selfdriving_per: 0,
  publictransport_per: 0,
});
const emit = defineEmits(["update:travelcommute"]);
const isSaved = ref(false);
function handleSave() {
  // 假设处理保存逻辑...
  emit("update:travelcommute", formData);
  isSaved.value = true;
}

</script>
