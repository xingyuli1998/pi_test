import serial

class Arduino_sensor():
    def __init__(self,serialPosrt,baudRate,timeout):
        self.serialPosrt = serialPosrt
        self.baudRate = baudRate
        self.timeout = timeout
        

        
    def read_data(self):
        # 设置端口变量和值
        # 设置波特率变量和值
        # 设置超时时间,单位为s
        # 接受串口数据
        ser = serial.Serial(self.serialPosrt, self.baudRate, timeout=self.timeout)
        # 循环获取数据(条件始终为真)
        
        # 读取接收到的数据的第一行
        data = ser.readline()
        data = data.decode()
        hum = data[0:5]
        tem = data[5:10]
        data_tup = (hum,tem)
        return data_tup


    

if __name__ == "__main__":
    dht11 = Arduino_sensor('/dev/ttyACM0',9600,50)
    dht11.read_data()


