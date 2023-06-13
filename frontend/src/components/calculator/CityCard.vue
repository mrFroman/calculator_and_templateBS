<template>
  <div class="filter-city">
    <h2>{{ city.city_name }}</h2>
    <city-table
        v-for="category in categories"
        :category="category"
        :key="category.title"
    ></city-table>
  </div>
</template>

<script>

import TableRow from "@/components/calculator/TableRow.vue";
import CityTable from "@/components/calculator/CityTable.vue";
import {mapGetters} from "vuex";

export default {
  components: {CityTable, TableRow},
  props: {
    city: {
      city_name: {
        type: String
      }
    }
  },
  computed: {
    ...mapGetters({
      categories: 'calculatorData/chooseCategory'
    })
  }
}
</script>

<style lang="scss" scoped>
.filter-city {
  background: #8e4adf;
  border-radius: 50px;
  padding: 40px;
  text-align: center;
  color: #fff;
  margin-bottom: 20px;
}

.filter-type {
  background-color: #fff;
  margin: 20px 0;
  color: #8be3a5;
  text-align: left;

  table {
    width: 100%;
    border-collapse: collapse;
    background-color: #fff;
    color: #8e4adf;
    font-size: 14px;
    padding: 20px;

    th:first-child {
      width: 240px;
    }

    th {
      text-transform: uppercase;
      text-align: center;
      padding: 10px;
      border-radius: 5px;
      background-color: #8e4adf;
      border: 2px #fff solid;
      box-shadow: 0 5px 10px #bebebe;
      color: #fff;
    }
  }
}
</style>
