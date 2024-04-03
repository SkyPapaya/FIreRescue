<template>
  <div ref="chart"></div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import * as echarts from 'echarts';

const chart = ref<HTMLDivElement | null>(null);
type EChartsOption = echarts.EChartsOption;
let option: EChartsOption = {
  title: {
    text: '设备数据'
  },
  dataset: [
    {
      dimensions: ['name', 'value'],
      source: [
        ['humidity', 63],
        ['temperature', 75],
        ['people', 15],
        ['fire_exist', 69],
        ['co', 25],
        ['smoke', 43],
      ]
    },
    {
      transform: {
        type: 'sort',
        config: { dimension: 'value', order: 'desc' } // 根据第二个数据进行排序
      }
    }
  ],
  xAxis: {
    type: 'category',
    axisLabel: { interval: 0, rotate: 30 }
  },
  yAxis: {
    min: 0,
    max: 100
  },
  series: {
    type: 'bar',
    encode: { x: 'name', y: 'value' }, // 编码修改为正确的名称
    datasetIndex: 1,
    itemStyle: {
      color: function(params: any) {
        const value = params.data[1]; // 获取 y 值
        if (value > 80) {
          return 'red'; // y 值大于 80 时柱状图颜色为红色
        } else if (value > 50) {
          return 'yellow'; // y 值大于 50 小于等于 80 时柱状图颜色为黄色
        } else {
          return 'blue'; // y 值小于等于 50 时柱状图颜色为蓝色
        }
      }
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: { type: 'shadow' },
    formatter: function(params) {
      const data = params[0].data;
      return `${data[0]}：<br/>${data[1]}`;
    }
  }
};

onMounted(() => {
  const myChart = echarts.init(chart.value!);
  myChart.setOption(option);

  // 模拟数据动态更新
  setInterval(() => {
    option.dataset[0].source.forEach((item: any) => {
      item[1] = Math.round(Math.random() * 100); // 更新第二个数据
    });
    option.dataset[0].source.sort((a: any, b: any) => b[1] - a[1]); // 根据第二个数据排序
    myChart.setOption(option); // 更新图表
  }, 10000);
});
</script>
