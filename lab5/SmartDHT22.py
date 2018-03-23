#!/usr/bin/python
import sys
import Adafruit_DHT
class SmartDHT22:
    def __init__(self, pinNum):
        self.dht = Adafruit_DHT.DHT22
        self.p = pinNum
    def get_temp_celsius(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht,self.p) 
        return temperature
    def get_temp_fahrenheit(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht,self.p)
        celsius = temperature*(9/5.0)+32
        return celsius
    def get_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht,self.p)
        return humidity


