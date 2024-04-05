<template>
  <div class="column">
    <div class="row justify-evenly q-mb-md">
      <PieChartOne
        :fixburn="props.fixburn"
        :movingburn="props.movingburn"
        :emission1="props.emission1"
        class="col-5"
      />
      <PieChartTwo
        :electricity="props.electricity"
        :heating="props.heating"
        :emission2="props.emission2"
        class="col-5"
      />
    </div>
    <div class="row justify-evenly">
      <PieChartThree
        :commuting="props.commuting"
        :travel="props.travel"
        :emission3="props.emission3"
        class="col-5"
      />
      <PieChartFour
        :emission1="props.emission1"
        :emission2="props.emission2"
        :emission3="props.emission3"
        :emission_all="props.emission_all"
        class="col-5"
      />
    </div>
    <div class="row justify-center q-my-md">
      <BarChart :emission_all="props.emission_all" :offset="props.offset" class="col-11"/>
    </div>
  </div>
</template>

<script setup>
import PieChartOne from "src/components/PieChartOne.vue";
import PieChartTwo from "src/components/PieChartTwo.vue";
import PieChartThree from "src/components/PieChartThree.vue";
import PieChartFour from "src/components/PieChartFour.vue";
import BarChart from "src/components/BarChart.vue";

const props = defineProps({
  fixburn: Number,
  movingburn: Number,
  emission1: Number,
  electricity: Number,
  heating: Number,
  emission2: Number,
  commuting: Number,
  travel: Number,
  emission3: Number,
  emission_all: Number,
  offset: Number,
});
</script>
