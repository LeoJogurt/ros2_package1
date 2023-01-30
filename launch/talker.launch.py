from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description([
    Node(
        package='demo_nodes_cpp',
        executable='listener'
    )
])