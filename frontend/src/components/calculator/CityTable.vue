<template>
  <h2>{{ t }}</h2>
  <table>
    <thead>
      <tr>
        <th>Место</th>
        <th style="width: 250px">Дата начала</th>
        <th style="width: 250px">Дата окончания</th>
        <th>Цена</th>
        <th>Цена</th>
      </tr>
    </thead>
    <tbody>
      <table-row
        v-for="row in tableRows"
        :row="row"
      ></table-row>

    </tbody>
  </table>
  <button @click="tableRows.push({})">Добавить</button>
</template>

<script>
import TableRow from "@/components/calculator/TableRow.vue";

export default {
  components: {TableRow},
  props: {
    t: {
      type: String
    }
  },
  data() {
    return {
      tableRows: []
    }
  },
  beforeMount() {
    this.tableRows.push({})
  }
}
</script>

<style lang="scss" scoped>
table {
  width: 100%;
  border-collapse: collapse;
  border-radius: 5px;

  th,
  td {
    border: 2px #fff solid;
    padding: 10px;
    text-transform: uppercase;
  }
}

h2 {
  text-align: left;
  color: #8be3a5;
  margin: 20px 0;
}

button {
  background: transparent;
  border: none;
  outline: none;
  margin: 20px 0;
  color: #fff;
  cursor: pointer;
}
</style>
