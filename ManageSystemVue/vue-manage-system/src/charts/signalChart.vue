<template>
  <div ref="chart" id="chart"></div>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import service from "../utils/request";

type EChartsOption = echarts.EChartsOption;
let option: EChartsOption;
const chart = ref<HTMLDivElement | null>(null);

let signalStrength;

const load = () => {
  service.get('/vital/getTheLatest').then((res) => {
    signalStrength = res.data.signalStrength
  })

}
onMounted(() => {
  load()
  const myChart = echarts.init(chart.value!);
  // 定义初始数据
  let value = 50;

  // 设置定时器，每隔一段时间更新数据
  setInterval(() => {
    // 生成一个介于-2到2之间的随机数
    const randomDelta = (Math.random() - 0.6) * 4;
    // 计算新的值
    value += randomDelta;
    // 限制数据在30到80之间
    value = Math.max(30, Math.min(80, value));
    // 更新图表数据
    myChart.setOption({
      series: [{
        data: [signalStrength + 100]
      }]
    });
  }, 200); // 间隔为2秒

  option = {
    title: {
      text: '信号强度',
      left: 'center',

      textStyle: {
        color: '#00c4ff',
        fontSize: 20
      }
    },


    tooltip: {
      formatter: ' <br/>{b}{c}db'
    },

    series: [{
      name: 'sign',
      type: 'gauge',
      progress: {
        show: true
      },
      detail: {
        formatter: '{value}',
        textStyle: {
          fontSize: 14
        }
      },
      data: [{
        value: value.toFixed(1),
        name: 'SCORE'
      }]
    }]
  };

  option && myChart.setOption(option);
});
</script>
