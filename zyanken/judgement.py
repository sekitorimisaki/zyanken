import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    b = random.randrange(3)
    if b == 0:
        print("私:グー")
    elif b == 1:
        print("私: パー")
    elif b == 2:
        print("私: チョキ")
    if msg.data == 0:
        print("player: グー")
    elif msg.data == 1:
        print("player: チョキ")
    elif msg.data == 2:
        print("player: パー")
    if msg.data == b:
        print("引き分け")
    elif msg.data == 2 and b == 0:
        print("player の 勝ち！")
    elif msg.data == 0 and b == 2:
        print("私の勝ち！")
    elif msg.data == b-1:
        print("私の勝ち!")
    elif msg.data == b+1:
        print("player の 勝ち！")
    node.get_logger().info("player: %d" % msg.data)

rclpy.init()
node = Node("judgement")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
