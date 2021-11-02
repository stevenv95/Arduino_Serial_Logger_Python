// Basic demo for accelerometer readings from Adafruit MPU6050

#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
#define numbersamples 10
void setup(void)
{
  Serial.begin(115200);
  while (!Serial)
    delay(10); // will pause Zero, Leonardo, etc until serial console opens
  // Try to initialize!
  if (!mpu.begin())
  {
    Serial.println("Failed to find MPU6050 chip");
    while (1)
    {
      delay(10);
    }
  }

  //Serial.println("MPU6050 Found!");
  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.println("");
  delay(100);
}

void loop()
{
  double val[numbersamples];
  unsigned long time[numbersamples];
  for (int i = 0; i < numbersamples; i++)
  {
    time[i] = micros();
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);
    val[i] = a.acceleration.x;
  }
  for (size_t i = 0; i < numbersamples; i++)
  {
    Serial.print("<");
    Serial.print(",");
    Serial.print(time[i]);
    Serial.print(",");
    Serial.print(val[i]);
    Serial.print(",");
    Serial.println("");
    
  }
}