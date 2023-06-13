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
            {{ cityString }}
          </span>
        </p>
        <choose-city
            :cities="dataCities"
            @update:cities="setCity"
        ></choose-city>
      </div>


      <div class="event">
        <h4>Ссылка на мероприятие</h4>
        <input
            type="text"
            @input="setEventLink"
        >
      </div>

      <div class="type">
        <h4>Выберите тип рассылки</h4>
        <div class="types">

          <div class="checkbox"
               v-for="category in types"
          >
            <input
                type="checkbox"
                :id=category
                :value=category
                v-model="chooseCategories"
            >
            <label :for=category>{{ category }}</label>
          </div>
        </div>
      </div>

      <div class="contacts">
        <h4>Контакты</h4>
        <div class="contacts_item">
          <label for="company_type">Организационно правовая форма</label>
          <select id="company_type" v-model="calculation.company.type">
            <option value="ООО">ООО</option>
            <option value="ИП">ИП</option>
          </select>
        </div>
        <div class="contacts_item">
          <label for="company_inn">ИНН</label>
          <input id="company_inn" v-model="calculation.company.inn">
        </div>
        <div class="contacts_item">
          <label for="company_phone">Телефон</label>
          <input id="company_phone" v-model="calculation.company.phone">
        </div>
        <div class="contacts_item">
          <label for="company_email">E-mail</label>
          <input id="company_email" v-model="calculation.company.email">
        </div>
      </div>

      <div class="comments">
        <h4>Комментарий к заказу</h4>
        <textarea v-model="calculation.comment"></textarea>
      </div>

      <calculator-button style="background: coral"
      >Перейти к расчету
      </calculator-button>
    </div>

    <div class="calculation">
      <city-card
          :city="city"
          v-for="city in selectedCity"
          :key="city.id"
      >
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
import {mapState, mapMutations, mapActions, mapGetters} from 'vuex'
export default {
  components: {CityTable, CityCard, ChooseCity, CalculatorButton, ViolettButton},
  data() {
    return {
      types: [
        'Сайт',
        'Емейл'
      ],
      calculation: {
        company: {
          type: '',
          inn: '',
          phone: '',
          email: ''
        },
        comment: ''
      },
      chooseCategories: []
    }
  },
  methods: {
    ...mapActions({
      getData: 'calculatorData/getData'
    }),
    ...mapMutations({
      setCity: 'calculatorData/setCity',
      setEventLink: 'calculatorData/setEventLink',
      setCategories: 'calculatorData/setCategories'
    }),

  },
  computed: {
    ...mapState({
        dataCities: state => state.calculatorData.apiData,
        selectedCity: state => state.calculatorData.calculation.cities,
        categories: state => state.calculatorData.calculation.categories
    }),
    ...mapGetters({
      cityString: 'calculatorData/chooseCityString',
    })
  },
  watch: {
    chooseCategories(event) {
      this.setCategories(event)
    }
  },
  mounted() {
    this.getData()
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

    .contacts {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 10px;

      h4 {
        width: 100%;
      }

      &_item {
        width: 48%;

        input,
        select {
          display: block;
          padding: 10px;
          width: 100%;
          border-radius: 5px;
          border: 1px #8e4adf solid;
          outline: none;
          margin-top: 5px;

          &:focus {
            box-shadow: inset 0 0 2px 0 #8e4adf;
          }
        }
      }
    }

    .comments {
      textarea {
        display: block;
        padding: 10px;
        width: 100%;
        height: 100px;
        border-radius: 5px;
        border: 1px #8e4adf solid;
        outline: none;
        margin-top: 5px;

        &:focus {
          box-shadow: inset 0 0 2px 0 #8e4adf;
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
