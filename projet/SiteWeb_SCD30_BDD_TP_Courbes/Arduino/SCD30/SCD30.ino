#include "SCD30.h"
void setup() {
    Wire.begin();
    Serial.begin(9600);
    scd30.initialize();
}
void loop() {
    float result[3] = {0};
    if (scd30.isAvailable()) 
      {
        scd30.getCarbonDioxideConcentration(result);
        Serial.println(result[2]);
        Serial.println(result[1]);
        Serial.println(result[0]);
      }

    delay(2000);
}
