<!---------------------------------------[Description]-->
## Description
    Create metatrader as a server for run command

<!---------------------------------------[Source]-->
<br><br>

## Source

#### Mac
    cd /Volumes/Data/develop/metatrader

#### Linux
    cd /home/morteza/Documents/

#### Windows
    cd Downloads

#### Download
    git clone https://github.com/dingmaotu/mql-zmq.git
    git clone https://github.com/dingmaotu/mql4-lib.git
    git clone https://github.com/darwinex/dwx-zeromq-connector.git


<!---------------------------------------[Copy]-->
<br><br>

## Copy files

#### Mac
    cp -fr /Volumes/Data/develop/metatrader/mql-zmq/Include/* /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Include/
    cp -fr /Volumes/Data/develop/metatrader/mql-zmq/Library/MT4/* /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Libraries/
    cp -fr /Volumes/Data/develop/metatrader/mql4-lib/* /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Include/Mql/
    cp -fr /Volumes/Data/develop/metatrader/dwx-zeromq-connector/v2.0.1/mql4/DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Experts/
    cp -fr /Volumes/Data/develop/metatrader/dwx-zeromq-connector/v2.0.1/python/api/DWX_ZeroMQ_Connector_v2_0_1_RC8.py /Volumes/data/projects/example_metatrader

#### Linux
    cp -fr /home/morteza/Documents/mql-zmq/Include/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/
    cp -fr /home/morteza/Documents/mql-zmq/Library/MT4/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/
    cp -fr /home/morteza/Documents/mql4-lib/* /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/
    cp -fr /home/morteza/Documents/dwx-zeromq-connector/v2.0.1/mql4/DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/
    cp -fr /home/morteza/Documents/dwx-zeromq-connector/v2.0.1/python/api/DWX_ZeroMQ_Connector_v2_0_1_RC8.py /home/morteza/Documents/forex_metatrader

#### Windows
    Copy    Downloads/mql-zmq/Include/*                                                   To    MQL4/Include/
    Copy    Downloads/mql-zmq/Library/MT4/*                                               To    MQL4/Libraries/
    Copy    Downloads/mql4-lib/*                                                          To    MQL4/Include/Mql/
    Copy    Downloads/dwx-zeromq-connector/v2.0.1/mql4/DWX_ZeroMQ_Server_v2.0.1_RC8.mq4   To    MQL4/Experts/

<!---------------------------------------[Permission]-->
<br><br>

## Permission

#### MAC
    chmod 777 /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Include/*
    chmod 777 /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Libraries/*
    chmod 777 /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Include/Mql/*
    chmod 777 /Users/morteza/.wine/drive_c/users/morteza/AppData/Roaming/MetaQuotes/Terminal/4436C789DD6783682A87A8056812DF7E/MQL4/Experts/*
    chmod 777 /Volumes/data/projects/example_metatrader/*

#### Linux
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Libraries/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Include/Mql/*
    chmod 777 /home/morteza/.wine//drive_c/Program\ Files\ \(x86\)/FXCM\ MetaTrader\ 4/MQL4/Experts/*
    chmod 777 /home/morteza/Documents/forex_metatrader/*



<!---------------------------------------[Copy]-->
<br><br>

## Edit DWX_ZeroMQ_Server_v2.0.1_RC8.mq4 On metatrader

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

<!---------------------------------------[Arm libzmq]-->
## Arm libzmq

#### Requirement
    https://download.microsoft.com/download/2/e/6/2e61cfa4-993b-4dd4-91da-3737cd5cd6e3/vcredist_x64.exe
    https://download.microsoft.com/download/2/e/6/2e61cfa4-993b-4dd4-91da-3737cd5cd6e3/vcredist_x86.exe

#### Install visual studio 2022 
    https://visualstudio.microsoft.com/downloads/
        install Desktop development with C++ 
        install MSVC v143 - VS 2022 C++ ARM64 build tools

#### Install cmake
    https://cmake.org/download/

#### Compile libzmq 
    git clone https://github.com/zeromq/libzmq.git
    cd libzmq
    mkdir build-arm64
    cd build-arm64
    cmake .. -G "Visual Studio 17 2022" -A ARM64 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
    cmake --build . --config Release