import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DuvardanKac(Node):
    def __init__(self):
        super().__init__('duvardan_kac')

        self.declare_parameter('speed', 2.0)
        self.declare_parameter('lower_limit', 1.0)
        self.declare_parameter('upper_limit', 10.0)

        self.x = 5.5
        self.y = 5.5

        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.create_subscription(Pose, '/turtle1/pose', self.pose_cb, 10)

        self.create_timer(0.1, self.move)
        self.create_timer(1.0, self.log)

    def pose_cb(self, msg):
        self.x = msg.x
        self.y = msg.y

    def move(self):
        speed = self.get_parameter('speed').value
        lower_limit = self.get_parameter('lower_limit').value
        upper_limit = self.get_parameter('upper_limit').value

        msg = Twist()
        msg.linear.x = speed

        if self.x < lower_limit or self.x > upper_limit or self.y < lower_limit or self.y > upper_limit:
            msg.angular.z = 3.0
        else:
            msg.angular.z = 0.0

        self.pub.publish(msg)

    def log(self):
        self.get_logger().info(f'x: {self.x:.2f}  y: {self.y:.2f}')


def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(DuvardanKac())
    rclpy.shutdown()


if __name__ == '__main__':
    main()



    
