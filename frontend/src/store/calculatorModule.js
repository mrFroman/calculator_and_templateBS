import axios from "axios";

export const calculatorModule = {
    state: () => ({
        apiData: [],
        calculation: {
            cities: [],
            link: '',
            categories: [],
        }
    }),
    getters: {
        chooseCityString(state) {
            return state.calculation.cities.map(el => el = el.city_name).toString().replace(',', ', ')
        },
        chooseCategory(state) {
            return state.calculation.cities.map(city => city.categories.filter(category => state.calculation.categories.map(c => c = c.name).includes(category.title)))[0]
        }
    },
    mutations: {
        setData(state, data) {
            state.apiData = data
        },
        setCity(state, chooseCity) {
            state.calculation.cities = state.apiData.filter(city => chooseCity.includes(city.city_name))
        },
        setEventLink(state, event) {
            state.calculation.link = event.target.value
        },
        setCategories(state, event) {
            state.calculation.categories = event.map(el => el = {name: el, types: []})
        },
        addRow(state, event, title) {
            state.calculation.categories.find(category => category.name === event[0].name).types = event
            console.log(event[0].name)
        }
    },
    actions: {
        getData({state, commit}) {
            try {
                axios.get('http://127.0.0.1:8000/api/v1/calculator/')
                    .then(response => commit('setData', response.data))
            } catch (e) {
                console.log(e)
            }
        }
    },
    namespaced: true
}
