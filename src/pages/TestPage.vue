<template>
  <q-layout>
    <q-page-container>
      <q-page class="q-pa-md row items-start justify-center">
        <div class="col-7 q-mb-md q-gutter-md">
          <q-card>
            <q-card-section class="text-h4"> 排放信息详情 </q-card-section>
            <q-card-section v-if="needToInputInfo">
              请先录入信息
            </q-card-section>
            <q-card-section v-if="apiData.show_data">
              <ChartComponent
                :fixburn="apiData.show_data.fixburn"
                :movingburn="apiData.show_data.movingburn"
                :emission1="apiData.show_data.emission1"
                :electricity="apiData.show_data.electricity"
                :heating="apiData.show_data.heating"
                :emission2="apiData.show_data.emission2"
                :commuting="apiData.show_data.commuting"
                :travel="apiData.show_data.travel"
                :emission3="apiData.show_data.emission3"
                :emission_all="apiData.show_data.emission_all"
                :offset = "apiData.show_data.offset"
              />
            </q-card-section>
          </q-card>


        </div>

        <div class="col-4 q-ml-md">
          <q-card class="fit">
            <UserProfile
              v-if="apiData"
              :enterpriseName="apiData.Enterprise_Name"
              :enterpriseIntro="apiData.Enterprise_Intro"
              :enterpriseLegalperson="apiData.Enterprise_Legalperson"
              :username="apiData.username"
              :email="apiData.email"
              @update:enterpriseIntro="handleUpdateEnterpriseIntro"
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
import { useStore } from "vuex";
import { ref, onMounted } from "vue";
import axios from "axios";
import UserProfile from "src/components/UserProfile.vue";
import ChartComponent from "src/components/ChartComponent.vue";
import MessageAlert from "src/components/MessageAlert.vue";

const apiData = ref({}); // 用于存储从 API 接收到的数据
const messageData = ref({}); // 存储消息数据
const isLoading = ref(true); // 用于表示加载状态
const needToInputInfo = ref(false); // 用于显示是否需要输入信息

const store = useStore();
//const token = computed(() => store.getters.token);
const token = localStorage.getItem("userToken");

function handleUpdateEnterpriseIntro(value1,value2) {
  apiData.value.Enterprise_Intro = value1;
  apiData.value.Enterprise_Legalperson = value2;
}
function fetchData() {
  console.log("in peasonal page");
  console.log(token);
  axios
    .get("http://47.122.24.142:7766/api/getemissioninfo", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        console.log(response.data);
        apiData.value = response.data;
        console.log(apiData.value.Enterprise_Name);
      } else if (response.status === 202) {
        needToInputInfo.value = true;
      }
      isLoading.value = false;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      isLoading.value = false;
    });
}

function fetMessage() {
  isLoading.value = true;
  axios
    .get("http://47.122.24.142:7766/api/getmassage", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    .then((response) => {
      messageData.value = response.data;

      isLoading.value = false;
    })
    .catch((error) => {
      console.error("Error fetching message:", error);
      isLoading.value = false;
    });
}

onMounted(() => {
  fetchData();
  fetMessage();
});
</script>

<style>
/* CSS styling to match the uploaded image */
</style>
