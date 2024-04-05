<template>
  <div class="q-pa-md column justify-center items-center">
    <h2 class="text-h4">历史排放数据</h2>
    <q-markup-table  flat bordered class="col-10">
      <thead>
        <tr>
          <th class="text-left">时间</th>
          <th class="text-right">范围一排放 (吨CO2)</th>
          <th class="text-right">范围二排放 (吨CO2)</th>
          <th class="text-right">范围三排放 (吨CO2)</th>
          <th class="text-right">总排放 (吨CO2)</th>
          <th class="text-right">碳抵消 (吨CO2)</th>
          <th class="text-right">认证情况</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in history_data" :key="index">
          <td>{{ `${item.year} - ${item.month}` }}</td>
          <td>{{ item.emission1 }}</td>
          <td>{{ item.emission2 }}</td>
          <td>{{ item.emission3 }}</td>
          <td>{{ item.emission_all }}</td>
          <td>{{ item.offset }}</td>
          <td>
            <q-chip
              :color="getCertifiedColor(item.certified)"
              style="color: white"
            >
              {{ getCertifiedLabel(item.certified) }}
            </q-chip>
          </td>
        </tr>
      </tbody>
    </q-markup-table>
    <q-pagination
      v-model="pagination.page"
      :max="history_page_max"
      class="q-my-md"
      @update:model-value="handlePageChange"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from "vue";
import axios from "axios";
// const separator = ref("vertical");
const username = localStorage.getItem("userName");
const requestData = reactive({
  page: 1,
  pagelength: 10,
  username: username,
});
//const token = localStorage.getItem("token");
const history_num = ref();
const history_page_max = ref();
const history_data = ref({});
const pagination = reactive({
  page: 1,
});

const props = defineProps({
  token: String,
});
function handlePageChange(newPage) {
  pagination.page = newPage;
  fetchData();
}
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
function fetchData() {
  requestData.page = pagination.page;
  const formData = new FormData();
  Object.keys(requestData).forEach((key) => {
    formData.append(key, requestData[key]);
  });
  axios
    .post("http://47.122.24.142:7766/api/gethistory", formData, {
      headers: {
        Authorization: `Bearer ${props.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        history_num.value = response.data.history_num;
        history_page_max.value = response.data.history_page_max;
        history_data.value = response.data.history_data;
      } else {
        console.error("Error fetching data:", response.status);
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}
onMounted(() => {
  fetchData();
});
</script>
