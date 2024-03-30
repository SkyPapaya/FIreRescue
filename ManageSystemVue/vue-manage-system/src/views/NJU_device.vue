<script lang="ts" setup>
import service from "../utils/request";

interface User {
  device_id: string;
  parent_device_id: string;
  address: string;
  co: number;
  fire_exit: string;
  fire_probability: number;
}

const tableRowClassName = ({
                             row,
                             rowIndex,
                           }: {
  row: User;
  rowIndex: number;
}) => {
  if (row.fire_probability > 0.8 || row.co > 0.8 || row.fire_exit === "exist") {
    return "warning-row";
  } else if (rowIndex === 3) {
    return "success-row";
  }
  return "";
};
const state = reactive({
  tableData: [],
  form: {}
})
import {reactive, ref, onMounted} from "vue";

const activeIndex = ref("1");
const activeIndex2 = ref("1");
const count = ref(0)
//请求后台数据
const load = () => {
  service.get('/environments').then((res) => {
    //res.data是后台返回的数据
    state.tableData = res.data
    console.log(res.data)
  })
}
// 初始加载数据
onMounted(() => {
  load();

  // 每隔一段时间检查一次数据
  setInterval(() => {
    state.tableData.forEach((item) => {
      if (item.fireExist === 1) {
        console.log('检测到火源')
        checkFire();
        // 如果遇到了一个存在火源的数据，就直接结束循环
        return;
      }
    });
  }, 3000); // 每隔三秒检查一次
});
// 每三秒刷新一次数据
setInterval(() => {
  load();

}, 3000);
import {ElNotification} from 'element-plus'

const checkFire = () => {
  ElNotification({
    title: 'Error',
    message: 'This is an error message',
    type: 'error',
  });
};
</script>
<style>
.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
  background-color: #cc0033;
  color: #cccccc;
}

.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>

<style scoped>
.layout-container-demo .el-header {
  position: relative;
  color: var(--el-text-color-primary);
  width: 100%;
}

.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
}

.layout-container-demo .el-menu {
  border-right: none;
}

.layout-container-demo .el-main {
  padding: 0;
}

.layout-container-demo .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  right: 20px;
}
</style>

<template>
  <el-button plain @click="checkFire"> Error</el-button>
  <el-container class="layout-container-demo" style="height: 100%">
    <el-container>
      <div style="display:block">
        <el-table
            :data="state.tableData"
            style="width: 100%; font-size: 20px; display: block"
            :row-class-name="tableRowClassName"
        >


          <el-table-column prop="fireExist" label="是否存在火源" width="180px" align="center"/>
          <el-table-column prop="temperature" label="最高温度" width="180px" align="center"/>
          <el-table-column prop="smoke" label="烟雾浓度" width="180px" align="center"/>
          <el-table-column prop="co" label="一氧化碳浓度" width="180px" align="center"/>
          <el-table-column prop="risk" label="火灾风险" width="180px" align="center"/>
          <el-table-column prop="humidity" label="湿度" width="180px" align="center"/>
          <el-table-column prop="people" label="是否有人" width="180px" align="center"/>
          <el-table-column prop="address" label="地址" width="180px" align="center"/>
        </el-table>
      </div>

    </el-container>
    <div class="example-pagination-block"
         style="padding-left: 10px; width: 100px;height: 50px; position: absolute; left: 10px ; bottom: 250px ">
      <div class="example-demonstration"></div>
      <el-pagination layout="prev, pager, next" :total="50" page-count="10"/>
    </div>

  </el-container>
</template>
