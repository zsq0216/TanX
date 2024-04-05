<template>
  <q-card class="my-card">
    <q-card-section>
      <div class="text-h5">待办事项</div>
    </q-card-section>
    <q-separator />

    <q-card-section>
      <div class="text-h6">排放数据提醒</div>
      <q-expansion-item
        label="排放数据提醒"
        :caption="'您有 ' + (emissions?.length || 0) + ' 条新的排放数据消息'"
      >
        <q-list>
          <q-item
            v-for="(emissions, index) in emissions"
            :key="'emissions-' + index"
            clickable
            v-ripple
          >
            <q-item-section>{{ emissions }}</q-item-section>
          </q-item>
        </q-list>
      </q-expansion-item>

      <q-separator />

      <div class="text-h6">企业信息提醒</div>
      <q-expansion-item
        label="企业信息提醒"
        :caption="'您有 ' + (info?.length || 0) + ' 条新的企业信息消息'"
      >
        <q-list>
          <q-item
            v-for="(info, index) in info"
            :key="'info-' + index"
            clickable
            v-ripple
          >
            <q-item-section>{{ info }}</q-item-section>
          </q-item>
        </q-list>
      </q-expansion-item>
    </q-card-section>

    <!-- <q-card-section v-else>
      <div class="text-subtitle1">没有新的消息。</div>
    </q-card-section> -->
  </q-card>
</template>

<script setup>
import {
  QCard,
  QCardSection,
  QList,
  QItem,
  QItemSection,
  QSeparator,
} from "quasar";

const props = defineProps({
  emissions: Array,
  info: Array,
});
</script>

<style scoped>
.my-card {
  width: 100%;
  max-width: 400px;
}
</style>
