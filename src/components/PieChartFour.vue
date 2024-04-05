<template>
  <div>
    <q-card :class="$q.dark.isActive ? 'bg-dark' : ''">
      <q-card-section class="text-h6">总排放 </q-card-section>
      <q-separator />
      <q-card-section>
        <div
          ref="pieChartContainer"
          class="q-mt-md"
          style="height: 250px"
        ></div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from "vue";
import * as echarts from "echarts";
import { CanvasRenderer } from "echarts/renderers";
import { TooltipComponent, LegendComponent } from "echarts/components";
import { useQuasar } from "quasar";

const $q = useQuasar();
const pieChartContainer = ref(null);

echarts.use([CanvasRenderer, TooltipComponent, LegendComponent]);

const props = defineProps({
  emission1: Number,
  emission2: Number,
  emission3: Number,
  emission_all: Number,
});
const options = ref({
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b}: {c} ({d}%)",
  },
  legend: {
    top: "bottom",
    bottom: "5%",
    left: "center",
  },
  series: [
    {
      name: "总排放信息",
      type: "pie",
      radius: ["40%", "70%"],
      center: ["50%", "35%"],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: "#fff",
        borderWidth: 2,
      },
      label: {
        show: false,
        position: "outside",
      },
      emphasis: {
        label: {
          show: true,
          fontSize: "12",
          fontWeight: "bold",
        },
      },
      labelLine: {
        show: false,
      },
      data: [
        {
          value: props.emission1,
          name: "范围一排放",
          itemStyle: { color: "#CCDCE3" },
        },
        {
          value: props.emission2,
          name: "范围二排放",
          itemStyle: { color: "#F6C786" },
        },
        {
          value: props.emission3,
          name: "范围三排放",
          itemStyle: { color: "#D5B386" },
        },
      ],
    },
    {
      name: "总排放量",
      type: "pie",
      radius: ["0", "30%"], // 内半径为0，外半径为30%，形成一个圆
      center: ["50%", "35%"], // 与环形图中心相同
      label: {
        normal: {
          position: "center",
          formatter: `{c} \n万吨`, // 标签格式化
          textStyle: {
            fontSize: "15",
            fontWeight: "bold",
          },
        },
      },

      itemStyle: {
        color: "rgba(0, 0, 0, 0)", // 设置颜色为透明
        borderColor: "auto", // 可以设置边框颜色
        borderWidth: 2, // 边框宽度
      },

      data: [{ value: props.emission_all, name: "总排放量" }],
    },
  ],
});
onMounted(() => {
  nextTick().then(() => {
    if (pieChartContainer.value) {
      const myChart = echarts.init(pieChartContainer.value);
      myChart.setOption(options.value);
    }
  });
});
</script>
