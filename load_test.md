**Teljesítménypróba dokumentáció**  

***Előkészületek***
Ahhoz, hogy megfelelő eredményeket kapjunk a teljesítménypróbán, el kell érni azt, hogy ne csak manuálisan, hanem automatikusan is skálázódjon az OpenShiftben a podok száma. Ehhez a telepítés konfigurációjában meg kell határozni egy CPU limitet, különben hagyja a környezet, hogy egyetlen pod használja fel az összes rendelkezésre álló erőforrást. Az egyszerűség kedvéért a továbbiakban minden beállítás módosítást az OpenShift termináljában kiadott parancsokkal fogok elvégezni.
A használt parancsok:
- oc set resources deployment/photo-gallery --limits=cpu=200m,memory=512Mi --requests=cpu=100m,memory=256Mi
- oc autoscale deployment/photo-gallery --min=1 --max=5 --cpu-percent=50
