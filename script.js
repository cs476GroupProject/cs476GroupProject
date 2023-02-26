window.addEventListener('load', () => {
    //const weatherInfo = document.getElementById('weather-info');
    const dateInfo = document.getElementById('date-info');
    function updateInfo() {
        const now = new Date();

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

        dateInfo.textContent = `${date} ${time}`;
    }
    setInterval(updateInfo, 1000);
});

window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    var scrollPosition = window.scrollY;

    if (scrollPosition >= header.offsetHeight) {
        header.classList.add('sticky');
    } else {
        header.classList.remove('sticky');
    }
    if (scrollPosition > header.offsetTop) {
        header.classList.add('header-hidden');
    } else {
        header.classList.remove('header-hidden');
    }
});




