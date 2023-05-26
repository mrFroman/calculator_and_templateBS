<template>
  <navbar></navbar>
  <div class="main">
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from "@/components/UI/Navbar.vue";

export default {
  components: {Navbar}

}
</script>

<style lang="scss">
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  font-family: Helvetica, Geneva, sans-serif;
  font-size: 14px;
}

.main__panel {
  width: calc(100% - 650px);
  margin-right: 650px;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  border-bottom: 1px #ccc solid;
}

h4 {
  margin-bottom: 15px;
}

.email {
  width: 650px;
  height: 100%;
  position: fixed;
  top: 0;
  right: 0;
  border-left: 1px #ccc solid;
  background-color: #f7f7f7;
  overflow-y: scroll;
  margin-top: 65px;
  z-index: 0;
}

.email__template {
  width: 600px;
  min-height: 100%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  background-color: #fff;
}

.header {
  height: 118px;
}

*[contenteditable] {
  border: 1px #868686 dashed;
  border-radius: 5px;
}
</style>
