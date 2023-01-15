/////humidity and temperature///////
#include "DHT.h"             // DHT sensors library
#define dhtPin 8             // This is data pin
#define dhtType DHT22        // This is DHT 22 sensor
DHT dht(dhtPin, dhtType);    // Initialising the DHT library
float humValue;           // value of humidity
float temperatureValueC;  // value of temperature in degrees Celcius
///////humidity and temperature///////

///////light intensity///////
double Light (int RawADC0)
{
  double Vout=RawADC0*0.0048828125;
  float lux=500/(10*((5-Vout)/Vout));//use this equation if the LDR is in the upper part of the divider
  // int lux=(2500/Vout-500)/10;
  return lux;
}
///////light intensity///////

//////Inside Air Quality//////
int airQuality = A1;
int co2Level;
//////Inside Air Quality//////

void setup() {
  Serial.begin(9600);
///////humidity and temperature///////
  dht.begin();               // start reading the value from DHT sensor
///////humidity and temperature///////

}

void loop() {
  
///////humidity and temperature///////
  humValue = dht.readHumidity();               // value of humidity
  temperatureValueC = dht.readTemperature();   // value of temperature in degrees Celcius
  Serial.print(humValue);     // get value of humidity
  Serial.print(" , ");          // create space after the value of humidity
  Serial.print(temperatureValueC);  // get value of temperature in degrees Celcius
///////humidity and temperature///////

///////light intensity///////
Serial.print(" , ");
Serial.print(float(Light(analogRead(0))));
///////light intensity///////

//////Air Quality//////
  int airQualityData = analogRead(airQuality);
  co2Level = airQualityData - 112;
  co2Level = map(co2Level,0,1024,400,5000);
  Serial.print(" , ");
  Serial.println(co2Level);
//////Air Quality//////

  delay(15000);
}
