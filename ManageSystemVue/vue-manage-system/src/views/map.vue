<template>

 <div class="map">
   <img  src="../img/map.png" :key="imageKey">/>
 </div>
</template>

<style>
.map{

  height: 60px;
  width: 60px;
}
</style>
<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const imageSrc = ref("");
    const imageKey = ref("");
    const load = () => {
      // Appending a timestamp to force the browser to reload the image
      imageSrc.value = `../img/map.png?timestamp=${new Date().getTime()}`;
      imageKey.value = new Date().getTime();
    };

    onMounted(() => {
      load(); // Initial load
      // Set interval to update the image source every 100ms
      setInterval(() => {
        location.reload();
        console.log("refresh")
      }, 3000);
    });

    return {
      imageSrc,
    };
  },
};
</script>