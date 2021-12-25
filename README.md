# erenacarel_2
ESP32 and OLED TFT SCREEN

TR:
ESP32 ile OLED ekran üzerinde konuma göre şekil çizmesini hedefledim. Yani ekran alt tarafa doğru eğildiğinde alt tarafa orayı dolduracak biçimde dikdörtgen çizmesini sağladım. 
Bununla birlikte ekran üst tarafa doğru eğildiğinde oraya dikdörtgen çizmesini sağladım. Ekran çaprazlara doğru eğilidiğinde ise oradaki köşe kısmına üçgen çizmesini sağladım.
Sürekli ekranın konumu değiştiğinde ekranımız kendini güncelleyecek ve ekranın eğildiği yere şekil çizilecektir.

ESP32 ile OLED ekran üzerinde, işlemcimize bağlı olan sıcaklık/nem(SHTC3) ve konum(LMSDO) sensörleriniden alınan değerleri yazdırmayı hedefledim. Sıcaklık/nem ve konum değerleri sürekli güncellenecek ve ekrana da bu yansıyacaktır. Bununla birlikte işlemcimize bağlı butonlardan alınan 1 veya 0 değeri de ekranda sürekli güncel bir halde yazacaktır.

ESP32 işlemcimize bağlı 4 adet neopixel ledlerin rastgele bir renkte yanmasını sağladım. Bununla birlikte yine şekil çiziminde olduğu gibi eğim olan yerde bazı neopixel ledlerin yanmasını sağladım. 

ENG:
With ESP32, I aimed to draw a shape according to the position on the OLED screen. In other words, when the screen is tilted towards the bottom, I have it draw a rectangle on the 
bottom side to fill it. However, when the screen is tilted towards the top, I have it draw a rectangle there. When the screen is tilted towards the diagonals, I made it draw a 
triangle on the corner there. When the position of the screen changes constantly, our screen will update itself and a shape will be drawn where the screen is tilted.

With ESP32, I aimed to print the values taken from the temperature/humidity (SHTC3) and position (LMSDO) sensors connected to our processor on the OLED screen. 
Temperature/humidity and location values will be updated continuously and this will be reflected on the screen. In addition, the value of 1 or 0 obtained from the buttons 
connected to our processor will also be constantly updated on the screen.

I made 4 neopixel leds connected to our ESP32 processor light up in a random color. However, as in the figure drawing, I made some neopixel leds light up where there is a slope.
