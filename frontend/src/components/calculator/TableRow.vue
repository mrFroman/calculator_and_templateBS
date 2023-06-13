<template>
  <tr>
    <td>
      <select id="type" v-model="o.type" @change="$emit('update:selected', o)">
        <option value="Выберите тип размещения" disabled>Выберите тип размещения</option>
        <option
            v-for="type in category.offer"
            :value="type.name_offer"
            :key="type.name_offer"
        >
          {{ type.name_offer }}
        </option>
      </select>
    </td>
    <td>
      <input type="date" v-model="o.start_date" @change="$emit('update:selected', o)">
    </td>
    <td>
      <input type="date" v-model="o.end_date" @change="$emit('update:selected', o)">
    </td>
    <td>{{ s }}</td>
  </tr>
</template>

<script>
export default {
  props: {
    category: {
      offer: {
        name_offer: {
          type: String
        }
      },
    },
    index: {
      type: Number
    }
  },
  data() {
    return {
      o: {
        name: this.category.title,
        id: this.index + 1,
        type: '',
        start_date: '',
        end_date: '',
        period: '',
        price: ''
      }
    }
  },
  computed: {
    s() {
      this.o.period = (new Date(this.o.end_date).getDate() - new Date(this.o.start_date).getDate()) + 1
      this.o.price = {...(this.category.offer.find(offer => offer.name_offer === this.o.type))}.price * this.o.period
      return this.o.price || 0
    }
  },
  beforeUnmount() {
    this.o = []
  }
}
</script>

<style lang="scss" scoped>
td {
  padding: 10px;
  background-color: #8e4adf;
  border: 2px #fff solid;
  color: #fff;

  select {
    padding: 5px;
    width: 100%;
    outline: none;
    border: none;
    border-radius: 5px;

    option {
      padding: 10px;
    }
  }

  input {
    padding: 5px;
    width: 100%;
    border-radius: 5px;
    outline: none;
    border: none;
  }
}
</style>
