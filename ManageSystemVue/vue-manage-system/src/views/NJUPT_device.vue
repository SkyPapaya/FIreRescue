<template>
  <el-container class="layout-container-demo" style="height: 100%">
    <el-container>
      <div style="display:block">
        <el-table
            :data="state.tableData"
            style="width: 100%; font-size: 20px; display: block"
            :row-class-name="tableRowClassName"
        >

          <el-table-column prop="humidity" label="湿度" width="180px" align="center"/>
          <el-table-column prop="temperature" label="最高温度" width="180px" align="center"/>
          <el-table-column prop="fire" label="是否存在火源" width="180px" align="center"/>
          <el-table-column prop="smoke" label="烟雾浓度" width="180px" align="center"/>
          <el-table-column prop="co" label="一氧化碳浓度" width="180px" align="center"/>
          <el-table-column prop="risk" label="火灾风险" width="180px" align="center"/>
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

<script setup lang="ts">
import {reactive, ref, onMounted} from "vue";
import service from "../utils/request";

interface environment {
  humidity: number;
  temperature: number;
  fire: number;
  smoke: number;
  co: number;
  risk: number;
}

const state = reactive({
  tableData: [],
  form: {},
});


const tableRowClassName = ({
                             row,
                           }: {
  row: environment;
  rowIndex: number;
}) => {
  if (row.risk > 0.8 || row.co > 0.8 || row.fire === 1) {
    return "warning-row";
  }
  return "";
};

// 请求后台数据
const load = () => {
  service.get('/environment/getTheLatest').then((res) => {
    state.tableData.push(res.data);

    console.log(res.data);
  });
};

// 初始加载数据
onMounted(() => {
  load();
});

//
setInterval(() => {
  load();
  state.tableData.shift();
}, 1000);


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


