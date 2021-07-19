#include <DHT.h>
#define DHTPIN A2
#define DHTTYPE DHT11
int sensorValue = 0;
const int sensorPin = A0;
int RelayPin=13;
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  //digitalWrite(13,LOW);
  pinMode(sensorPin, INPUT);
  dht.begin();
} 
void loop() {
  // Wait a few seconds between measurements.
  delay(500);
  sensorValue = analogRead(sensorPin);
  Serial.print(sensorValue);
  if(sensorValue < 550){            
      digitalWrite(13,HIGH);
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      if (isnan(h) || isnan(t)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
      }
      Serial.print(h);
      Serial.println(t);
      delay(1000);       
  }else{
      digitalWrite(13,LOW);
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      if (isnan(h) || isnan(t)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
      }
      Serial.print(h);
      Serial.println(t); 
      delay(1000);
  }
}
