#!/usr/bin/python3

import os
from setuptools import setup
from setuptools.command.install import install

import pose


class PoseInstall(install):
    """Create folder to store experiments and images.

    PoseInstall wraps the standard install to create a custom 
    directory on installation to store results.
    """

    def run(self):
        self._create_application_data_folder()
        install.run(self)

    def _create_application_data_folder(self):
        path = os.path.join(os.getenv("HOME"), "Pose")

        if not os.path.exists(path):
            os.mkdir(path)

            output = f"EXPERIMENTS AND IMAGES WILL BE LOCATED IN: {path}\n"
            print(output)


setup(
    name='pose',
    version=pose.__version__,
    description='Automated image capturing via command line',
    license='MIT',
    packages=['pose'],
    entry_points={
        'console_scripts': ['pose=pose.__main__:main']
    },
    cmdclass={'install': PoseInstall},
)
