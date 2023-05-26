<template>
  <div
      class="filter-city"
      v-for="city in calculation.cities"
      :key="city"
  >
    <h2>{{ city }}</h2>
    <div class="filter-type" v-for="type in calculation.types" :key="type">
      <h2>{{ type }}</h2>
      <table>
        <thead>
        <tr>
          <th>Место</th>
          <th style="width: 200px">Дата начала</th>
          <th style="width: 200px">Дата окончания</th>
          <th>Цена</th>
          <th>Цена</th>
        </tr>
        </thead>
        <tbody>
          <table-row v-for="row in rowArray"
            :place="calculation.place"
          ></table-row>
        </tbody>
      </table>
      <button @click="rowArray.push({})">Добавить</button>
    </div>
  </div>

</template>

<script>

import TableRow from "@/components/calculator/TableRow.vue";

export default {
  components: {TableRow},
  props: {
    calculation: {
      type: Object
    }
  },
  data() {
    return {
      selected: '',
      rowArray: []
    }
  },
  computed: {
  },
  beforeMount() {
    this.rowArray.push(this.calculation.place)
  }
}
</script>

<style lang="scss" scoped>
.filter-city {
  background: #fff;
  border-radius: 50px;
  padding: 20px;
  text-align: center;
  color: #8e4adf;
  margin: 20px 0 20px;
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
