<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts';
import { ref, onMounted } from 'vue';
import service from "../utils/request";

const chart = ref<HTMLDivElement | null>(null);
const fit = 'fill';
const url = './img/heart.png';
let now = new Date();
let data: any[] = [];
let xAxisData: string[] = [];
let option: echarts.EChartsOption;

let heartRate;
const load = () => {
  service.get('/vital/getTheLatest').then((res) => {
    heartRate = res.data.heartRate;
  });
};

//将这里的smoothedValue替换成获取到的数据
function randomData() {
  now = new Date(now.getTime() + 1000); // 每次增加1秒

  return {
    name: now.toLocaleTimeString(), // 使用时分秒作为名称
    value: [
      now.toLocaleTimeString(),
      Math.round(heartRate)
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
    load();
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


    // 更新标记点的位置
    myChart.setOption({
      graphic: [{
        type: 'text',
        left: 'center',
        top: 10,
        style: {
          text: `实时心率: ${newData.value[1]}`,
          textAlign: 'center',
          fill: '#ef3b3b',
          fontSize: 24
        }
      },

      ]
    });
  }, 1000); // 每1秒刷新一次

  myChart.setOption(option);
});
option = {
  title: {
    text: '心率'
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
    max: 200
  },
  series: [
    {
      name: 'Breath Rate',
      type: 'line',
      showSymbol: false,
      data: data,
      lineStyle: {
        color: '#ef3b3b'
      }
    }
  ]
};
</script>
