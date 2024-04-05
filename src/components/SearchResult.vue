<template>
  <q-table
    :rows="emissionData"
    :columns="columns"
    row-key="username"
  >
    <template v-slot:body-cell-enterpriseName="props">
      <q-td :props="props">
        <div
          v-html="props.row.Enterprise_name"
          @click.stop="
            navigateToDetail(
              props.row.username,
              props.row.year,
              props.row.month
            )
          "
        ></div>
      </q-td>
    </template>
    <template v-slot:body-cell-certified="props">
      <q-td :props="props">
        <q-chip :color="getCertifiedColor(props.row.certified)" style="color: white;">
          {{ getCertifiedLabel(props.row.certified) }}
        </q-chip>
      </q-td>
    </template>
  </q-table>
  <!-- <q-pagination
    v-model="currentPage"
    :max="maxPages"
    @update:model-value="handlePageChange"
  /> -->
</template>

<script setup>
import { ref, watch } from "vue";
import { useRouter } from "vue-router";
import { QPagination } from 'quasar';
import { useStore } from "vuex";

const router = useRouter();
const store = useStore();

const props = defineProps({
  emissionData: {
    type: Array,
    default: () => [],
  },
  currentPage: Number,
  maxPages: Number
});

const emit = defineEmits(['update-page']);

const currentPage = ref(props.currentPage);
function navigateToDetail(username, year, month) {
  localStorage.setItem("userName", username);
  console.log(username, year, month);
  store.commit("setCurrentYear", year);
  store.commit("setCurrentMonth", month);

  router.push({ path: "/detail" });
}
const handlePageChange = (newPage) => {
  currentPage.value = newPage;
  emit('update-page', newPage);
};
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

const columns = [
  {
    name: "enterpriseName",
    label: "公司名称",
    field: "Enterprise_name",
    sortable: true,
  },
  { name: "certified", label: "认证状态", field: "certified", sortable: true },
  {
    name: "combinedDate",
    label: "年/月",
    align: "left",
    field: (row) => `${row.year}-${row.month.toString().padStart(2, "0")}`,
    sortable: true,
  },
  { name: "emission1", label: "排放1", field: "emission1", sortable: true },
  { name: "emission2", label: "排放2", field: "emission2", sortable: true },
  { name: "emission3", label: "排放3", field: "emission3", sortable: true },
  {
    name: "emissionAll",
    label: "总排放",
    field: "emission_all",
    sortable: true,
  },
  {
    name: "offset",
    label: "碳排放抵消",
    field: "offset",
    sortable: true,
  },
];
</script>
