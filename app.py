from flask import Flask, render_template, request, send_file
import json
import os
from datetime import datetime
from weather import get_weather_data

app = Flask(__name__)
HISTORY_DIR = 'search_history'
if not os.path.exists(HISTORY_DIR):
    os.makedirs(HISTORY_DIR)

# Function to save search history in JSON files
def save_search_history(data, location):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(os.path.join(HISTORY_DIR, f"{date}-{location}.json"), 'w') as file:
        json.dump(data, file)

@app.route('/weather', methods=['GET', 'POST'])
def display_weather():
    if request.method == 'POST':
        location = request.form.get('location')
        try:
            # Fetch weather data and save to history
            weather_data = dict(get_weather_data(location))
            save_search_history(weather_data, location)
            return render_template('index.html', **weather_data, location=location)
        except Exception as e:
            return render_template('index.html', error=str(e))
    else:
        return render_template('index.html')

@app.route('/weather/download_history')
def download_history():
    try:
        # List all files in the search history directory
        files = os.listdir(HISTORY_DIR)
        files.sort()
        return render_template('download_history.html', files=files)
    except Exception as e:
        return str(e), 404

@app.route('/weather/history_files/<filename>')
def download_file(filename):
    file_path = os.path.join(HISTORY_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found.", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
