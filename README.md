# erenacarel_2
ESP32 and OLED TFT SCREEN

TR Açıklama:
ESP32 ile OLED ekran üzerinde konuma göre şekil çizmesini hedefledim. Yani ekran alt tarafa doğru eğildiğinde alt tarafa orayı dolduracak biçimde dikdörtgen çizmesini sağladım. 
Bununla birlikte ekran üst tarafa doğru eğildiğinde oraya dikdörtgen çizmesini sağladım. Ekran çaprazlara doğru eğilidiğinde ise oradaki köşe kısmına üçgen çizmesini sağladım.
Sürekli ekranın konumu değiştiğinde ekranımız kendini güncelleyecek ve ekranın eğildiği yere şekil çizilecektir.

ESP32 ile OLED ekran üzerinde, işlemcimize bağlı olan sıcaklık/nem(SHTC3) ve konum(LMSDO) sensörleriniden alınan değerleri yazdırmayı hedefledim. Sıcaklık/nem ve konum değerleri 
sürekli güncellenecek ve ekrana da bu yansıyacaktır. Bununla birlikte işlemcimize bağlı butonlardan alınan 1 veya 0 değeri de ekranda sürekli güncel bir halde yazacaktır.

ESP32 işlemcimize bağlı 4 adet neopixel ledlerin rastgele bir renkte yanmasını sağladım. Bununla birlikte yine şekil çiziminde olduğu gibi eğim olan yerde bazı neopixel ledlerin 
yanmasını sağladım. 

tri_rect_toget.py  --> Bu dosyada belirtilen pozisyonlara ekranın konumuna göre dikdörtgen ve üçgen beraber çizilmiştir. display.clear() ile ekranda sürekli güncellemeler 
yapılabiliyor. Üçgen çizimi için gfx_triangle_lib.py kütüphanesinden GFX sınıfını graphics değişkenine atadım. 

tri_rect_neopixel_toget.py  -->  Bu dosyada ekranın konum pozisyonuna göre sadece üçgen veya dikdörgen çizilmesini hedefledim.

neopix.py  --> Bu dosyamızda neopixel ledleri için kütüphane bulunmaktadır. Elimizdeki 4 adet neopixel ledi bir while döngüsünde döndürebiliriz ve rastgele renkler elde 
edebiliriz.

mainYedek2.py  --> Bu dosyamızda sıcaklık/nem, konum ve buton değerlerimizi yazdırmayı hedefledim. Text yazdırmak için ili9341.py kütüphanesinden faydalandım. Araya sınır çizmek 
için gfx_triangle_lib.py kütüphanesini kullandım. Ekranın konumuna göre neopixel ışıkların rastgele renkte yanmasını istedim.

xglcd_font.py  --> Bu kütüphanemiz ekrana text yazdırırken font oluşturmada işimize yaramaktadır. Ben expresso_dolce fontunu kullandım. 

main.py  --> Bu dosyamızda okunması gereken değerlerin tanımını ve onların karşılığını ayrı ayrı yazdık. Sebebi ise ekrana yazdırma işlemini daha hızlı gerçekleştirmektir.
(Picture_1_Button_Active and Picture_2_Button_Active)


ENG explanation:
With ESP32, I aimed to draw a shape according to the position on the OLED screen. In other words, when the screen is tilted towards the bottom, I have it draw a rectangle on the 
bottom side to fill it. However, when the screen is tilted towards the top, I have it draw a rectangle there. When the screen is tilted towards the diagonals, I made it draw a 
triangle on the corner there. When the position of the screen changes constantly, our screen will update itself and a shape will be drawn where the screen is tilted.

With ESP32, I aimed to print the values taken from the temperature/humidity (SHTC3) and position (LMSDO) sensors connected to our processor on the OLED screen. 
Temperature/humidity and location values will be updated continuously and this will be reflected on the screen. In addition, the value of 1 or 0 obtained from the buttons 
connected to our processor will also be constantly updated on the screen.

I made 4 neopixel leds connected to our ESP32 processor light up in a random color. However, as in the figure drawing, I made some neopixel leds light up where there is a slope.

tri_rect_toget.py  --> Rectangle and triangle are drawn together at the positions specified in this file, according to the position of the screen. Continuous updates can be made 
on the screen with display.clear(). For triangle drawing, I assigned the GFX class to the graphics variable from the gfx_triangle_lib.py library.

tri_rect_neopixel_toget.py  --> In this file, I aimed to draw only triangles or rectangles according to the position location of the screen.

neopixel.py  --> In this file, there is a library for neopixel leds. We can rotate 4 neopixel LEDs in a while loop and get random colors.

mainYedek2.py  --> In this file, I aimed to print our temperature/humidity, location and button values. I used the ili9341.py library to print text. I used the 
gfx_triangle_lib.py library to draw a border. I wanted the neopixel lights to turn on in a random color according to the position of the screen.

xglcd_font.py  --> This library is useful for creating fonts while printing text on the screen. I used expresso_dolce font.

main.py  --> In this file, I wrote the definition of the values that should be read and their equivalents separately. The reason is to perform the printing to the screen faster.
(Picture_1_Button_Active and Picture_2_Button_Active)
