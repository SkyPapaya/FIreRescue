<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';
import { ElNotification } from "element-plus";

const chart = ref<HTMLDivElement | null>(null);

let now = new Date();
let oneDay = 24 * 3600 * 1000;
let data: any[] = [];
let option: echarts.EChartsOption;

// 滑动平均法处理随机数据
let smoothedValue = 0;
const smoothingFactor = 0.2;

function randomData() {
  now = new Date(+now + oneDay);
  let newValue = Math.random() * 100;
  smoothedValue = smoothedValue * (1 - smoothingFactor) + newValue * smoothingFactor;
  return {
    name: now.toString(),
    value: [
      [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'),
      Math.round(smoothedValue)
    ]
  };
}

for (var i = 0; i < 100; i++) {
  data.push(randomData());
}

onMounted(() => {
  const myChart = echarts.init(chart.value!);
  window.addEventListener('resize', () => {
    myChart.resize();
  });

  setInterval(function () {
    checkFire();
    data.shift();
    data.push(randomData());
    myChart.setOption({
      series: [
        {
          data: data
        }
      ]
    });
  }, 1000);

  myChart.setOption(option);
});

const checkFire = () => {
  console.log(data.some((item: any) => item.value[1] ));
  if (data.some((item: any) => item.value[1] > 80)) {
    ElNotification({
      title: 'Error',
      message: '有火灾风险',
      type: 'error',
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
    type: 'time',
    splitLine: {
      show: true
    },
    axisLabel: {
      formatter: function (value: string | number | Date) {
        let date = new Date(value);
        return "";
      },
      axisLabelShow: false
    },

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
