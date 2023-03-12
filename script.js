

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

function openPopup() {
    // Create the popup element
    var popup = document.createElement("div");
    popup.id = "popup";
    popup.style.position = "fixed";
    popup.style.top = "50%";
    popup.style.left = "50%";
    popup.style.transform = "translate(-50%, -50%)";
    popup.style.background = "white";
    popup.style.padding = "20px";
    popup.style.border = "1px solid black";

    // Add a form for uploading images and submitting a web link
    popup.innerHTML = `
    <h2>Customize Image</h2>
    <form>
      <label for="image-file">Upload Image:</label>
      <input type="file" id="image-file" name="image-file"><br><br>
      <label for="web-link">Submit Web Link:</label>
      <input type="text" id="web-link" name="web-link"><br><br>
      <button type="submit">Submit</button>
    </form>
  `;

    // Add the popup to the body
    document.body.appendChild(popup);
}

