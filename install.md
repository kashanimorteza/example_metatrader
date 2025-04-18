<!---------------------------------------[Metatrader]-->
## Metatrader 

##### Mac 
    brew install --cask --no-quarantine wine-stable
    brew install --cask gstreamer-development
    brew install winetricks
    winetricks vcrun6 vcrun2010 msxml3
	wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
	wine fxcm4setup.exe

##### Linux
    dpkg --add-architecture i386
    dpkg --print-foreign-architectures
    sudo apt update
    
    sudo apt install wget gnupg2 software-properties-common
    wget -nc https://dl.winehq.org/wine-builds/winehq.key
    sudo gpg --dearmor < winehq.key > /etc/apt/trusted.gpg.d/winehq.gpg
    sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ jammy main'
    sudo apt update

    sudo apt install --install-recommends winehq-stable


    apt install wine
    apt update
    apt install wine32
    wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
    wine fxcm4setup.exe

<!---------------------------------------[User]-->
## User
    useradd -m -p $(openssl passwd -1 "123456") "morteza"
    echo "morteza ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

<!---------------------------------------[GUI]-->
## Gui
    apt install xfce4 xfce4-goodies -y

    apt install xorg dbus-x11 x11-xserver-utils 
    apt install xfce4 xfce4-goodies 
    apt install ubuntu-desktop 
    apt install task-gnome-desktop

    systemctl set-default graphical.target

<!---------------------------------------[XRDP]-->
## XRDP

#### Install From Source
    sudo apt install -y git make gcc autoconf libtool pkg-config libpam0g-dev libssl-dev libx11-dev libxfixes-dev libjpeg-dev libxrandr-dev libxrender-dev libxv-dev xserver-xorg-dev x11proto-dev libxinerama-dev libx264-dev libopus-dev nasm automake libfuse3-dev

    cd /usr/local/src
    sudo git clone https://github.com/neutrinolabs/xrdp.git
    cd xrdp
    sudo git checkout v0.10.3

    ./bootstrap
    ./configure --enable-fuse --enable-jpeg --enable-opus
    make
    make install

#### APT
    sudo apt install xfce4 xfce4-goodies -y
    sudo apt install xrdp -y

#### Monitor
    sudo xrdp -v
    /usr/local/sbin/xrdp -v

    sudo systemctl enable xrdp
    sudo systemctl restart xrdp
    sudo journalctl -f -u xrdp 

    sudo -u xrdp cat /etc/xrdp/key.pem
    vim /lib/systemd/system/xrdp.service

    sudo mkdir -p /var/lib/xrdp
    sudo cp /etc/xrdp/*.pem /var/lib/xrdp/
    sudo chown xrdp:xrdp /var/lib/xrdp/*.pem
    sudo chmod 600 /var/lib/xrdp/key.pem
    sudo chmod 644 /var/lib/xrdp/cert.pem

    certificate=/var/lib/xrdp/cert.pem
    key_file=/var/lib/xrdp/key.pem













    sudo chown xrdp:xrdp /etc/xrdp/cert.pem /etc/xrdp/key.pem
    sudo chmod 644 /etc/xrdp/cert.pem
    sudo chmod 640 /etc/xrdp/key.pem

    sudo systemctl enable xrdp

    sudo systemctl restart xrdp
    sudo journalctl -f -u xrdp 



    /lib/systemd/system/xrdp.service
    -------------------------------------------
    [Unit]
    Description=xrdp daemon
    Documentation=man:xrdp(8) man:xrdp.ini(5)
    Requires=xrdp-sesman.service
    After=network.target xrdp-sesman.service

    [Service]
    Type=forking
    PIDFile=/run/xrdp/xrdp.pid
    RuntimeDirectory=xrdp
    EnvironmentFile=-/etc/sysconfig/xrdp
    EnvironmentFile=-/etc/default/xrdp
    User=xrdp
    Group=xrdp
    PermissionsStartOnly=true
    ExecStartPre=/bin/sh /usr/share/xrdp/socksetup
    ExecStart=/usr/sbin/xrdp $XRDP_OPTIONS
    ExecStop=/usr/sbin/xrdp $XRDP_OPTIONS --kill

    [Install]
    WantedBy=multi-user.target







    sudo chown xrdp:xrdp /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/ssl/private/ssl-cert-snakeoil.key
    sudo chmod 644 /etc/ssl/certs/ssl-cert-snakeoil.pem
    sudo chmod 640 /etc/ssl/private/ssl-cert-snakeoil.key


    sudo systemctl enable xrdp xrdp-sesman
    sudo systemctl restart xrdp xrdp-sesman
    sudo journalctl -f -u xrdp -u xrdp-sesman -f



echo "startxfce4" > ~/.xsession


sudo -u xrdp cat /etc/xrdp/key.pem



    apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils xrdp -y
    useradd -m -p $(openssl passwd -1 "L9gT7ffvJYM5gz") "morteza"
    apt install --reinstall xrdp
    systemctl restart xrdp-sesman
    systemctl status xrdp-sesman
   