import {createStore} from "vuex";
import {calculatorModule} from "@/store/calculatorModule";


export default  createStore({
    modules: {
        calculatorData: calculatorModule
    }
})
