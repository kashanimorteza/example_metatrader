
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

zmq = DWX_ZeroMQ_Connector()

bc = zmq.account(model="Balance")

print(bc)