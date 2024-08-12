#include <Arduino.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <WiFi.h>
#include <vector>
#include <iostream>
#include "config.hpp"
#include "report.hpp"

HTTPClient httpClient;
String* jsonReportData = nullptr;
StaticJsonDocument<200>* jsonReportDocument = nullptr;
std::vector<Report> pendingReports;
int nextSendReportTime = 0.0;

bool isPumpOn = false;

void setup() {
    Serial.begin(115200);
    analogReadResolution(12);
    pinMode(PUMP_PIN, OUTPUT);

    jsonReportData = new String();
    jsonReportDocument = new StaticJsonDocument<200>();

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while(WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }

    Serial.println("Connected to WiFi!");
}

bool isServerAlive() {
    httpClient.begin(SERVER_HEALTH_ENDPOINT);
    int responseCode = httpClient.GET();
    httpClient.end();

    return responseCode == HTTP_CODE_OK;
}

inline bool isTimeToSendReport(unsigned long time) {
    return nextSendReportTime < time;
}

inline void updateNextSendReportTime(unsigned long time) {
    nextSendReportTime = time + REPORT_INTERVAL_MS;
}

Report createReport(int timestamp, int humidity) {
    Report report = {"", timestamp, humidity};
    std::copy(std::begin(PLANT_UUID), std::end(PLANT_UUID), std::begin(report.plantId));
    return report;
}

void fillJsonDocumentReport(StaticJsonDocument<200>* jsonDocument, const Report& report) {
    (*jsonDocument)["plant_id"] = String(report.plantId);
    (*jsonDocument)["timestamp"] = report.timestamp;
    (*jsonDocument)["humidity"] = report.humidity;
}

bool sendReport(const Report& report) {
    jsonReportData->clear();
    jsonReportDocument->clear();
    fillJsonDocumentReport(jsonReportDocument, report);
    serializeJson(*jsonReportDocument, *jsonReportData);

    httpClient.begin(SERVER_REPORT_ENDPOINT);
    httpClient.addHeader("Content-Type", "application/json");
    int responseCode = httpClient.POST(*jsonReportData);
    httpClient.end();

    return responseCode == HTTP_CODE_CREATED;
}

void sendPendingReports() {
    for(auto reportIterator = pendingReports.begin(); reportIterator != pendingReports.end(); ) {
        if(sendReport(*reportIterator)) {
            pendingReports.erase(reportIterator);
        } else {
            reportIterator++;
        }
    }
}

void loop() {
    unsigned long timestamp = millis();
    float humidity = analogRead(HUMIDITY_SENSOR_PIN);

    if(isTimeToSendReport(timestamp)) {
        Report report = createReport(timestamp, humidity);
        if(WiFi.status() != WL_CONNECTED || !isServerAlive() || !sendReport(report)) {
            pendingReports.push_back(report);
        } else {
            sendPendingReports();
        }
        updateNextSendReportTime(timestamp);
    }

    if(humidity < HUMIDITY_PERCENTAGE_START_PUMP_THRESHOLD && !isPumpOn) {
        digitalWrite(PUMP_PIN, HIGH);
        isPumpOn = true;
    } else if(humidity > HUMIDITY_PERCENTAGE_STOP_PUMP_THRESHOLD && isPumpOn) {
        digitalWrite(PUMP_PIN, LOW);
        isPumpOn = false;
    }
}
