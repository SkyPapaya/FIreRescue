<template>
  <div class="container">
    <el-image class="heart" style="width: 100px; height: 100px ; display: inline ; position: absolute" :src="urlHeart"
              :fit="fit "/>
    <sign class="chart"></sign>
    <img class="breath" style="width: 115px; height: 90px ; display: inline ; position: absolute" src="../img/nose.gif"/>
    <heat class="chart"></heat>
    <breath class="chart"></breath>
    <div class="chart">
      <el-card :style="{ width: '480px', margin: '30px', color: distanceColor }" shadow="hover">{{
          distanceContent
        }}
      </el-card>
      <el-card :style="{ width: '480px', margin: '30px', color: actionColor }" shadow="hover">{{
          actionContent
        }}
      </el-card>
      <el-card :style="{ width: '480px', margin: '30px', color: warningColor }" shadow="hover">{{
          warningContent
        }}
      </el-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue';
import sign from '../charts/signalChart.vue'
import heat from '../charts/heatRateChart.vue'
import breath from '../charts/breathRateChart.vue'
import service from "../utils/request";

const fit = ['fill', 'contain', 'cover', 'none', 'scale-down']
const urlHeart = 'https://www.bing.com/th/id/OGC.f7cd7f65fa8e2f5802dfd72331b41bd9?pid=1.7&rurl=https%3a%2f%2fwimg.588ku.com%2fgif%2f20%2f08%2f03%2f89debc955a204f3ef20ca5c7192dbc2e.gif&ehk=iGwXJVDKxVEosD3vWAtCOXDVvqgtqx2vf1slUpJcHeY%3d'
const urlBreath = '../img/nose.gif'
const actionContent = ref("Initial content");
const warningContent = ref("Initial content");
const distanceContent = ref("Initial content");

const actionColor = ref("black");
const warningColor = ref("black");
const distanceColor = ref("black");

let distance;
let active;

const load = () => {
  service.get('/vital/getTheLatest').then((res) => {
    distance = res.data.distance;
    active = res.data.active;
  });
};

onMounted(() => {
  // 设置定时器每秒更新一次数据
  setInterval(() => {
    load();
    // 随机切换 actionContent 和 warningContent 的值
    const actionValues = {
      0: {value: "无人", color: "black"},
      1: {value: "静息", color: "#00c4ff"},
      2: {value: "安静", color: "#4bfc4e"},
      3: {value: "动作", color: "#ffa02c"},
      4: {value: "持续动作", color: "red"}
    };

    const warningValues = ["正常", "异常"];
    actionContent.value = actionValues[active].value;
    //设置为设备状态正常
    warningContent.value = warningValues[0];

    // 设置字体颜色
    actionColor.value = actionValues[active].color;
    warningColor.value = warningContent.value === "异常" ? "red" : "black";

    // 随机生成距离，保留一位小数，范围在 0 到 10 之间
    distanceContent.value = `距离: ${distance} cm`;
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

.heart {
  right: 27%;
  top: 5%;
}

.breath {
  border-radius: 20px;
  left: 9%;
  bottom:40%;

}
</style>
