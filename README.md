## Related Repositories

- [Weather App EKS Terraform](https://github.com/eilaytal/weather-app-eks-terraform): Terraform configuration for deploying the Weather App on AWS EKS.
- [Jenkins Pipeline](https://github.com/eilaytal/jenkins_pipeline): Jenkins pipeline for automating CI/CD processes for the Weather App.
- [GitOps Manifests](https://github.com/eilaytal/gitops-manifests): GitOps manifests for managing the deployment of the Weather App.

# Weather App

A simple weather application built with Flask that retrieves and displays weather data for a specified location. It also allows users to download the search history.

## Features

- Fetches weather data using the Open-Meteo API.
- Displays current weather conditions including maximum and minimum temperatures and humidity.
- Saves search history and allows users to download it.
- Responsive and user-friendly interface.

## Project Structure

```
weatherapp/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── download_history.html
├── testing.py
├── weather.py
└── Dockerfile
```

## Installation

Clone the repository:

```bash
git clone https://github.com/eilaytal/weather-app.git
cd weatherapp
```

Create a virtual environment and activate it (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python app.py
```

Open your web browser and navigate to http://127.0.0.1:5000/weather.

Enter a city name to get the weather forecast.

## Routing

/weather [GET, POST]
- GET: Renders the main page with a form to input the city name.
- POST: Processes the city name submitted by the user, fetches the weather data, and displays it.

/weather/download_history [GET]
- Lists all the files in the search_history directory, allowing users to see their search history.

/weather/history_files/<filename> [GET]
- Downloads the specified search history file.

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
```

This README.md file now includes the project structure with the Dockerfile included.
