window.addEventListener('load', () => {
    //const weatherInfo = document.getElementById('weather-info');
    const dateInfo = document.getElementById('date-info');

    // Function to update the weather and date information
    function updateInfo() {
        // Get the current date and time
        const now = new Date();

        // Format the date and time
        const date = now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        const time = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        /*
        const apiURL = 'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=3e9d28baebcd2dbbb56b4e49177b45e1';
        fetch(apiURL)
            .then(response => response.json())
            .then(data => {
                const temperature = data.main.temp;
                weatherInfo.textContent = `Today's temperature in Regina is ${temperature}°C`;
            })
            .catch(error => {
                console.error(error);
                weatherInfo.textContent = `Failed to load weather data`;
            });

         */

        // Set the weather and date information
        dateInfo.textContent = `${date} ${time}`;
    }

    // Call the updateInfo function every second
    setInterval(updateInfo, 1000);
});
