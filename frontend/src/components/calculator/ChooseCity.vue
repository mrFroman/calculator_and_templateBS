<template>
  <div>
    <my-modal
        v-model:show="isVisible"
    >
      <h2>Выберите города</h2>
      <div class="cities">

        <div class="checkbox"
             v-for="city in cities"
        >
          <input
              type="checkbox"
              :id=city
              :value=city
              v-model="selectedCities"
          >
          <label :for=city>{{ city }}</label>
        </div>
      </div>
      <calculator-button style="margin: 20px 0;" @click="updateCity">Выбрать</calculator-button>
    </my-modal>
    <calculator-button @click="showModal">Выбрать города</calculator-button>
  </div>
</template>

<script>
import CalculatorButton from "@/components/UI/CalculatorButton.vue";
import MyModal from "@/components/UI/MyModal.vue";
import axios from "axios";

export default {
  components: {MyModal, CalculatorButton},
  emits: ['update:citiesProp'],
  props: {
    citiesProp: {
      type: Array
    }
  },
  data() {
    return {
      isVisible: false,
      cities: [],
      selectedCities: []
    }
  },
  methods: {
    showModal() {
      this.isVisible = true
    },
    updateCity() {
      if(this.selectedCities.length < 1) {
        alert('Выберите минимум 1 город')
        return
      }
      this.$emit('update:citiesProp', this.selectedCities)
      this.isVisible = false
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/api/v1/calculator/`)
        .then(response => console.log(response.data))
  }
}
</script>

<style lang="scss" scoped>

.cities {
  font-size: 14px;
  color: #222;
  letter-spacing: normal;
  columns: 7 auto;
  padding: 20px 40px;
}

.checkbox {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 5px 0;
  cursor: pointer;
}

label {
  cursor: pointer;
}
</style>
