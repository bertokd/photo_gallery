# Photo gallery

Használt technológiák: Red Hat Openshift, Python, Javascript környezet, Django keretrendszer, Sqlite adatbázis.  

Az alkalmazás egy fényképalbum weblapját valósítja meg. Az oldalon az albumban szereplő képek listáját illetve a listából elérve egy-egy képet lehet megtekinteni.  
A projekt Django keretrendszerrel készült, a feladatkiírásban csatolt videó utasításait követve. Egy alap projektet kellett létrehozni, amely egy home és egy about page-et foglal magába, emellett a globális beállítások is ezalatt kezelhetőek. További projektek hozhatóak létre ez alá, mint például ebben az esetbern a photos alkalmazás, amiben a feladat lényegi implementációja szerepel, továbbá a users modul a felhasználók kezelése érdekében. A keretrendszer magától létrehoz már konfigurációs fájlokat amelyek szerkesztésével fel lehet építeni az alkalmazást. A frontend oldali fejlesztés alapkoncepció az, hogy HTML sablonokat definiálunk, amelyeket alkalmazás URL-jén belüli elérési utakhoz kötünk, emellett pedig statikus JavaScript és CSS fájlok egészítik ki az alkalmazás működését. Ezeket dinamikus adatokkal lehet tölteni, python file-okban szintén a Django eszközeivel lehet adatbázistáblákat (modelleket), logikát definiálni. 

Funkcionalitás és Jogosultságkezelés
Az alkalmazás nem csak statikus tartalmat jelenít meg, hanem interaktív funkciókkal is rendelkezik:

Publikus nézetek: A főoldal (Home), a Rólunk (About) oldal és a Galéria lista nézete bejelentkezés nélkül is elérhető.

Részletes nézet: A listából egy képre kattintva a dinamikus URL routing (<slug:slug>) segítségével betöltődik az adott kép részletes oldala.

Védett funkciók: Új kép feltöltése csak hitelesített (bejelentkezett) felhasználók számára engedélyezett. Ezt a @login_required dekorátorral biztosítottam a backend oldalon.

Navigáció: A layout.html sablonban a navigációs sáv dinamikusan változik attól függően, hogy a felhasználó be van-e jelentkezve (pl. a "Login" gomb helyett "Logout" és "New Photo" jelenik meg).

Médiafájlok és Statikus tartalmak
A Django külön kezeli a fejlesztés során használt statikus fájlokat (CSS, JS) és a felhasználók által feltöltött médiafájlokat.

Static: A stíluslapok (style.css) és scriptek (main.js) a static mappában kaptak helyet.

Media: A settings.py-ban konfigurált MEDIA_URL és MEDIA_ROOT beállítások teszik lehetővé, hogy a feltöltött képek a szerver fájlrendszerébe kerüljenek, és URL-en keresztül elérhetőek legyenek a böngésző számára
