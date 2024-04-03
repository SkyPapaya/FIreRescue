<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';
import { ElNotification } from "element-plus";

const chart = ref<HTMLDivElement | null>(null);

let now = new Date();
let data: any[] = [];
let xAxisData: string[] = [];
let option: echarts.EChartsOption;

// 滑动平均法处理随机数据
let smoothedValue = 0;
const smoothingFactor = 0.2;

function randomData() {
  now = new Date(now.getTime() + 30000); // 每次增加30秒
  let newValue = Math.random() * 100;
  smoothedValue = smoothedValue * (1 - smoothingFactor) + newValue * smoothingFactor;
  return {
    name: now.toLocaleTimeString(), // 使用时分秒作为名称
    value: [
      now.toLocaleTimeString(),
      Math.round(smoothedValue)
    ]
  };
}

for (var i = 0; i < 100; i++) {
  const newData = randomData();
  data.push(newData.value);
  xAxisData.push(newData.name);
}

onMounted(() => {
  const myChart = echarts.init(chart.value!);
  window.addEventListener('resize', () => {
    myChart.resize();
  });

  setInterval(function () {
    checkFire();
    const newData = randomData();
    data.shift();
    xAxisData.shift();
    data.push(newData.value);
    xAxisData.push(newData.name);
    myChart.setOption({
      series: [
        {
          data: data
        }
      ],
      xAxis: [
        {
          data: xAxisData
        }
      ]
    });
  }, 10000); // 每30秒刷新一次

  myChart.setOption(option);
});

const checkFire = () => {
  console.log(data.some((item: any) => item[1] ));
  if (data.some((item: any) => item[1] > 80)) {
    ElNotification({
      title: 'Error',
      message: '有火灾风险',
      type: 'error',
      duration: 10000,
    });
  }
};

option = {
  title: {
    text: '发生火灾的风险'
  },
  tooltip: {
    trigger: 'axis',
    formatter: function (params) {
      params = params[0];
      var date = new Date(params.name);
      return (
          date.getHours() +
          ':' +
          (date.getMinutes()) +
          ':' +
          date.getSeconds() +
          ' ' +
          params.value[1]
      );
    },
    axisPointer: {
      animation: false
    }
  },
  xAxis: {
    type: 'category',
    splitLine: {
      show: true
    },
    data: xAxisData // 不再需要格式化为日期格式
  },
  yAxis: {
    type: 'value',
    boundaryGap: [0, '100%'],
    splitLine: {
      show: false
    },
    min: 0,
    max: 100
  },
  series: [
    {
      name: 'Fake Data',
      type: 'line',
      showSymbol: false,
      data: data
    }
  ]
};
</script>
