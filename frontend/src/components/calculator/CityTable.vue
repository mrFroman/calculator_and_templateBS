<template>
  <h2>{{ category.title }}</h2>
  <table>
    <thead>
      <tr>
        <th>Место</th>
        <th style="width: 250px">Дата начала</th>
        <th style="width: 250px">Дата окончания</th>
        <th>Цена</th>
      </tr>
    </thead>
    <tbody>
      <table-row
        v-for="(row, index) in tableRows"
        :category="category"
        :key="index + 1"
        :index="index"
        @update:selected="update"
      ></table-row>
    </tbody>
  </table>
  <div class="buttons">
    <button @click="tableRows.push({})">Добавить</button>
    <button @click="tableRows.pop()">Удалить</button>
  </div>
</template>

<script>
import TableRow from "@/components/calculator/TableRow.vue";
import {mapMutations, mapState} from "vuex";

export default {
  components: {TableRow},
  props: {
    category: {
      title: {
        type: String
      },
      offer: {
        type: Object
      }
    }
  },
  data() {
    return {
      tableRows: [
        {
          type: '',
          start_date: '',
          end_date: '',
          period: '',
          price: ''
        }
      ]
    }
  },
  methods: {
    update(event) {
      console.log(event.name)
      this.tableRows[event.id - 1] = event
      this.addRow(this.tableRows, event.name)
    },
    ...mapMutations({
      addRow: 'calculatorData/addRow'
    })
  },
  beforeUnmount() {
    this.tableRows = []
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

.buttons {
  display: flex;
  justify-content: start;
  gap: 20px;

  button {
    background: transparent;
    border: none;
    outline: none;
    margin: 20px 0;
    color: #fff;
    cursor: pointer;
  }
}
</style>
