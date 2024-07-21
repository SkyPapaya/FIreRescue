<template>
  <div class="area-chart" ref="chart"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts';
import {ref, onMounted} from 'vue';
import service from "../utils/request";

// 定义图表容器
const chart = ref<HTMLDivElement | null>(null);
// 初始化当前时间
let now = new Date();
// 初始化数据数组
let data: any[] = [];
// 初始化 x 轴数据数组
let xAxisData: string[] = [];
// 初始化 echarts 选项
let option: {
  yAxis: { min: number; max: number; splitLine: { show: boolean }; type: string; boundaryGap: [number, string] };
  xAxis: { data: string[]; splitLine: { show: boolean }; type: string };
  series: {
    symbol: string;
    showSymbol: boolean;
    data: any[];
    lineStyle: { color: string };
    symbolSize: number;
    name: string;
    type: string
  }[];
  tooltip: { formatter: (params) => string; axisPointer: { animation: boolean }; trigger: string };
  title: { text: string }
};

// 定义心率变量
let heartRate;
// 加载心率数据的函数
const load = () => {
  service.get('/vital/getTheLatest').then((res) => {
    heartRate = res.data.heartRate;
  });
};

// 生成随机数据的函数
function randomData() {
  now = new Date(now.getTime() + 1000);
  return {
    name: now.toLocaleTimeString(),
    value: [
      now.toLocaleTimeString(),
      Math.round(heartRate)
    ]
  };
}

// 生成带有轻微波动的数据
function generateFluctuatedData(originalData: number[]): number[] {
  return originalData.map((value) => value + Math.random() * 10 - 5);
}

// 初始化额外线的数据数组
let data2: any[] = [];
let data3: any[] = [];
let data4: any[] = [];
let data5: any[] = [];

// 初始化数据
for (var i = 0; i < 100; i++) {
  const newData = randomData();
  data.push(newData.value[1]); // 仅将心率值推送到数据数组
  xAxisData.push(newData.name);
}

// 组件挂载后的操作
onMounted(() => {
  const myChart = echarts.init(chart.value!);
  window.addEventListener('resize', () => {
    myChart.resize();
  });

  // 定时刷新数据
  setInterval(function () {
    load();
    const newData = randomData();
    data.shift();
    xAxisData.shift();
    data.push(newData.value[1]); // 仅将心率值推送到数据数组
    xAxisData.push(newData.name);

    // 更新额外线的数据
    data2 = generateFluctuatedData(data);
    data3 = generateFluctuatedData(data);
    data4 = generateFluctuatedData(data);
    data5 = generateFluctuatedData(data);

    myChart.setOption({
      series: [
        {name: '心率', data: data},
        {name: '线 2', data: data2},
        {name: '线 3', data: data3},
        {name: '线 4', data: data4},
        {name: '线 5', data: data5}
      ],
      xAxis: [{data: xAxisData}]
    });

    // 更新文本标签
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
      }]
    });
  }, 1000); // 每秒刷新一次

  myChart.setOption(option);
});

// 初始化图表选项
option = {
  title: {
    text: '心率'
  },
  tooltip: {
    trigger: 'axis',
    formatter: function (params) {
      const date = new Date(params[0].name);
      let tooltip = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds() + '<br/>';
      params.forEach(function (item) {
        tooltip += item.seriesName + ': ' + item.value[1] + '<br/>';
      });
      return tooltip;
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
      name: '心率',
      type: 'line',
      showSymbol: true, // 显示数据点
      symbol: 'circle', // 数据点样式
      symbolSize: 6, // 数据点大小
      data: data,
      lineStyle: {
        color: '#ef3b3b'
      }

      // {
      //   name: '线 2',
      //   type: 'line',
      //   showSymbol: true, // 显示数据点
      //   symbol: 'circle', // 数据点样式
      //   symbolSize: 6, // 数据点大小
      //   data.txt: data2,
      //   lineStyle: {
      //     color: '#ffa02c'
      //   }
      // },
      // {
      //   name: '线 3',
      //   type: 'line',
      //   showSymbol: true, // 显示数据点
      //   symbol: 'circle', // 数据点样式
      //   symbolSize: 6, // 数据点大小
      //   data.txt: data3,
      //   lineStyle: {
      //     color: '#4afafa'
      //   }

      // {
      //   name: '线 4',
      //   type: 'line',
      //   showSymbol: true, // 显示数据点
      //   symbol: 'circle', // 数据点样式
      //   symbolSize: 6, // 数据点大小
      //   data.txt: data4,
      //   lineStyle: {
      //     color: '#ff5f72'
      //   }
      // },
      // {
      //   name: '线 5',
      //   type: 'line',
      //   showSymbol: true, // 显示数据点
      //   symbol: 'circle', // 数据点样式
      //   symbolSize: 6, // 数据点大小
      //   data.txt: data5,
      //   lineStyle: {
      //     color: '#8663e1'
      //   }
    }
  ]
};
</script>
