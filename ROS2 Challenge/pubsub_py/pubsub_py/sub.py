import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Subscribe(Node):

    def __init__(self):
        super().__init__('Subscribe')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('Subscribing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    subscribe = Subscribe()
    rclpy.spin(subscribe)
    subscribe.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
