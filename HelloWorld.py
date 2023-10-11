import machine
import ssd1306
import time

# Configuración de la pantalla OLED
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Limpiar la pantalla
oled.fill(0)
oled.show()

# Mostrar "Hola, mundo"
oled.text("Hola, mundo", 0, 0, 1)
oled.show()

# Esperar unos segundos antes de salir
time.sleep(5)
