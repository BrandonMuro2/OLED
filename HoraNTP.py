import network
import urequests
import utime
from machine import Pin, I2C
import ssd1306

# Conectar a la red WiFi
def conectar_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectándose a la red WiFi...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            utime.sleep(1)  # Espera 1 segundo antes de verificar nuevamente
        print('Conexión WiFi exitosa')
        print('Dirección IP:', sta_if.ifconfig()[0])

# Obtener la hora desde un servicio web
def obtener_hora_desde_servicio_web():
    try:
        response = urequests.get("http://worldtimeapi.org/api/ip")
        datos = response.json()
        return datos['datetime']
    except Exception as e:
        print("Error al obtener la hora desde el servicio web:", e)
        return None

# Configurar el display OLED
def configurar_oled():
    i2c = I2C(0, sda=Pin(0), scl=Pin(1))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    return oled

# Mostrar la hora en la pantalla OLED
def mostrar_hora_en_oled(oled, hora):
    oled.fill(0)
    oled.text("Hora actual:", 0, 0)
    oled.text(hora, 0, 16)
    oled.show()

# Programa principal
def main():
    ssid = "TecNM-ITT-Docentes"
    password = "tecnm2022!"

    conectar_wifi(ssid, password)
    oled = configurar_oled()

    while True:
        hora = obtener_hora_desde_servicio_web()

        if hora is not None:
            print("Hora actual:", hora)
            mostrar_hora_en_oled(oled, hora)

        utime.sleep(60)  # Espera 60 segundos antes de actualizar nuevamente

if __name__ == '__main__':
    main()
