EOD BOT Mk. 2 

Špecifikácia

Jedná sa o pásové UGW riadené pomocou PC a ovládača. Počítač komunikuje cez PC pomocou Raspberry pi 4 cez uzavretú lokálnu WiFi sieť, ktorú si budeme vytvárať vlastným access pointom. RPI komunikuje s mikrokontrolérom(mi) STM pomocou USART zbernice. Mechanická časť práce je už hotová.

 Mikrokontroléry budú mať na starosti 
-	Riadenie hnacích motorov (2x 12/24V DC) pomocou PWM signálov
-	Zber dát zo senzorov (Ultrazvukový senzor, teplomer, laserový diaľkomer, gyroskop (prone to changes))
-	Kamera na servách pre ovladanie osí X a Y pomocou servomodulu cez I2C
RPI bude mať na starosti:
-	Kameru
-	Prenos dát medzi PC a STM

Riadiaca aplikácia
-	Zobrazovanie obrazu a telemetrie (graficky, textovo)
-	Spracovavať vstupy z joysticku (generic Xbox360 controller)
-	Komunikaciu po lokalnej wifi sieti s RPI

