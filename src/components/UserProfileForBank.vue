<template>
  <q-card class="fit">
    <q-card-section class="text-h4"> 公司信息 </q-card-section>
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

      <q-card-section>
        <span class="text-weight-bold" style="margin-right: 10px"
          >企业介绍:
        </span>
        <span>{{ enterpriseIntro }}</span>
      </q-card-section>

      <q-card-section
        ><span class="text-weight-bold" style="margin-right: 10px">法人: </span>
        <span>{{ enterpriseLegalperson }}</span></q-card-section
      >
    </q-card-section>
  </q-card>
</template>

<script setup>
const props = defineProps({
  enterpriseName: String,
  enterpriseIntro: String,
  enterpriseLegalperson: String,
  username: String,
  email: String,
});
</script>
