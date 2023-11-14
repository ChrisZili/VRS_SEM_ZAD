EOD BOT Mk. 2 špecifikácia

	Jedná sa o UGW riadené pomocou PC a ovládača. Počítač komunikuje cez PC pomocou Raspberry pi 4 cez uzavretú lokálnu WiFi sieť, ktorú si budeme vytvárať vlastným access pointom. RPI komunikuje s mikrokontrolérom(mi) STM pomocou USART zbernice.
 Mikrokontroléry budú mať na starosti 
-	Riadenie hnacích motorov (2x 12/24V DC) pomocou PWM signálov
-	Zber dát zo senzorov (IR senzory po bokoch ako detekcia prekážky, teplomery, GPS, laserový diaľkomer, gyroskop...[TBD])
-	Kamera na servách pre ovladanie osí X a Y pomocou servomodulu cez I2C
-	Rameno prípadne iný nástroj (cez servá na I2C doske)
RPI bude mať na starosti:
-	Kameru
-	Prenos dát medzi PC a STM

Riadiaca aplikácia
-	Zobrazovanie obrazu a telemetrie (graficky, textovo)
-	Zobrazovanie GPS polohy na mape
-	Spracovavať vstupy z joysticku (generic PS4 controller)
-	Komunikaciu po lokalnej wifi sieti s RPI


Obrázok: referenčná mechanická časť projektu
