# Photo gallery

Használt technológiák: Red Hat Openshift, Python, Javascript környezet, Django keretrendszer, Sqlite adatbázis.  

Az alkalmazás egy fényképalbum weblapját valósítja meg. Az oldalon az albumban szereplő képek listáját illetve a listából elérve egy-egy képet lehet megtekinteni.  
A projekt Django keretrendszerrel készült, a feladatkiírásban csatolt videó utasításait követve. Egy alap projektet kellett létrehozni, amely egy home és egy about page-et foglal magába, emellett a globális beállítások is ezalatt kezelhetőek. További projektek hozhatóak létre ez alá, mint például ebben az esetbern a photos alkalmazás, amiben a feladat lényegi implementációja szerepel, továbbá a users modul a felhasználók kezelése érdekében. A keretrendszer magától létrehoz már konfigurációs fájlokat amelyek szerkesztésével fel lehet építeni az alkalmazás struktúráját. A frontend oldali fejlesztés alapkoncepciója az, hogy HTML sablonokat definiálunk, amelyeket alkalmazás URL-jén belüli elérési utakhoz kötünk, emellett pedig statikus JavaScript és CSS fájlok egészítik ki az alkalmazás működését. Ezeket dinamikus adatokkal lehet tölteni, python file-okban szintén a Django eszközeivel lehet adatbázistáblákat (modelleket), logikát definiálni, ez gyakorlatilag a szerver-oldali réteg.

Funkcionalitás és Jogosultságkezelés
Az alkalmazás nem csak statikus tartalmat jelenít meg, hanem interaktív funkciókkal is rendelkezik:

Publikus nézetek: A főoldal (Home), a Rólunk (About) oldal és a Galéria lista nézete bejelentkezés nélkül is elérhető.

Részletes nézet: A listából egy képre kattintva a dinamikus URL routing (<slug:slug>) segítségével betöltődik az adott kép részletes oldala.

Védett funkciók: Új kép feltöltése csak hitelesített (bejelentkezett) felhasználók számára engedélyezett. Ezt a @login_required dekorátorral biztosítottam a backend oldalon. Emellett képet csak az a felhasználó törölhet, aki feltöltötte.

Médiafájlok és Statikus tartalmak
A Django külön kezeli a fejlesztés során használt statikus fájlokat (CSS, JS) és a felhasználók által feltöltött médiafájlokat.

Static: A stíluslapok (style.css) és scriptek (main.js) a static mappában kaptak helyet.

Media: A settings.py-ban konfigurált MEDIA_URL és MEDIA_ROOT beállítások teszik lehetővé, hogy a feltöltött képek a szerver fájlrendszerébe kerüljenek, és URL-en keresztül elérhetőek legyenek a böngésző számára

Felhőbe való telepítés:  
Red Hat Openshift PaaS környezetbe telepítettem az alkalmazást. A konzolon keresztül fel lehet venni projekteket, amelyekbe kitelepíthetőek alkalmazások. Lehet forráskódból, vagy github repository-ból importálni az alkalmazást, esetünkben az utóbbit kellett alkalmazni. A buildConfig-okkal lehet a pusholásra történő Openshiften belüli buildet paraméterezni, környezeti változókkal, a YAML leíró fájl szerkesztésével, stb. Skálázható az alkalmazás, hiszen több pod-ot lehet manuálisan is indítani, és a PaaS környezet magától, terhelés növekedés/csökkenés hatására kezeli a pod-ok indítását. Ezeknek a státuszát, hozzájuk tartozó log-ot a Topology nézetben érdemes nyomon követni. Az elvárt működés az lenne, hogy keresztbe van kötve az Openshift és a GitHub, azonban az Openshift ingyenes verziója által kiadott url-t beállítva webhooknak GitHub-on nem indul el automatikusan a build a PaaS környezetben, és tapasztalataim szerint ez másoknál is megoldhatatlan problémát okozott.
