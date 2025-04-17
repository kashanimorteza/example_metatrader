<!---------------------------------------[Install]-->
## Metatrader 

##### Mac 
    brew install --cask --no-quarantine wine-stable
    brew install --cask gstreamer-development
    brew install winetricks
    winetricks vcrun6 vcrun2010 msxml3
	wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
	wine fxcm4setup.exe

##### Linux

    apt install wine
    dpkg --add-architecture i386
    apt update
    apt install wine32
    wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
    wine fxcm4setup.exe