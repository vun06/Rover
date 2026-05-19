import time
from LCD import LCD

# Initialize the LCD with specific parameters: Raspberry Pi revision, I2C address, and backlight status
lcd = LCD(2, 0x27, True)

# Display messages on the LCD
lcd.message("Hello", 1)
lcd.message("Mr. Burnham", 2)

# Keep the messages displayed for 5 seconds
time.sleep(5)



