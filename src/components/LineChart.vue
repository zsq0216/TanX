<template>
  <div>
    <q-card :class="$q.dark.isActive ? 'bg-dark' : ''">
      <q-card-section class="text-h6"> Line Chart </q-card-section>
      <q-card-section>
        <!-- <ECharts
          ref="barchart"
          :option="options"
          class="q-mt-md"
          :resizable="true"
          autoresize
          style="height: 250px"
        /> -->
        <div
          ref="lineChartContainer"
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

echarts.use([CanvasRenderer, TooltipComponent, LegendComponent]);
const $q = useQuasar();
const lineChartContainer = ref(null);

const props = defineProps({
  linesData: {
    type: Array,
    default: () => [],
  },
});

let myChart = null;

const processedData = linesData.map((item) => ({
  date: `${item.year}-${item.month.toString().padStart(2, "0")}`, // 将年和月组合成 "YYYY-MM" 格式
  value: item.value,
}));

// 创建图表实例的方法
const initChart = () => {
  if (lineChartContainer.value && props.linesData.length) {
    myChart = echarts.init(lineChartContainer.value);

    // 提取时间字段作为 x 轴的数据
    const dates = props.linesData.map((item) => item.date);
    const emission_1 = props.linesData.map((item) => item.emission1);
    const emission_2 = props.linesData.map((item) => item.emission2);
    const emission_3 = props.linesData.map((item) => item.emission3);
    const emission_offset = props.linesData.map((item) => item.off_set);

    myChart.setOption({
      color: ["#80FFA5", "#37A2FF", "#00DDFF", "#FF0087", "#FFBF00"],
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "cross",
          label: {
            backgroundColor: "#6a7985",
          },
        },
      },
      legend: {
        data: ["Line 1", "Line 2"],
        bottom: 10,
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "20%",
        top: "5%",
        containLabel: true,
      },
      xAxis: {
        type: "category",
        data: dates, // 使用时间数据作为 x 轴数据
      },
      series: [
        {
          name: "范围一排放",
          type: "line",
          //stack: "Total",
          smooth: true,
          lineStyle: {
            width: 0,
          },
          showSymbol: false,
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: "rgba(128, 255, 165)",
              },
              {
                offset: 1,
                color: "rgba(1, 191, 236)",
              },
            ]),
          },
          emphasis: {
            focus: "series",
          },
          data: emission_1
        },
        {
          name: "范围二排放",
          type: "line",
          stack: "Total",
          smooth: true,
          lineStyle: {
            width: 0,
          },
          showSymbol: false,
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: "rgba(0, 221, 255)",
              },
              {
                offset: 1,
                color: "rgba(77, 119, 255)",
              },
            ]),
          },
          emphasis: {
            focus: "series",
          },
          data: emission_2
        },
        {
          name: "范围三排放",
          type: "line",
          stack: "Total",
          smooth: true,
          lineStyle: {
            width: 0,
          },
          showSymbol: false,
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: "rgba(55, 162, 255)",
              },
              {
                offset: 1,
                color: "rgba(116, 21, 219)",
              },
            ]),
          },
          emphasis: {
            focus: "series",
          },
          data: emission_3
        },
        {
          name: "碳抵消",
          type: "line",
          stack: "Total",
          smooth: true,
          lineStyle: {
            width: 0,
          },
          showSymbol: false,
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: "rgba(255, 0, 135)",
              },
              {
                offset: 1,
                color: "rgba(135, 0, 157)",
              },
            ]),
          },
          emphasis: {
            focus: "series",
          },
          data: [220, 402, 231, 134, 190, 230, 120],
        },
        {
          name: "Line 5",
          type: "line",
          stack: "Total",
          smooth: true,
          lineStyle: {
            width: 0,
          },
          showSymbol: false,
          label: {
            show: true,
            position: "top",
          },
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: "rgba(255, 191, 0)",
              },
              {
                offset: 1,
                color: "rgba(224, 62, 76)",
              },
            ]),
          },
          emphasis: {
            focus: "series",
          },
          data: emission_offset,
        },
      ],
    });
  }
};

// 当 linesData 改变时重新设置图表
watchEffect(() => {
  processedData();
  initChart();
});

onMounted(() => {
  processedData();
  initChart();
});
</script>
