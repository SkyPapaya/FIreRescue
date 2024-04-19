<template>
  <el-button plain @click="click3" class="search-button"  :style="{ backgroundColor: background }">
    <LocationInformation style="width: 8em; height: 8em; margin-right: 8px"/>
  </el-button>
  <el-text type="success" class="text1"  v-show="text_visible">{{ status }}</el-text>
  <el-text type="danger" class="text2"  v-show="!text_visible">{{ status }}</el-text>
  <el-button plain @click="click1" class="warning-button">
    <Warning style="width: 8em; height: 8em; margin-right: 8px"/>
  </el-button>
  <div>
    <el-input v-model="input" style="width: 240px" placeholder="输入地区以查询终端数据" class="input"/>
    <el-button plain @click="click2" class="check-button">
      <Search style="width: 1.2em; height: 1.2em; margin-right: 8px;border: 2px" />
    </el-button>
  </div>
  <el-table
      :data="state.tableData"
      style="width: 100%; font-size: 20px; display: block; color: black; margin-left: 15%;;width:67%;margin-top: 10px"
      :row-class-name="tableRowClassName"
      :header-cell-style="{color:'black'}"
      v-show="visible"
  >
    <el-table-column prop="humidity" label="湿度" width="180px" align="center" style="color: black"/>
    <el-table-column prop="temperature" label="最高温度" width="180px" align="center"/>
    <el-table-column prop="fire" label="是否存在火源" width="180px" align="center"/>
    <el-table-column prop="smoke" label="烟雾浓度" width="180px" align="center"/>
    <el-table-column prop="co" label="有害气体浓度" width="180px" align="center"/>
    <el-table-column prop="risk" label="火灾风险" width="180px" align="center"/>
  </el-table>
</template>

<script lang="ts" setup>
import { ElNotification } from 'element-plus'
import {LocationInformation, Warning} from "@element-plus/icons-vue";
import { reactive, ref, onMounted } from "vue";
import service from "../utils/request";

const input = ref('');

interface environment {
  humidity: number;
  temperature: number;
  fire: number;
  smoke: number;
  co: number;
  risk: number;
}

let humidity; //8
let temperature; //50
let fire; //0
let smoke; //8
let co; //20
let risk; //0
const state = reactive({
  tableData: [],
  form: {},
});
const activeIndex = ref("1");
const activeIndex2 = ref("1");
const count = ref(0);

const tableRowClassName = ({
                             row,
                             rowIndex,
                           }: {
  row: environment;
  rowIndex: number;
}) => {
  if (row.risk === 1 || row.co > 20 || row.fire === 1) {
    return "warning-row";
  }
  return "";
};

// 请求后台数据
const load = () => {
  service.get('/environment/getTheLatest').then((res) => {
    const newData = res.data;
    // 清空表格数据
    state.tableData = [];
    // 将获得的五条数据添加到表格数据中
    for (let i = 0; i < newData.length; i++) {
      state.tableData.push(newData[i]);
    }
    // 更新数据到界面
    humidity = state.tableData[state.tableData.length - 1].humidity;
    temperature = state.tableData[state.tableData.length - 1].temperature;
    fire = state.tableData[state.tableData.length - 1].fire;
    smoke = state.tableData[state.tableData.length - 1].smoke;
    co = state.tableData[state.tableData.length - 1].co;
    risk = state.tableData[state.tableData.length - 1].risk;
  });
};

// 初始加载数据
onMounted(() => {
  load();
});

// 每三秒刷新一次数据
setInterval(() => {
  state.tableData.shift();
  state.tableData.shift();
  state.tableData.shift();
  state.tableData.shift();
  state.tableData.shift();
  load();
  if (humidity > 80 || temperature > 50 || fire === 1 || smoke > 80 || co > 20 || risk === 1) {
    ElNotification({
      title: 'Warning',
      message: '有火情',
      type: 'error',
    })
  }
}, 60000);

const click1 = () => {
  ElNotification({
    title: 'Warning',
    message: '已向终端设备发送警报',
    type: 'error',
  })
}

let visible = true
const click2 = () => {
  visible = !visible
  load();
}

let status1 = '觅生者处于监控状态'
let status2 = '觅生者处于搜寻状态'
let status = status1
let text_visible = true
let background = 'green'
const click3 = () => {
  if (text_visible){
    status = status2
  }
  else {
    status = status1
  }
  text_visible = !text_visible
  background = background === 'red' ? 'green' : 'red'; // Toggle background color
  load();
}
</script>

<style scoped>
.warning-button {
  background-color: #f56c6c;
  color: white;
  border-color: #f56c6c;
  width:15%;
  height:15%;
  margin-left: 25%;
  margin-top: 5%;
  border-radius: 10px;
}

.check-button {
  color: white;
  border-color: #64d8ff;
  background-color: #64d8ff;
  margin-left: 5px;
  border-radius: 20px;
  margin-top: 5%;
}

.search-button {
  background-color: #31b033;
  color: white;
  border-color: #31b033;
  height: 15%;
  width: 15%;
  margin-left: 15%;
  margin-top: 5%;
  border-radius: 10px;
}

.text1, .text2 {
  position: absolute;
  font-size: 20px;
  margin-top: 8%;
  margin-left: 40px;
  border-color: #8c939d;
}

.input{
  margin-left: 15%;
  border-radius: 10px;
  margin-top: 5%;
}
</style>
