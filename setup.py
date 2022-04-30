from setuptools import setup

package_name = 'ros2_filecoin'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tubleronchik',
    maintainer_email='tubleronchik@todo.todo',
    description='Simple ROS2 package to publisjh Robonomics datalgo data to Filecoin.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'datalog_listener = ros2_filecoin.listener:main',
        ],
    },
)
