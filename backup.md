<!---------------------------------------[Metatrader]-->
## Metatrader 




















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
   