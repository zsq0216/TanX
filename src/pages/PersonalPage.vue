<template>
  <q-layout>
    <q-page-container>
      <q-page class="q-pa-md row items-start justify-center">
        <div class="col-8 q-mb-md q-gutter-md">
          <q-card>
            <div class="row">
              <q-card-section class="text-h4 col-4"> 排放信息详情 </q-card-section>
              <q-form @submit="fetchData" class="col-12 q-pa-md">
                <div class="row col-5">
                  <q-select
                    outlined
                    v-model="requestData.year"
                    :options="years"
                    label="年份"
                    type="number"
                    class="col-2"
                    padding
                  >
                    <template v-slot:prepend>
                      <q-icon name="event" />
                    </template>
                  </q-select>
                  <q-select
                    outlined
                    v-model="requestData.month"
                    :options="months"
                    label="月份"
                    type="number"
                    class="col-2"
                    padding
                  >
                    <template v-slot:prepend>
                      <q-icon name="event" />
                    </template>
                  </q-select>
                  <q-btn
                    label="查询"
                    type="submit"
                    color="primary"
                    class="col-2 q-px-md"
                  />
                </div>
              </q-form>
            </div>
            <q-card-section v-if="showData">
              <ChartComponent
                :key="componentKey"
                :fixburn="showData.fixburn"
                :movingburn="showData.movingburn"
                :emission1="showData.emission1"
                :electricity="showData.electricity"
                :heating="showData.heating"
                :emission2="showData.emission2"
                :commuting="showData.commuting"
                :travel="showData.travel"
                :emission3="showData.emission3"
                :emission_all="showData.emission_all"
                :offset="showData.offset"
              />
            </q-card-section>
            <q-card-section v-if="showData">
              <q-chip
                :color="getCertifiedColor(showData.certified)"
                style="color: white"
              >
                {{ getCertifiedLabel(showData.certified) }}
              </q-chip>
              <q-btn
                label="下载报告"
                color="primary"
                @click="downloadReport"
                v-if="showData.certified === 'all'"
              />
            </q-card-section>
          </q-card>
          <q-card>
            <q-card-sectiont>
              <HistoryList
              :token="token"  />
            </q-card-sectiont>
          </q-card>
        </div>

        <div class="col-3 q-ml-md">
          <q-card class="fit">
            <UserProfile
              v-if="apiData"
              :enterpriseName="apiData.Enterprise_Name"
              :enterpriseIntro="apiData.Enterprise_Intro"
              :enterpriseLegalperson="apiData.Enterprise_Legalperson"
              :username="apiData.username"
              :email="apiData.email"
            />
          </q-card>
          <q-card class="q-my-md">
            <MessageAlert
              v-if="messageData"
              :emissions="messageData.emissions"
              :info="messageData.info"
            />
          </q-card>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useStore } from "vuex";
import { Notify } from "quasar";
import axios from "axios";

import HistoryList from "src/components/HistoryList.vue";
import ChartComponent from "src/components/ChartComponent.vue";
import UserProfile from "src/components/UserProfile.vue";
import MessageAlert from "src/components/MessageAlert.vue";

const store = useStore();

const username = localStorage.getItem("userName");

const token = localStorage.getItem("userToken");

const requestData = reactive({
  month: null,
  year: null,
  username: username,
});

const componentKey = computed(
  () => `${showData.value.year}-${showData.value.month}`
);

const showData = ref();
const apiData = ref();
const messageData = ref({});

const years = [...Array(new Date().getFullYear() - 1999).keys()].map(
  (i) => 2000 + i
);
const months = Array.from({ length: 12 }, (_, i) => i + 1);

function getCertifiedLabel(certifiedValue) {
  switch (certifiedValue) {
    case "all":
      return "全部认证";
    case "part":
      return "部分认证";
    case "none":
      return "未认证";
    default:
      return "未知";
  }
}

function getCertifiedColor(certifiedValue) {
  switch (certifiedValue) {
    case "all":
      return "green";
    case "part":
      return "orange";
    case "none":
      return "red";
    default:
      return "grey";
  }
}
function downloadReport() {
  const uploadData = new FormData();
  uploadData.append("username", requestData.username);
  uploadData.append("month", requestData.month);
  uploadData.append("year", requestData.year);
  axios
    .post("http://47.122.24.142:7766/api/getenterprisereport", uploadData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        const loc = response.data.loc;
        console.log(loc);
        window.location.href = "http://47.122.24.142:7766"+loc;
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}
function fetchData() {
  console.log("in detailed info page");
  console.log(token);
  console.log(username);

  if (
    requestData.username == null ||
    requestData.month == null ||
    requestData.year == null
  ) {
    Notify.create({
      color: "red-5",
      textColor: "white",
      icon: "error",
      message: "查询条件不能为空！",
    });
  }
  const formData = new FormData();
  Object.keys(requestData).forEach((key) => {
    formData.append(key, requestData[key]);
  });
  axios
    .post("http://47.122.24.142:7766/api/getenterpriseinfo", formData, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        showData.value = response.data.show_data;
        apiData.value = response.data;
        console.log(apiData.value);
        console.log(apiData);
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}
function fetMessage() {
  axios
    .get("http://47.122.24.142:7766/api/getmassage", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      messageData.value = response.data;
    })
    .catch((error) => {
      console.error("Error fetching message:", error);
    });
}
onMounted(() => {
  requestData.month = 2;
  requestData.year = 2024;
  fetchData();
  fetMessage();
});
</script>
