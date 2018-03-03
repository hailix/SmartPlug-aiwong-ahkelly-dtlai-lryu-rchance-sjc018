import sys
sys.path.insert(0,"/home/pi")
import time
import SmartDHT22
import SmartMCP3008
import SmartSound
import sqlite3

class SensorSQL:
    def __init__(self):
        self.sensor_data=0
    def get_sensor(self,sensor):
        if (sensor == 'MCP'):
            self.sensor_data=self.get_MCP()
        elif(sensor=='DHT'):
            self.sensor_data=self.get_DHT()
        elif(sensor=='SS'):
            self.sensor_data=self.get_SS()
        else:
            print(0)

    def set_sensor(self,sensor):
        self.writeToDB(sensor)    
    
    def get_MCP(self):
        MCP=SmartMCP3008.SmartMCP3008()
        voltage = MCP.read(0)
        return voltage,

    def get_DHT(self):
        DHT=SmartDHT22.SmartDHT22(18)
        celsius=DHT.get_temp_celsius()
        fah=DHT.get_temp_fahrenheit()
        hum=DHT.get_humidity()
        return celsius,fah,hum

    def get_SS(self):
        SS = SmartSound.SmartSound()
        gate=SS.get_gate()
        envelope=SS.get_envelope()
        audio=SS.get_audio()
        return gate,envelope,audio

    def writeToDB(self,sensor):
        
        # Insert a row of data
        if (sensor=='MCP'):
            c.execute("INSERT INTO "+sensor+" VALUES (?)",[self.sensor_data[0],])
        else:
            c.execute("INSERT INTO "+sensor+" VALUES (?,?,?)",[self.sensor_data[0], self.sensor_data[1], self.sensor_data[2]])
        
       # Save (commit) the changes
        conn.commit()

if __name__ == "__main__":
    i=1
    conn=sqlite3.connect('sensor_dash.db')
    c=conn.cursor()
    SenToSql = SensorSQL()
    c.execute('''DROP TABLE IF EXISTS MCP''')
    c.execute('''DROP TABLE IF EXISTS DHT''')
    c.execute('''DROP TABLE IF EXISTS SS''')
    c.execute('''DROP TABLE IF EXISTS Temp_Hum''')
    c.execute('''DROP TABLE IF EXISTS Light''')
    c.execute('''DROP TABLE IF EXISTS Sound_E''')
    
    # Create table
    c.execute('''CREATE TABLE MCP
                 (voltage real)''')
    c.execute('''CREATE TABLE DHT
                (celsius real, fahrenheit real, humidity real)''')
    c.execute('''CREATE TABLE SS
                (gate real, envelope real, audio real)''')

    while (i<=60):

        SenToSql.get_sensor('MCP')
        SenToSql.set_sensor('MCP')
        SenToSql.get_sensor('DHT')
        SenToSql.set_sensor('DHT')
        SenToSql.get_sensor('SS')
        SenToSql.set_sensor('SS')
        # Save (commit) the changes
        conn.commit()

        print("querying from database to check values at timestamp ", i)

        c.execute("select * from MCP")
        print(c.fetchall())
        c.execute("select * from DHT")
        print(c.fetchall())
        c.execute("select * from SS")
        print(c.fetchall())

        print("done querying at timestamp ", i)
        i=i+1

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
