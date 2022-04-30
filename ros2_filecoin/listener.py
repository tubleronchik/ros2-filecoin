import robonomicsinterface as ri
import rclpy
from rclpy.node import Node

class DatalogListener(Node):
    def __init__(self) -> None:
        super().__init__("datalog_listener")
        self.interface = ri.RobonomicsInterface()
        self.subscriber = ri.Subscriber(self.interface, ri.SubEvent.NewRecord, self.datalog_callback)

    def datalog_callback(self, data: str) -> None:
        print(data)

def main(args=None) -> None:
    rclpy.init(args=args)
    datalog_listener = DatalogListener()
    rclpy.spin(DatalogListener)

