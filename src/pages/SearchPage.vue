<template>
  <q-page padding>
    <div class="q-pa-md row justify-center">
      <q-card class="col-10 row justify-center">
        <q-form @submit="fetchData" class="col-12 q-pa-md">
          <div class="row justify-evenly items-center">
            <q-card-section class="text-h4"> 查询企业</q-card-section>
            <q-select
              outlined
              v-model="params.year"
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
              v-model="params.month"
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
            <q-select
              outlined
              v-model="params.sortkey"
              :options="sortOptions"
              label="排序方式"
              class="col-3"
              padding
            />
          </div>
          <div class="row q-py-md justify-evenly">
            <q-toggle
              v-model="params.certified"
              label="仅显示全部认证的企业"
              class="col-2.8"
            />
            <q-toggle
              v-model="params.ascending"
              label="排放量从低到高"
              class="col-2"
            />
            <q-input
              v-model="searchTerm"
              label="企业名称"
              rounded
              outlined
              class="col-4"
            >
              <template v-slot:append>
                <q-icon name="search" class="cursor-pointer" />
              </template>
            </q-input>

            <q-btn
              label="查询"
              type="submit"
              color="primary"
              class="col-2 q-px-md"
            />
          </div>
        </q-form>
      </q-card>
    </div>
    <search-result
      :emissionData="tableData"
      :current-page="params.page"
      :max-pages="params.pagelength"
      @update-page="handlePageUpdate"
    />
  </q-page>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useQuasar, Notify } from "quasar";
import axios from "axios";
import { computed } from "vue";
import { useStore } from "vuex";

import { QInput, QIcon } from "quasar";
import SearchResult from "src/components/SearchResult.vue";
const store = useStore();
//const token = computed(() => store.getters.token);
const token = localStorage.getItem("bankToken");

const searchTerm = ref("");
const years = [...Array(new Date().getFullYear() - 1999).keys()].map(
  (i) => 2000 + i
);
const months = Array.from({ length: 12 }, (_, i) => i + 1);

const $q = useQuasar();

const params = reactive({
  year: null,
  month: null,
  page: 1,
  pagelength: 10,
  sortkey: { label: "总排放量", value: "emission_all" },
  ascending: false,
  certified: false,
  searchkey: "",
});

const sortOptions = [
  { label: "固定燃烧", value: "fixburn" },
  { label: "移动燃烧", value: "movingburn" },
  { label: "范围一排放", value: "emission1" },
  { label: "购入电力", value: "electricity" },
  { label: "购入热力", value: "heating" },
  { label: "范围二排放", value: "emission2" },
  { label: "员工通勤", value: "commuting" },
  { label: "员工差旅", value: "travel" },
  { label: "范围三排放", value: "emission3" },
  { label: "总排放量", value: "emission_all" },
  { label: "碳排放抵消", value: "offset" },
];

const tableData = ref([]);
const pagination = ref({ page: 1, rowsPerPage: 10 });

const fetchData = async () => {
  console.log(token);
  console.log(params.sortkey);
  const formData = new FormData();
  Object.keys(params).forEach((key) => {
    if (key !== "sortkey") {
      formData.append(key, params[key]);
    }
  });
  formData.append("sortkey", params.sortkey.value);

  try {
    const response = await axios.post(
      "http://47.122.24.142:7766/api/getinfoall",
      formData,
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    if (response.status === 200) {
      tableData.value = response.data.data;
      console.log(tableData.value);
      pagination.value.page = response.data.page_max;
      console.log(pagination.value.page);
    } else {
      $q.notify({ color: "negative", message: "无法获取数据" });
    }
  } catch (error) {
    console.error(error);
    $q.notify({ color: "negative", message: "请求失败" });
  }
};
</script>
