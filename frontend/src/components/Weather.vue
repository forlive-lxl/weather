<template>
  <div>
    <h1>Weather Application</h1>
    <input v-model="city" type="text" placeholder="Enter city name">
    <button @click="searchWeather">Search</button>

    <div class="weather" v-if="weather.cityname">
      <div class="city-info">
          <h2 class="city-name">{{weather.cityname}}</h2>
          <p class="city-name">{{weather.weather}}</p>
          <h2 class="temp">
              <!-- em标签 斜体-->
              <em>{{weather.temp}}</em>℃
          </h2>
          <div class="detail">
              <span>deg: {{weather.deg}}</span> |
              <span>gust: {{ weather.gust }}</span> |
              <span>speed: {{ weather.speed }}</span>
          </div>
      </div>
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
      errorMessage: '',
      icon: '',
      weather: {
        cityname: '',
        weather: '',
        temp: ''
      }
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
          console.log(data)
          this.weather.cityname = data.name
          this.weather.temp = data.main.temp
          this.weather.weather = data.weather[0].main
          this.weather.deg = data.wind.deg
          this.weather.gust = data.wind.gust
          this.weather.speed = data.wind.speed
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

.weather {
  width: 500px;
  margin: 20px auto;
  /* border: 1px; */
  background: #a5ffff;
  padding: 5px;
  border-radius: 15px;
}
.nav {
    overflow: auto;
    padding: 10px;
}

.time {
    float: left;
}

.city {
    float: right;
}

.city-info {
    text-align: center;
}

.temp {
    font-size: 26px;
}

.temp em {
    font-style: normal;
    font-size: 34px;
}

</style>
