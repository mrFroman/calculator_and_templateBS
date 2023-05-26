<template>
  <div class="navbar">
    <img @click="$router.push('/')" src="@/assets/img/rassylka.png" alt="logo">
    <hr>
    <navbar-link @click="$router.push('/')">Калькулятор</navbar-link>
    <navbar-link @click="$router.push('/email-templater')">Шаблонизатор</navbar-link>
  </div>
</template>

<script>
import NavbarLink from "@/components/UI/NavbarLink.vue";
export default {
  components: {NavbarLink}

}
</script>

<style lang="scss" scoped>
.navbar {
  height: 60px;
  background-color: #8e4adf;
  box-shadow: 2px 2px 4px #222;
  display: flex;
  align-items: center;
  padding: 0 20px;
  gap: 20px;
  z-index: 100;
  position: sticky;
  top: 0;

  img {
    height: 40px;
    margin-right: 50px;
    cursor: pointer;
  }

  hr {
    height: 30px;
    border-left: 2px #fff solid;
    border-radius: 5px;
  }
}
</style>
