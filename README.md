# Weather App

A simple weather application built with Flask that retrieves and displays weather data for a specified location. It also allows users to download the search history.

## Features

- Fetches weather data using the Open-Meteo API.
- Displays current weather conditions including maximum and minimum temperatures and humidity.
- Saves search history and allows users to download it.
- Responsive and user-friendly interface.

## Project Structure

```plaintext
weatherapp/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── download_history.html
├── testing.py
├── weather.py
```

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/eilaytal/weather-app.git
    cd weatherapp
    ```

2. **Create a virtual environment and activate it** (optional but recommended):

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to** `http://127.0.0.1:5000/weather`.

3. **Enter a city name to get the weather forecast**.

## Routing

### `/weather` [GET, POST]

- **GET**: Renders the main page with a form to input the city name.
- **POST**: Processes the city name submitted by the user, fetches the weather data, and displays it.

### `/weather/download_history` [GET]

- Lists all the files in the search_history directory, allowing users to see their search history.

### `/weather/history_files/<filename>` [GET]

- Downloads the specified search history file.

## Running Tests

To run the tests, use the following command:

```sh
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


