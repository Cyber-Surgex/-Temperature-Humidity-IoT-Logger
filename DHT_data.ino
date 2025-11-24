// DHT11_Logger.ino
// Reads temperature + humidity from DHT11 and sends data to Python via Serial

#include <DHT.h>

#define DHTPIN 2          // DHT11 data pin
#define DHTTYPE DHT11     // Sensor type
#define BAUDRATE 9600

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(BAUDRATE);
  dht.begin();
  delay(2000);

  Serial.println("START");   // signals Python that Arduino started
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();  // in Celsius
  unsigned long ms = millis();                // timestamp

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("ERROR,NaN,NaN");
    return;
  }

  // Format → millis,temperature,humidity
  // Example → 2000,26.5,58.2
  Serial.print(ms);
  Serial.print(",");
  Serial.print(temperature, 2);
  Serial.print(",");
  Serial.println(humidity, 2);

  delay(2000);   // 2-second interval
}
