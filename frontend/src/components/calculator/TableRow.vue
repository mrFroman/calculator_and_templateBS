<template>
  <tr>
    <td>
      <select id="type" v-model="selected">
        <option value="Выберите тип размещения" disabled>Выберите тип размещения</option>
        <option v-for="type in place" :value="type.name">{{ type.name }}</option>
      </select>
    </td>
    <td>
      <input v-if="selected !== 'Выберите тип размещения'" type="date" v-model="startDate">
    </td>
    <td>
      <input v-if="startDate" type="date" v-model="endDate">
    </td>
    <td>4</td>
    <td>5</td>
  </tr>
</template>

<script>
export default {
  props: {
    place: {
      type: Object
    }
  },
  data() {
    return {
      selected: 'Выберите тип размещения',
      startDate: '',
      endDate: ''
    }
  }
}
</script>

<style lang="scss" scoped>
td {
  padding: 10px;
  border-radius: 5px;
  background-color: #8e4adf;
  border: 2px #fff solid;
  box-shadow: 0 5px 10px #bebebe;
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
