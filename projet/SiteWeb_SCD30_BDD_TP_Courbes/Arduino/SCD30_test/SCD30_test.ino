#include "SCD30.h"
void setup() {
    Wire.begin();
    Serial.begin(9600);
    Serial.println("SCD30 Raw Data");
    scd30.initialize();
}
void loop() {
    float result[3] = {0};

    if (scd30.isAvailable()) {
        scd30.getCarbonDioxideConcentration(result);
        Serial.print("Carbon Dioxide Concentration is: ");
        Serial.print(result[0]);
        Serial.println(" ppm");
        Serial.println(" ");
        Serial.print("Temperature = ");
        Serial.print(result[1]);
        Serial.println(" ℃");
        Serial.println(" ");
        Serial.print("Humidity = ");
        Serial.print(result[2]);
        Serial.println(" %");
        Serial.println(" ");
        Serial.println(" ");
        Serial.println(" ");
    }

    delay(2000);
}
