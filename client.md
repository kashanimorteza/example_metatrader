<!---------------------------------------[Description]-->
## Description
    Client for send command to metatrader


<!---------------------------------------[Python]-->
<br><br>

## Python

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
	pip install pyzmq
    pip install pandas






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
    git clone https://github.com/darwinex/dwx-zeromq-connector.git

<!---------------------------------------[DWX_ZeroMQ_Connector_v2_0_1_RC8.py]-->
<br><br>

## DWX_ZeroMQ_Connector_v2_0_1_RC8.py

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



<!---------------------------------------[client]-->
<br><br>

## client.py

    from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

    zmq = DWX_ZeroMQ_Connector()

    bc = zmq.account(model="Balance")

    print(bc)















<!---------------------------------------[client]-->
## Arm libzmq

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


