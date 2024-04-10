<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts';
import {ref, onMounted} from 'vue';
import service from "../utils/request";

const chart = ref<HTMLDivElement | null>(null);
let now = new Date();
let data: any[] = [];
let xAxisData: string[] = [];
let option: echarts.EChartsOption;
let breathRate;
const load = () => {
  service.get('/vital/getTheLatest').then((res) => {
    breathRate = res.data.breathRate
  })
}

//获取呼吸频率
function getBreathRate() {
  now = new Date(now.getTime() + 1000);
  return {
    //以时分秒作为横坐标
    name: now.toLocaleTimeString(),
    value: [
      now.toLocaleTimeString(),
      Math.round(breathRate)
    ]
  };
}

//初始化图表
for (var i = 0; i < 100; i++) {
  const newData = getBreathRate();
  data.push(newData.value);
  xAxisData.push(newData.name);
}


onMounted(() => {
  const myChart = echarts.init(chart.value!);
  window.addEventListener('resize', () => {
    myChart.resize();
  });

  setInterval(function () {
    load();
    const newData = getBreathRate();
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

    // 更新标记点的位置
    myChart.setOption({
      graphic: [{
        type: 'text',
        left: 'center',
        top: 10,
        style: {
          text: `实时呼吸频率: ${newData.value[1]}`,
          textAlign: 'center',
          fill: '#4afafa',
          fontSize: 24
        }
      }]
    });
  }, 1000); // 每1秒刷新一次

  myChart.setOption(option);
});
option = {
  title: {
    text: '呼吸频率',

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
    data: xAxisData
  },
  yAxis: {
    type: 'value',
    boundaryGap: [0, '100%'],
    splitLine: {
      show: false
    },
    min: 0,
    max: 200
  },
  series: [
    {
      name: 'Breath Rate',
      type: 'line',
      showSymbol: false,
      data: data,
      lineStyle: {
        color: '#ffa02c'
      }
    }
  ]
};
</script>
