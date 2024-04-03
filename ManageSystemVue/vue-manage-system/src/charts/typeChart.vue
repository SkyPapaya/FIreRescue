<template>
  <div ref="chart"></div>
</template>
<script setup lang="ts">
import {ref, onMounted, onBeforeUnmount} from 'vue';
import * as echarts from 'echarts';

var chartDom = document.getElementById('chart');

var option;
const chart = ref<HTMLDivElement | null>(null);

// 生成随机数据的函数
function generateRandomData() {
  // 定义时间范围
  const timeRange = Array.from({length: 13}, (_, i) => i < 10 ? '0' + i : '' + i);
  // 定义产品名称
  const products = ['电器', '粉尘', '电瓶', '厨房'];
  // 生成随机数据
  const sourceData = [timeRange];
  products.forEach(product => {
    const productData = [product];
    for (let i = 0; i < 12; i++) {
      productData.push(Math.random() * 100); // 随机生成数据
    }
    sourceData.push(productData);
  });
  return sourceData;
}

onMounted(() => {
  const myChart = echarts.init(chart.value!);

  function refreshData() {
    option.dataset.source = generateRandomData(); // 刷新数据
    myChart.setOption(option);
  }

  // 每10秒钟刷新一次数据
  const interval = setInterval(refreshData, 10000);
  option = {
    title: {text: '火灾类型统计'},
    legend: {},
    tooltip: {
      trigger: 'axis',
      showContent: false
    },
    dataset: {
      source: generateRandomData() // 使用随机数据
    },
    xAxis: {type: 'category'},
    yAxis: {gridIndex: 0},
    grid: {top: '55%'},
    series: [
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: {focus: 'series'}
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: {focus: 'series'}
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: {focus: 'series'}
      },
      {
        type: 'line',
        smooth: true,
        seriesLayoutBy: 'row',
        emphasis: {focus: 'series'}
      },
      {
        type: 'pie',
        id: 'pie',
        radius: '30%',
        center: ['50%', '25%'],
        emphasis: {
          focus: 'self'
        },
        label: {
          formatter: '{b}: {@2012} ({d}%)'
        },
        encode: {
          itemName: 'product',
          value: '2012',
          tooltip: '2012'
        }
      }
    ]
  };
  myChart.on('updateAxisPointer', function (event) {
    const xAxisInfo = event.axesInfo[0];
    if (xAxisInfo) {
      const dimension = xAxisInfo.value + 1;
      myChart.setOption({
        series: {
          id: 'pie',
          label: {
            formatter: '{b}: {@[' + dimension + ']} ({d}%)'
          },
          encode: {
            value: dimension,
            tooltip: dimension
          }
        }
      });
    }
  });
  myChart.setOption(option);

  // 页面销毁时清除定时器
  onBeforeUnmount(() => {
    clearInterval(interval);
  });
})
</script>
