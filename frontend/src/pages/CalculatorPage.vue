<template>
  <div class="calculator">
    <div class="control-panel">

      <div class="city">
        <p>
          <span
              style="font-weight: bold"
          >
            Выбраны города:
          </span>
          <span
              style="color: #8e4adf"
          >
            {{ selectedCity }}
          </span>
        </p>
        <choose-city
            :cities-prop="calculation.cities"
            @update:citiesProp="calculation.cities = $event"
        ></choose-city>
      </div>


      <div class="event">
        <h4>Ссылка на мероприятие</h4>
        <input
            type="text"
            v-model="link"
        >
        <calculator-button>Выбрать мероприятие</calculator-button>
      </div>

      <div class="type">
        <h4>Выберите тип рассылки</h4>
        <div class="types">

          <div class="checkbox"
               v-for="type in types"
          >
            <input
                type="checkbox"
                :id=type
                :value=type
                v-model="calculation.types"
            >
            <label :for=type>{{ type }}</label>
          </div>
        </div>
      </div>

      <div class="contacts">
        
      </div>

      <calculator-button style="background: coral"
                         @click="calculate"
      >Перейти к расчету
      </calculator-button>
    </div>

    <div class="calculation">
      <city-card
          :city="city"
          v-for="city in calculation.cities"
          :key="city"
      >
        <city-table
            v-for="type in calculation.types"
            :t="type"
        ></city-table>
      </city-card>
    </div>
  </div>
</template>

<script>

import ViolettButton from "@/components/UI/ViolettButton.vue";
import CalculatorButton from "@/components/UI/CalculatorButton.vue";
import ChooseCity from "@/components/calculator/ChooseCity.vue";
import CityCard from "@/components/calculator/CityCard.vue";
import CityTable from "@/components/calculator/CityTable.vue";

export default {
  components: {CityTable, CityCard, ChooseCity, CalculatorButton, ViolettButton},
  data() {
    return {
      city: '',
      link: '',
      types: [
        'Сайт',
        'Рассылка',
        'Социальные сети',
        'Контекст/Таргет',
        'Прочее'
      ],
      calculation: {
        cities: [],
        types: [],

      },
      isValidCalculation: false,
      error: 0
    }
  },
  methods: {
    calculate() {
      this.error = 0
      for (let key in this.calculation) {
        if (!`${this.calculation[key]}`) {
          alert(`Заполните ${key}`)
          this.error += 1
        }
        this.isValidCalculation = !this.error;
      }
    }
  },
  computed: {
    selectedCity() {
      this.city = ''
      for (let c of this.calculation.cities) {
        this.city += `${c} `
      }
      return this.city.trim().split(' ').join(', ')
    }
  }
}
</script>

<style lang="scss">
.calculator {
  display: flex;
  padding: 20px;

  .control-panel {
    width: 30%;
    display: flex;
    flex-direction: column;
    gap: 40px;

    .city {
      p {
        border-bottom: 1px #bebebe solid;
        margin-bottom: 20px;
        padding-bottom: 5px;
      }
    }

    .event {
      input {
        padding: 10px;
        width: 100%;
        border-radius: 5px;
        border: 1px #8e4adf solid;
        outline: none;
        margin-bottom: 20px;

        &:focus {
          box-shadow: inset 0 0 2px 0 #8e4adf;
        }
      }
    }

    .type {
      .types {
        display: flex;
        align-items: center;
        gap: 10px;

        .checkbox {
          display: flex;
          align-items: center;
          gap: 5px;
        }
      }
    }
  }
}

.calculation {
  flex: 1 1 70%;
  padding-left: 20px;
}
</style>
