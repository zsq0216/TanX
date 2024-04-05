<template>
  <q-card class="fit">
    <q-card-section class="text-h5"> 账户信息 </q-card-section>
    <q-item>
      <q-item-section avatar>
        <q-avatar>
          <img src="../assets/R-C.jpg" />
        </q-avatar>
      </q-item-section>

      <q-item-section>
        <q-item-label class="text-h5 text-weight-bold">{{
          enterpriseName
        }}</q-item-label>
      </q-item-section>
    </q-item>

    <q-separator />

    <q-card-section class="column">
      <q-card-section>
        <span class="text-weight-bold" style="margin-right: 10px"
          >公司邮箱:
        </span>
        <span>{{ email }}</span>
      </q-card-section>
      <q-card-section>
        <span class="text-weight-bold" style="margin-right: 10px"
          >公司电话:
        </span>
        <span>{{ username }}</span>
      </q-card-section>

      <q-card-section
        ><span class="text-weight-bold" style="margin-right: 10px"
          >企业介绍:
        </span>
        <span v-if="!isEditing">{{ enterpriseIntro }}</span>
        <q-input v-else v-model="editingData.intro" dense />
      </q-card-section>

      <q-card-section>
        <span class="text-weight-bold" style="margin-right: 10px">法人: </span
        ><span v-if="!isEditing">{{ enterpriseLegalperson }}</span>
        <q-input v-else v-model="editingData.per" dense />
      </q-card-section>

      <div class="row justify-end q-mt-md">
        <q-btn v-if="!isEditing" label="编辑" color="primary" @click="onEdit" />
        <q-btn
          v-if="isEditing"
          label="保存"
          color="primary"
          @click="saveEdit"
        />
        <q-btn
          v-if="isEditing"
          label="取消"
          color="primary"
          @click="cancelEdit"
        />
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { Notify } from "quasar";

const props = defineProps({
  enterpriseName: String,
  enterpriseIntro: String,
  enterpriseLegalperson: String,
  username: String,
  email: String,
});

const editingData = ref({});
const isEditing = ref(false);
const token = localStorage.getItem("userToken");

const onEdit = () => {
  isEditing.value = true;
  editingData.value = {
    intro: props.enterpriseIntro,
    per: props.enterpriseLegalperson,
  };
};
const emit = defineEmits(["update:enterpriseIntro"]);

function handleSave() {
  // 假设处理保存逻辑...
  emit(
    "update:enterpriseIntro",
    editingData.value.intro,
    editingData.value.per
  );
}

const saveEdit = async () => {
  const url = "http://47.122.24.142:7766/api/changeinfo";
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  const formData = new FormData();
  formData.append("Enterprise_Intro", editingData.value["intro"]);
  formData.append("Enterprise_Legalperson", editingData.value["per"]);
  try {
    const response = await axios.post(url, formData, { headers });
    console.log("Success:", response.data);
    isEditing.value = false;
    handleSave();
    Notify.create({
      color: "green-4",
      textColor: "white",
      icon: "cloud_done",
      message: "信息修改成功",
    });
  } catch (error) {
    console.error("Error:", error);
  }
};

const cancelEdit = () => {
  isEditing.value = false;
};
</script>
