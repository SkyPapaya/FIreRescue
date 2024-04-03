<template>
  <div class="container" style="display: flex ; flex-wrap: wrap ; justify-content: space-between">

    <div id="area-chart" class="chart">
      <areaCharts style="width: 100% ; height: 100%"></areaCharts>
    </div>

    <div id="environment-chart" class="chart">
      <environmentChart style="width: 100% ; height: 100%"></environmentChart>
    </div>

    <div id="type-chart" class="chart">
      <typeChart style="width: 100% ; height: 100%"> 66</typeChart>
    </div>

    <div class="chart">
      <deviceChart style="width: 100% ; height: 100%"></deviceChart>
    </div>

  </div>
</template>

<script setup lang="ts" name="basecharts">
import areaCharts from '../charts/areaCharts.vue';
import environmentChart from '../charts/riskChart.vue';
import typeChart from '../charts/typeChart.vue';
import deviceChart from '../charts/device.vue';

const option = areaCharts

</script>

<style scoped>
.container{
  width:100%;
  height: 100%;
}
.chart {
  margin-top: 10px;
  width: 45%;
  height: 45%;
  margin-right: 10px;
}

</style>
