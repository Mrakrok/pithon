# Zadání

1. Zobrazte manuálovou stránku programu ls a najděte v ní, jak seřadit soubory podle jejich velikosti.

2. Popište, jak se v manuálové stránce vyhledává.

3. Vytvořte proměnnou prostředí heslo, která bude obsahovat Vaše osobní číslo studenta.

4. Vypište obsah proměnné SHELL.

5. Pomocí shellu vypočítejte 2048 * 18 - 397 a výsledek uložte do proměnné vysledek.

6. Nastavte jako svůj pracovní adresář /tmp a následně jedním příkazem ve svém domovském adresáři vytvořte adresář psk-zk.

7. Nastavte jako svůj pracovní adresář psk-zk a zkopírujte soubor /etc/group do aktuálního pracovního adresáře.

8. Zkopírujte celý adreář (ne jen jeho obsah) /etc/init.d do adresáře psk-zk.

9. Přejmenujte právě zkopírovaný adresář init.d na setup.

10. Přejmenujte soubor ~/psk-zk/group na ~/psk-zk/prog.sh

11. Nastavte přístupová práva tak, aby soubor prog.sh byl spustitelný.

12. Všem souborům v adresáři psk-zk/setup odeberte (pomocí "žolíkových" znaků) právo pro čtení všemi uživateli.

13. Nastavte přístupová práva tak, všichni ostatní uživatelé směli číst adresář psk-zk a jeho obsah a zároveň tak, aby nemohli číst váš domovský 
adresář.

14. Smažte adresář psk-zk.

# Odpovědi

1. ls --help <br>
najdeš -S<br>
(ls -S)

2. whatis

3. heslo = číslo_studenta <br>
echo = $heslo<br> *(alt + ů = $)*
vypíše číslo_studenta <br>

4.

5. echo ((2048 * 18 - 397))<br> *nebo* <br>
echo [2048 * 18 - 397]

6.  cp -r /etc/init.d /home/uzivatel/psk-zk<br>
*(-r ,dovolí kopírovat složky)*
