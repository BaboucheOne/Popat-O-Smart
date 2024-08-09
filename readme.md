
# Potato-O-Smart
Potato-O-Smart is a simple, all-in-one repository solution for a connected plant. It includes frontend, backend, and embedded code for the ESP32. Additionally, you can find circuit diagrams and 3D models to build your own connected plant.

# Installation 🛠️
## Frontend
## Backend
## Embedded
- Install [vscode](https://code.visualstudio.com/download)
- Install [C/C++ extension](https://code.visualstudio.com/docs/languages/cpp)
- Install [platformIO extension](https://platformio.org/platformio-ide)
- Open `embedded` folder with platformIO.
- Build & Upload.

# Configuration ⚙️
## Frontend
## Backend
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

#endif
```

| Name      | Explanation       |
| -------------- | -------------- |
| PLANT_UUID | UUID to identity your plant into the server.|
| REPORT_INTERVAL_MS | Milliseconds to wait before sending another report |


