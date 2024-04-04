<template>
  <div ref="chart"></div>
</template>

<script setup lang="ts">
import {ref, onMounted} from 'vue';
import * as echarts from 'echarts';
import service from "../utils/request";

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
        ['湿度', 0],
        ['温度', 0],
        ['火情', 0],
        ['CO浓度', 0],
        ['烟雾浓度', 0],
      ]
    },
    {
      // 根据第二个数据进行排序
      transform: {
        type: 'sort',
        config: {dimension: 'value', order: 'desc'}
      }
    }
  ],
  xAxis: {
    type: 'category',
    axisLabel: {interval: 0, rotate: 30}
  },
  yAxis: {
    min: 0,
    max: 100
  },
  // 编码修改为正确的名称
  series: {
    type: 'bar',
    encode: {x: 'name', y: 'value'},
    datasetIndex: 1,
    // y 值大于 80 时柱状图颜色为红色，y 值大于 50 小于等于 80 时柱状图颜色为黄色，y 值小于等于 50 时柱状图颜色为蓝色
    itemStyle: {
      color: function (params: any) {
        const value = params.data[1]; // 获取 y 值
        if (value > 80) {
          return 'red';
        } else if (value > 50) {
          return 'yellow';
        } else {
          return 'blue';
        }
      }
    }
  },
  tooltip: {
    trigger: 'axis',
    axisPointer: {type: 'shadow'},
    formatter: function (params) {
      const data = params[0].data;
      return `${data[0]}：<br/>${data[1]}`;
    }
  }
};
let humidity;
let temperature;
let people;
let fire;
let co;
let smoke;
//获取数据
const load = () => {
  service.get('environment/getTheLatest').then((res) => {
    humidity = res.data.humidity;
    temperature = res.data.temperature;
    people = res.data.people;
    fire = res.data.fire;
    co = res.data.co;
    smoke = res.data.smoke;
    // 替换数据
    option.dataset[0].source = [
      ['湿度', humidity],
      ['温度', temperature],
      ['火情', fire],
      ['CO浓度', co],
      ['烟雾浓度', smoke],
    ];
  });
}

onMounted(() => {
  const myChart = echarts.init(chart.value!);
  load();
  myChart.setOption(option);

  setInterval(() => {
    load();
    // 根据第二个数据排序
    option.dataset[0].source.sort((a: any, b: any) => b[1] - a[1]);
    // 更新图表
    myChart.setOption(option);
  }, 1000);
});
</script>
