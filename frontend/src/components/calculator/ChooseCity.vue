<template>
  <div>
    <my-modal
        v-model:show="isVisible"
    >
      <h2>Выберите города</h2>
      <div class="cities">

        <div class="checkbox"
             v-for="city in cities"
             :key="city.id"
        >
          <input
              type="checkbox"
              :id=city.id
              :value=city.city_name
              v-model="selectedCities"
          >
          <label :for=city.id>{{ city.city_name }}</label>
        </div>
      </div>
      <calculator-button @click="updateCity">Выбрать</calculator-button>
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
  emits: ['update:cities'],
  props: {
    cities: {
      id: {
        type: Number
      },
      city_name: {
        type: String
      }
    }
  },
  data() {
    return {
      isVisible: false,
      selectedCities: []
    }
  },
  methods: {
    showModal() {
      this.isVisible = true
    },
    updateCity() {
      // if(this.selectedCities.length < 1) {
      //   alert('Выберите минимум 1 город')
      //   return
      // }
      this.$emit('update:cities', this.selectedCities)
      this.isVisible = false
    }
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
