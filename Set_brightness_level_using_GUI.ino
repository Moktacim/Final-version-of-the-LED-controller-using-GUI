#include <FastLED.h>

// #define LED_PIN_2 2
#define LED_PIN_3 3
// #define LED_PIN_4 4
#define LED_PIN_5 5
#define LED_PIN_6 6
// #define LED_PIN_7 7
// #define LED_PIN_8 8
#define LED_PIN_9 9
#define LED_PIN_10 10
#define LED_PIN_11 11
// #define LED_PIN_12 12


#define NUM_LEDS 33

CRGB leds[NUM_LEDS];

void setup()
{
  Serial.begin(115200);

  FastLED.addLeds<WS2811, LED_PIN_3, RGB>(leds, NUM_LEDS);
  // FastLED.addLeds<WS2811, LED_PIN_4, RGB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2811, LED_PIN_5, RGB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2811, LED_PIN_6, RGB>(leds, NUM_LEDS);
  // FastLED.addLeds<WS2811, LED_PIN_7, RGB>(leds, NUM_LEDS);
  // FastLED.addLeds<WS2811, LED_PIN_8, RGB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2811, LED_PIN_9, RGB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2811, LED_PIN_10, RGB>(leds, NUM_LEDS);
  // FastLED.addLeds<WS2811, LED_PIN_11, RGB>(leds, NUM_LEDS);
  // FastLED.addLeds<WS2811, LED_PIN_12, RGB>(leds, NUM_LEDS);

  FastLED.setBrightness(100);
}

void loop()
{
  static byte buffer[1024];
  static int index = 0;
  static int brightness = 100; // Default brightness

  // Read the data from the serial port
  while (Serial.available() > 0)
  {
    byte data = Serial.read();

    if (data == '[')
    {
      index = 0; // Reset the buffer index
    }
    else if (data == ']')
    {
      // Parse the buffer
      int i = 0;
      char *p = strtok((char *)buffer, " ,");
      int values[NUM_LEDS * 3 + 1] = {0}; // Array to store the received values
      while (p != NULL && i < NUM_LEDS * 3)
      {
        values[i] = atoi(p);
        i++;
        p = strtok(NULL, " ,");
      }

      // Set the LED colors
      for (int ledIndex = 0; ledIndex < NUM_LEDS; ledIndex++)
      {
        int colorIndex = ledIndex * 3;
        if (values[colorIndex + 1] >= 0 && values[colorIndex + 1] <= 255 && values[colorIndex + 2] >= 0 && values[colorIndex + 2] <= 255 && values[colorIndex + 3] >= 0 && values[colorIndex + 3] <= 255)
        {
          leds[ledIndex].r = values[colorIndex + 1];
          leds[ledIndex].g = values[colorIndex + 2];
          leds[ledIndex].b = values[colorIndex + 3];
        }
      }

      // Set the brightness
      if (values[0] >= 0 && values[0] <= 255)
      {
        brightness = values[0];
        FastLED.setBrightness(brightness);
      }

      FastLED.show();
    }
    else
    {
      buffer[index++] = data;
    }
  }
  FastLED.clear();
}
