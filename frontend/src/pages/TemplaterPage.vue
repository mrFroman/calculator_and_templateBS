<template>
  <div>
    <div class="main__panel">
      <events-upload
          @loadEvents="getEvents"
          ref="replaceEvent"
      />
      <choose-template
          @choose="choose"
      />
      <violett-button
          style="margin: 0"
          @click="getDemoEvents"
      >
        Получить демоданные из базы данных
      </violett-button>
    </div>
    <events-list
        :events="events"
        @remove="removeEvent"
    />
    <div class="email">
      <div class="email__template">
        <div class="header">
          <p class="not-correct">Если письмо отображается некорректно, то <a href="#">смотрите здесь</a></p>
          <img src="@/assets/img/header.jpg" alt="">
        </div>
        <email-template
            :template="template"
        />
        <div class="footer">
          <img src="@/assets/img/footer.jpg" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EventsList from '@/components/email-templater/EventsList.vue'
import EventsUpload from '@/components/email-templater/EventsUpload.vue';
import ChooseTemplate from '@/components/email-templater/ChooseTemplate.vue';
import EmailTemplate from "@/components/email-templater/EmailTemplate.vue";
import axios from "axios";

export default {
  components: {
    EmailTemplate,
    EventsList,
    EventsUpload,
    ChooseTemplate
  },
  data() {
    return {
      events: [],
      template: 'Формат не выбран'
    }
  },
  methods: {
    removeEvent(event) {
      this.events = this.events.filter(element => element.id !== event.id)
    },
    choose(button) {
      this.template = button.data
    },
    getEvents(eventsArray) {
      Promise.all(eventsArray.map(link => {
        axios.get(`http://localhost:3000/events?link=${link}`)
            .then(response => this.events.push(response.data))
      }))
    },
    getDemoEvents() {
      axios.get(`http://localhost:3000/events/demo`)
          .then(response => this.events.push(...response.data))
    }
  }
}
</script>

<style>
.email {
  margin-right: 5px;
  &::-webkit-scrollbar {
    width: 5px;
  }

  &::-webkit-scrollbar-thumb {
    background: #B0B0B0;
    border-radius: 50px;
  }

  &::-webkit-scrollbar-track {
    background: #F5F5F5;
  }
}

.not-correct {
  margin: 5px 5px 20px 5px;
  text-align: center;
  color: #919191;
}

a {
  color: #919191;
}
</style>
