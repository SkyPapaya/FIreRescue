<template>

 <div class="map">
   <img  src="../img/map.png">/>
 </div>
</template>

<style>
.map{

  height: 60px;
  width: 60px;
}
</style>
<script>
import {onMounted} from "vue";

onMounted(() => {
  // 设置定时器每秒更新一次数据
  setInterval(() => {
    load();
    console.log("2")
  }, 1000);
});

</script>