<template>
  <div>
    <q-card :class="$q.dark.isActive ? 'bg-dark' : ''">
      <q-card-section class="text-h6"> 碳排放抵消 </q-card-section>
      <q-separator />
      <q-card-section>
        <div
          ref="barChartContainer"
          class="q-mt-md"
          style="height: 250px"
        ></div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, computed } from "vue";
import * as echarts from "echarts";
import { CanvasRenderer } from "echarts/renderers";
import { TooltipComponent, LegendComponent } from "echarts/components";
import { useQuasar } from "quasar";

echarts.use([CanvasRenderer, TooltipComponent, LegendComponent]);
const $q = useQuasar();
const barChartContainer = ref(null);

const options = computed(() => ({
  legend: {
    bottom: 10,
  },
  tooltip: {},
  dataset: {
    source: [
      ["category", "单位: 吨CO2"],
      ["总排放量", props.emission_all],
      ["碳排放抵消", props.offset],
    ],
  },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "20%",
    top: "5%",
    containLabel: true,
  },
  xAxis: {
    type: "value",
  },
  yAxis: {
    type: "category",
    data: ["总排放量", "碳排放抵消"], // 指定 y 轴类别
  },
  series: [
    {
      type: "bar",
      itemStyle: {
        // 配置渐变色
        color: (params) => {
          const colors = [
            { start: "#BEBEBE", end: "#708090" }, // 总量的渐变色
            { start: "#C1FFC1", end: "#9BCD9B" }, // 偏移的渐变色
          ];
          const color = colors[params.dataIndex % colors.length];
          return new echarts.graphic.LinearGradient(0, 0, 1, 0, [
            { offset: 0, color: color.start },
            { offset: 1, color: color.end },
          ]);
        },
      },
    },
  ],
}));

const props = defineProps({
  emission_all: Number,
  offset: Number,
});

onMounted(() => {
  nextTick().then(() => {
    if (barChartContainer.value) {
      const myChart = echarts.init(barChartContainer.value);
      myChart.setOption(options.value);
    }
  });
});
</script>
