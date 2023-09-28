from machine import UART, delay, LED
import music


def init_BLE():
    # RL62M01 change to CMD mode
    ble.write('!CCMD@')
    delay(150)
    ble.write('AT+MODE_DATA\r\n')
    delay(50)
    ble.read(ble.any())  # clear UART buffer

# init a UART port read a line timeout is 100ms
ble = UART(1, 115200, timeout=100)
init_BLE()
ledy = LED('ledy')
ledr = LED('ledr')

while True:
    recv_data = str(ble.readline(), 'utf-8').strip()
    data = []
    if recv_data:
        ledy.toggle()
        if recv_data in ('C', 'D', 'E', 'F', 'G', 'A', 'B'):
            data.append(recv_data)
            music.play(data, wait=True)
