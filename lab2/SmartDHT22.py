#!/usr/bin/python
import sys
import Adafruit_DHT
class SmartDHT22:
    def __init__(self, pin):
        temperature, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,pin)
    def get_temp_celsius(SmartDHT22):
        temperature, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4) 
        return temperature
    def get_temp_fahrenheit(SmartDHT22):
        temperature, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
        celsius = temperature*(9/5.0)+32
        return celsius
    def get_humidity(SmartDHT22):
        temperature, humidity = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
        return humidity


