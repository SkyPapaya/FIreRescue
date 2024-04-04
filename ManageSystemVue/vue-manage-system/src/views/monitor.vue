<template>
  <div class="container">
    <sign class="chart">{{ signContent }}</sign>
    <heat class="chart">{{ heatContent }}</heat>
    <breath class="chart">{{ breathContent }}</breath>
    <div class="chart">
      <el-card :style="{ width: '480px', margin: '30px', color: distanceColor }" shadow="hover">{{ distanceContent }}</el-card>
      <el-card :style="{ width: '480px', margin: '30px', color: actionColor }" shadow="hover">{{ actionContent }}</el-card>
      <el-card :style="{ width: '480px', margin: '30px', color: warningColor }" shadow="hover">{{ warningContent }}</el-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import sign from '../charts/signalChart.vue'
import heat from '../charts/heatRateChart.vue'
import breath from '../charts/breathRateChart.vue'

const signContent = ref("Initial content");
const heatContent = ref("Initial content");
const breathContent = ref("Initial content");
const actionContent = ref("Initial content");
const warningContent = ref("Initial content");
const distanceContent = ref("Initial content");
const actionColor = ref("black");
const warningColor = ref("black");
const distanceColor = ref("black");

onMounted(() => {
  // 设置定时器每秒更新一次数据
  setInterval(() => {
    // 更新内容，保留一位小数
    signContent.value = `Signal: ${(Math.random() * 100).toFixed(1)}`;
    heatContent.value = `Heat Rate: ${(Math.random() * 100).toFixed(1)}`;
    breathContent.value = `Breath Rate: ${(Math.random() * 100).toFixed(1)}`;

    // 随机切换 actionContent 和 warningContent 的值
    const actionValues = ["活动", "静息"];
    const warningValues = ["正常", "异常"];
    actionContent.value = actionValues[Math.floor(Math.random() * actionValues.length)];
    warningContent.value = warningValues[Math.floor(Math.random() * warningValues.length)];

    // 当 actionContent 的值为 "活动" 时，将字体颜色设置为蓝色
    actionColor.value = actionContent.value === "活动" ? "#00c4ff" : "black";
    warningColor.value = warningContent.value === "异常" ? "red" : "black";

    // 随机生成距离，保留一位小数，范围在 0 到 10 之间
    distanceContent.value = `Distance: ${(Math.random() * 10).toFixed(1)}`;
    distanceColor.value = "black"; // 默认将字体颜色设置为黑色
  }, 1000);
});
</script>

<style>
.chart {
  margin-top: 10px;
  width: 45%;
  height: 45%;
}

.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between
}
</style>
