<template>
  <q-page padding>
    <div class="row justify-evenly q-my-md">
      <q-card class="col-8">
        <div class="row justify-evenly items-center">
          <div class="text-h4 q-my-md">填写排放信息</div>
          <div class="col-6 row q-my-md justify-evenly items-center">
            <q-select
              outlined
              v-model="dateData.year"
              :options="years"
              label="年份"
              type="number"
              class="col-5"
              :rules="[(val) => val !== null || '请选择年份']"
              padding
            >
              <template v-slot:prepend>
                <q-icon name="event" />
              </template>
            </q-select>
            <q-select
              outlined
              v-model="dateData.month"
              :options="months"
              label="月份"
              type="number"
              class="col-5"
              :rules="[(val) => val !== null || '请选择月份']"
              padding
            >
              <template v-slot:prepend>
                <q-icon name="event" />
              </template>
            </q-select>
          </div>
        </div>
      </q-card>
    </div>
    <div class="row justify-center">
      <q-stepper v-model="step" animated class="col-8">
        <q-step :name="1" label="能源消耗" title="能源消耗">
          <q-form class="q-gutter-md">
            <energy-consumption-form
              @update:energyConsumption="handleUpdateData1"
            />
          </q-form>
        </q-step>

        <q-step :name="2" label="能源购买" title="能源购买">
          <q-form class="q-gutter-md">
            <energy-purchase-form @update:energyPurchase="handleUpdateData2" />
          </q-form>
        </q-step>

        <q-step :name="3" label="差旅与通勤" title="差旅与通勤">
          <q-form class="q-gutter-md">
            <travel-commute-form @update:travelcommute="handleUpdateData3" />
          </q-form>
        </q-step>

        <q-step :name="4" label="抵消排放" title="抵消排放">
          <q-form class="q-gutter-md">
            <OffsetEmissionForm @update:offsetEmission="handleUpdateData4" />
          </q-form>
        </q-step>

        <template v-slot:navigation>
          <q-stepper-navigation>
            <q-btn flat label="上一步" @click="step--" :disable="step === 1" />
            <q-btn
              color="primary"
              label="下一步"
              @click="step++"
              :disable="step === 4 || !canProceed"
            />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </div>
    <div class="row justify-evenly q-my-md">
      <q-btn
        color="primary"
        label="提交"
        @click="submitForm"
        v-if="step === 4"
        class="q-mt-md col-8"
        :disable="!canProceed"
      />
    </div>
  </q-page>
</template>

<script setup>
import { ref, reactive, computed } from "vue";
import { Notify } from "quasar";
import EnergyConsumptionForm from "../components/EnergyConsumptionForm.vue";
import EnergyPurchaseForm from "../components/EnergyPurchaseForm.vue";
import TravelCommuteForm from "../components/TravelCommuteForm.vue";
import OffsetEmissionForm from "../components/OffsetEmissionForm.vue";
import axios from "axios";

// 使用 ref 创建响应式的数据
const step = ref(1);
const token = localStorage.getItem("userToken");
const dateData = reactive({
  year: null,
  month: null,
});

const years = [...Array(new Date().getFullYear() - 1999).keys()].map(
  (i) => 2000 + i
);
const months = Array.from({ length: 12 }, (_, i) => i + 1);

const savedStatus = ref({
  form_1: false,
  form_2: false,
  form_3: false,
  form_4: false,
});

const formData1 = new FormData();
const formData2 = new FormData();
const formData3 = new FormData();
const formData4 = new FormData();

const canProceed = computed(() => {
  if (step.value === 1) {
    return savedStatus.value.form_1;
  } else if (step.value === 2) {
    return savedStatus.value.form_2;
  } else if (step.value === 3) {
    return savedStatus.value.form_3;
  } else if (step.value === 4) {
    return savedStatus.value.form_4;
  } else {
    return false;
  } // 根据当前步骤调整
});

function handleUpdateData1(data) {
  //updateData1.value = data;
  savedStatus.value.form_1 = true;
  //formData1.set("data", JSON.stringify(data));
  Object.keys(data).forEach((key) => {
    formData1.append(key, data[key]);
  });
}
function handleUpdateData2(data) {
  //updateData2.value = data;
  savedStatus.value.form_2 = true;
  //formData2.set("data", JSON.stringify(data));
  Object.keys(data).forEach((key) => {
    formData2.append(key, data[key]);
  });
}
function handleUpdateData3(data) {
  //updateData3.value = data;
  savedStatus.value.form_3 = true;
  //formData3.set("data", JSON.stringify(data));
  Object.keys(data).forEach((key) => {
    formData3.append(key, data[key]);
  });
}
function handleUpdateData4(data) {
  //updateData4.value = data;
  savedStatus.value.form_4 = true;
  //formData4.set("data", JSON.stringify(data));
  Object.keys(data).forEach((key) => {
    formData4.append(key, data[key]);
  });
}
const responseStatus = ref({
  form_1: false,
  form_2: false,
  form_3: false,
  form_4: false,
});
function submitForm1() {
  formData1.append("year", dateData.year);
  formData1.append("month", dateData.month);
  axios
    .post("http://47.122.24.142:7766/api/scope1", formData1, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        responseStatus.value.form_1 = true;
        console.log(response.data);
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function submitForm2() {
  formData2.append("year", dateData.year);
  formData2.append("month", dateData.month);
  axios
    .post("http://47.122.24.142:7766/api/scope2", formData2, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        responseStatus.value.form_2 = true;
        console.log(response.data);
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function submitForm3() {
  formData3.append("year", dateData.year);
  formData3.append("month", dateData.month);
  axios
    .post("http://47.122.24.142:7766/api/scope3", formData3, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        responseStatus.value.form_3 = true;
        console.log(response.data);
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function submitForm4() {
  formData4.append("year", dateData.year);
  formData4.append("month", dateData.month);
  axios
    .post("http://47.122.24.142:7766/api/offset", formData4, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        responseStatus.value.form_4 = true;
        console.log(response.data);
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}
function submitForm() {
  if (token === null) {
    Notify.create({
      color: "negative",
      position: "top",
      message: "请先登录",
      icon: "report_problem",
    });
    return;
  }
  // 验证必要字段
  if (dateData.year === null || dateData.month === null) {
    Notify.create({
      color: "negative",
      position: "top",
      message: "必须填写年份和月份",
      icon: "report_problem",
    });
    return;
  }
  console.log(dateData.year, dateData.month);
  formData1.append("year", dateData.year);
  formData1.append("month", dateData.month);
  console.log(formData1);
  submitForm1();
  submitForm2();
  submitForm3();
  submitForm4();
  if (
    responseStatus.value.form_1 &&
    responseStatus.value.form_2 &&
    responseStatus.value.form_3 &&
    responseStatus.value.form_4
  ) {
    Notify.create({
      color: "green-4",
      textColor: "white",
      icon: "cloud_done",
      message: "录入成功",
    });
  }
}
</script>
