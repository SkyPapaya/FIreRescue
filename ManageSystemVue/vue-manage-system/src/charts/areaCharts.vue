<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';

type EChartsOption = echarts.EChartsOption;

let option: EChartsOption;

let base = +new Date();
let oneDay = 24 * 3600 * 1000;
let date = [];
let data = [Math.random() * 300];
var now = new Date((base -= oneDay));
const money = [114,450,124,187,845,126,665,425,788,115,351,251,452,321,612,351,327,368,218]
for (let i = 1; i < 20; i++) {
  now = new Date(base -= oneDay);

  date.push([now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/'));
  data.push (money[i]);
}

// 反转日期和数据数组
date.reverse();
data.reverse();

const chart = ref<HTMLDivElement | null>(null);

// myChart和其他函数要放在onMounted里面，否则会报错
onMounted(() => {
  const myChart = echarts.init(chart.value!);

  window.addEventListener('resize', () => {
    myChart.resize();
  })

  option = {
    tooltip: {
      trigger: 'axis',
      position: function (pt) {
        return [pt[0], '10%'];
      }
    },
    title: {
      left: 'center',
      text: '火灾造成的经济损失'
    },
    toolbox: {
      feature: {
        dataZoom: {
          yAxisIndex: 'none'
        },
        restore: {},
        saveAsImage: {}
      }
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: date
    },
    yAxis: {
      type: 'value',
      boundaryGap: [0, '100%']
    },
    dataZoom: [
      {
        type: 'inside',
        start: 0,
        end: 10
      },
      {
        start: 0,
        end: 10
      }
    ],
    series: [
      {
        name: 'Fake Data',
        type: 'line',
        symbol: 'none',
        sampling: 'lttb',
        itemStyle: {
          color: 'rgb(255, 70, 131)'
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: 'rgb(255, 158, 68)'
            },
            {
              offset: 1,
              color: 'rgb(255, 70, 131)'
            }
          ])
        },
        data: data
      }
    ]
  };

  myChart.setOption(option);
});
</script>
