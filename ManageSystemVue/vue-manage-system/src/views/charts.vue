<template>
  <div class="container">

    <div class="schart-box">

      <schart class="schart" canvasId="bar" :options="options1"></schart>
    </div>
    <div class="schart-box">

      <schart class="schart" canvasId="line" :options="options2"></schart>
    </div>
<!--    <div class="schart-box">-->

    <!--      <schart class="schart" canvasId="pie" :options="options3"></schart>-->
    <!--    </div>-->
    <!--    <div class="schart-box">-->

    <!--      <schart class="schart" canvasId="ring" :options="options4"></schart>-->
    <!--    </div>-->
  </div>
</template>

<script setup lang="ts" name="basecharts">
import Schart from 'vue-schart';

const options1 = {
  type: 'bar',
  title: {
    text: '造成火灾的原因'
  },
  bgColor: '#fbfbfb',
  labels: ['一季度', '二季度', '三季度', '四季度'],
  datasets: [
    {
      label: '电瓶车',
      fillColor: 'rgba(241, 49, 74, 0.5)',
      data: [234, 278, 270, 190, 230]
    },
    {
      label: '电器',
      data: [164, 178, 190, 135, 160]
    },
    {
      label: '粉尘',
      data: [144, 198, 150, 235, 120]
    }
  ]
};
const options2 = {
  type: 'line',
  title: {
    text: '火灾造成的经济损失'
  },
  bgColor: '#fbfbfb',
  labels: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
  datasets: [
    {
      label: '直接经济损失',
      data: [234, 278, 270, 190, 230, 550, 150, 592, 150, 589, 151, 111, 125]
    },
    {
      label: '间接经济损失',
      data: [164, 178, 190, 135, 160, 148, 11, 125, 114, 116, 31, 55]
    }

  ]
};
const options3 = {
  type: 'pie',
  title: {
    text: '服装品类销售饼状图'
  },
  legend: {
    position: 'left'
  },
  bgColor: '#fbfbfb',
  labels: ['T恤', '牛仔裤', '连衣裙', '毛衣', '七分裤', '短裙', '羽绒服'],
  datasets: [
    {
      data: [334, 278, 190, 235, 260, 200, 141]
    }
  ]
};
const options4 = {
  type: 'ring',
  title: {
    text: '环形三等分'
  },
  showValue: false,
  legend: {
    position: 'bottom',
    bottom: 40
  },
  bgColor: '#fbfbfb',
  labels: ['vue', 'react', 'angular'],
  datasets: [
    {
      data: [500, 500, 500]
    }
  ]
};
</script>

<style scoped>
.schart-box {
  display: inline-block;
  margin: 20px;
}

.schart {
  width: 600px;
  height: 400px;
}

.content-title {
  clear: both;
  font-weight: 400;
  line-height: 50px;
  margin: 10px 0;
  font-size: 22px;
  color: #1f2f3d;
}
</style>
