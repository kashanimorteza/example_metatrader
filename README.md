<!---------------------------------------[Description]-->
## Description
    Create metatrader as a server for run command





<!---------------------------------------[Github]-->
<br><br>

## Source
    Github : mql-zmq  : https://github.com/dingmaotu/mql-zmq.git
    Github : mql4-lib : https://github.com/dingmaotu/mql4-lib.git
    Github : darwinex : https://github.com/darwinex/dwx-zeromq-connector.git





<!---------------------------------------[Install]-->
<br><br>

## Install 

##### Metatrader 
MAC

    brew install --cask --no-quarantine wine-stable
    brew install --cask gstreamer-development
    brew install winetricks
    winetricks vcrun6 vcrun2010 msxml3
	wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
	wine fxcm4setup.exe

Linux

    apt install wine
    dpkg --add-architecture i386
    apt update
    apt install wine32
    wget https://download.mql5.com/cdn/web/stratos.trading.pty/mt4/fxcm4setup.exe
    wine fxcm4setup.exe

#### Source
    git clone git@github.com:kashanimorteza/example_metatrader.git
    cd ./example_metatrader

#### Python
    add-apt-repository ppa:deadsnakes/ppa
	apt update -y
	apt install python3 -y
	apt install python3-pip -y
	apt install python3-venv -y

#### Python virtual environment 
	python3 -m venv .myenv3
	.myenv3/bin/python3 -m pip install --upgrade pip
	source .myenv3/bin/activate
	pip install -r requirements.txt





<!---------------------------------------[Server]-->
<br><br>

## Server
#### Download repository
    git clone https://github.com/dingmaotu/mql-zmq.git
    git clone https://github.com/dingmaotu/mql4-lib.git
    git clone https://github.com/darwinex/dwx-zeromq-connector.git

#### Copy files

    MAC
    -------------------
    cp -fr /Users/morteza/Documents/mql-zmq/Include/* /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/
    cp -fr /Users/morteza/Documents/mql-zmq/Library/MT4/* /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/
    cp -fr /Users/morteza/Documents/mql4-lib/* /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/
    cp -fr /Users/morteza/Documents/dwx-zeromq-connector/v2.0.1/mql4/DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/
    cp -fr /Users/morteza/Documents/dwx-zeromq-connector/v2.0.1/python/api/DWX_ZeroMQ_Connector_v2_0_1_RC8.py /Users/morteza/Documents/forex_metatrader

    Linux
    -------------------
    cp -fr /home/morteza/Documents/mql-zmq/Include/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/
    cp -fr /home/morteza/Documents/mql-zmq/Library/MT4/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/
    cp -fr /home/morteza/Documents/mql4-lib/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/
    cp -fr /home/morteza/Documents/dwx-zeromq-connector/v2.0.1/mql4/DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/
    cp -fr /home/morteza/Documents/dwx-zeromq-connector/v2.0.1/python/api/DWX_ZeroMQ_Connector_v2_0_1_RC8.py /home/morteza/Documents/forex_metatrader

#### Permission

    MAC
    -------------------
    chmod 777 /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/*
    chmod 777 /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/*
    chmod 777 /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/*
    chmod 777 /Users/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/*
    chmod 777 /Users/morteza/Documents/forex_metatrader/*

    Linux
    -------------------
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/*
    chmod 777 /home/morteza/Documents/forex_metatrader/*

#### Edit DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 On metatrader

    //+---------------------------Account---------------------------------------+
    void account(string model, string &zmq_ret)
    {   
        double res = 0;
        if (model == "Balance")
            res=AccountBalance();
        if (model == "Equity")
            res=AccountEquity();
        if (model == "FreeMargin") 
            res=AccountFreeMargin();
        if (model == "Number") 
            res=AccountNumber();
        if (model == "Profit") 
            res=AccountProfit();
        zmq_ret = zmq_ret + ", '_response': '"+ res +"'";
    }

    if(compArray[0] == "account")
        switch_action = 20;

    case 20:
        zmq_ret = "{'_action': 'account', '_model': '"+compArray[1]+"'";
        account(compArray[1], zmq_ret);
        zmq_ret = zmq_ret + "}";
        InformPullClient(pSocket, zmq_ret);
    break;



#### DWX_ZeroMQ_Connector_v2_0_1_RC8.py

    def account(self, model):
        try:
            subject = 'account'
            self._set_response_(None)                    
            _msg = f"{subject};{model}"
            self.remote_send(self._PUSH_SOCKET, _msg)                      
            while self._valid_response_('zmq') == False: sleep(0.1)
            response = self._get_response_()
            return response
        except KeyError:
            print("error")

#### client.py

    from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

    zmq = DWX_ZeroMQ_Connector()

    zmq.account(model="Balance")







<!---------------------------------------[Account]-->
<br><br>

## Account

#### FXCM
    51866921
    5osyyfc
    2susibr
