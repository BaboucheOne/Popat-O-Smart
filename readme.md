
# Potato-O-Smart
Potato-O-Smart is a simple, all-in-one repository solution for a connected plant. It includes frontend, backend, and embedded code for the ESP32. Additionally, you can find circuit diagrams and 3D models to build your own connected plant.

# Installation 🛠️
## Frontend
## Backend
- Install [pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
- Install `requirements.txt` in a venv.
- Run main.py
## Embedded
- Install [vscode](https://code.visualstudio.com/download)
- Install [C/C++ extension](https://code.visualstudio.com/docs/languages/cpp)
- Install [platformIO extension](https://platformio.org/platformio-ide)
- Open `embedded` folder with platformIO.
- Build & Upload.

# Configuration ⚙️
## Frontend
## Backend
In `backend` create two files named `.env.dev` and `.env.prod`. These are your configuration to run the backend.

This is an example of `.env.dev`:
```md
MONGODB_CONNECTION_STRING=mongodb://localhost:27017/
MONGODB_CONNECTION_TIMEOUT_MS=50000
MONGODB_DATABASE_NAME=PotatoSmartPlant
REPORT_COLLECTION_NAME=reports
SERVER_IP=127.0.0.1
SERVER_PORT=8000
LOGGER_FILENAME=log.log
```
## Embedded
In `embedded/src` create a file name `config.hpp`. This file will contains information relative to your wifi and server configuration that the ESP32 will use.

:point_right: Do not commit this file at all. (Already setup into the .gitignore)

```hpp
#ifndef CONFIG_HPP
#define CONFIG_HPP

constexpr char WIFI_SSID[] = "YOUR_WIFI_SSID";
constexpr char WIFI_PASSWORD[] = "YOUR_WIFI_PASSWORD";

constexpr char SERVER_REPORT_ENDPOINT[] = "http://SERVER_IP:PORT/report";
constexpr char SERVER_HEALTH_ENDPOINT[] = "http://SERVER_IP:PORT/health";
constexpr char PLANT_UUID[37] = "c303282d-f2e6-46ca-a04a-35d3d873712d";

constexpr unsigned long REPORT_INTERVAL_MS = 10 * 60 * 1000;

constexpr int HUMIDITY_SENSOR_PIN = 3;
constexpr int PUMP_PIN = 4;

constexpr float HUMIDITY_PERCENTAGE_START_PUMP_THRESHOLD = 45.0;
constexpr float HUMIDITY_PERCENTAGE_STOP_PUMP_THRESHOLD = 70.0;

#endif
```

| Name           | Explanation       |
| -------------- | -------------- |
| PLANT_UUID     | UUID to identity your plant into the server.|
| REPORT_INTERVAL_MS | Milliseconds to wait before sending another report |


