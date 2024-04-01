<template>
  <div>
    <h1>Weather Application</h1>
    <input v-model="city" type="text" placeholder="Enter city name">
    <button @click="searchWeather">Search</button>
    <div v-if="weatherData">
      <h2>Weather in {{ weatherData.location.name }}, {{ weatherData.location.country }}</h2>
      <p>Temperature: {{ weatherData.current.temp_c }}°C</p>
      <p>Condition: {{ weatherData.current.condition.text }}</p>
    </div>
    <div v-if="errorMessage">{{ errorMessage }}</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      city: '',
      weatherData: null,
      errorMessage: ''
    }
  },
  methods: {
    async searchWeather () {
      try {
        const response = await fetch(`/api/weather?city=${this.city}`)
        const data = await response.json()
        if (response.ok) {
          this.weatherData = data
          this.errorMessage = ''
        } else {
          this.weatherData = null
          this.errorMessage = data.error
        }
      } catch (error) {
        console.error('Error fetching weather data:', error)
        this.weatherData = null
        this.errorMessage = 'An error occurred while fetching weather data.'
      }
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
