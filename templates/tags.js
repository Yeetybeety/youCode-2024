const tags = document.querySelectorAll('.tag');
        tags.forEach(tag => {
            tag.addEventListener('change', () => {
                tag.nextElementSibling.classList.toggle('bg-blue-500');
                tag.classList.toggle('selected');
            });
        });


        const form = document.getElementById('searchForm');
        const weatherInfo = document.getElementById('weatherInfo');
        
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const location = document.getElementById('weather').value;
        
            fetchWeather(location)
            .then(weatherData => {
              console.log(weatherData);

              const keywords = getKeywords(weatherData);
              console.log(keywords);

          })
          .catch(error => {
              console.error('Error fetching weather data:', error);
          });
            
        });
        
        async function fetchWeather(location) {
            const apiKey = '819c1831006701474962e990a731fdf1';
            const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=${apiKey}`;
        
            try {
                const response = await fetch(apiUrl);
                const data = await response.json();
        
                // Check if location is valid
                if (data.cod === '404') {
                    weatherInfo.textContent = 'Location not found';
                } else {
                    const weatherDescription = data.weather[0].description;
                    const temperature = Math.round(data.main.temp - 273.15); // Convert temperature to Celsius
                    const cityName = data.name;

                    weatherInfo.innerHTML = `<p>Weather in ${cityName}: ${weatherDescription}</p>
      <p>Temperature: ${temperature}°C</p>`;
                };
                 
      

            } catch (error) {
                console.error('Error fetching weather data:', error);
            }
        }

        function getKeywords(weatherData) {
          const keywords = [];
      
          // Check weather description
          if (weatherData.weatherDescription.includes('rain')) {
              keywords.push('rain');
          }
      
          // Check temperature
          const temperature = weatherData.temperature;
          if (temperature > 30) {
              keywords.push('hot');
          } else if (temperature < 10) {
              keywords.push('cold');
          } else {
          }
      
          return keywords;
      }
       