#!/usr/bin/env python

import sys

from setuptools import setup

assert sys.version_info.major == 3 and sys.version_info.minor >= 6

setup(
    name='la_mbda',
    packages=['la_mbda', 'experiments'],
    install_requires=[
        'dm_control==0.0.355168290',
        'tensorflow==2.4.0',
        'tensorflow-probability==0.12.0',
        'tensorflow-addons==0.12.1',
        'tensorboardx==2.1',
        'matplotlib==3.3.4',
        'tf_agents==0.6.0',
        'absl-py==0.12.0',
        'astunparse==1.6.3',
        'cachetools==4.2.1',
        'certifi==2020.12.5',
        'cffi==1.14.5',
        'chardet==4.0.0',
        'cycler==0.10.0',
        'Cython==0.29.22',
        'decorator==4.4.2',
        'dm-env==1.4',
        'dm-tree==0.1.5',
        'fasteners==0.16',
        'flatbuffers==1.12',
        'future==0.18.2',
        'gast==0.3.3',
        'gin-config==0.4.0',
        'glfw==2.1.0',
        'google-auth==1.27.1',
        'google-auth-oauthlib==0.4.3',
        'google-pasta==0.2.0',
        'grpcio==1.32.0',
        'gym==0.18.0',
        'h5py==2.10.0',
        'idna==2.10',
        'imageio-ffmpeg==0.4.3',
        'importlib-metadata==3.7.2',
        'joblib==0.14.1',
        'Keras-Preprocessing==1.1.2',
        'kiwisolver==1.3.1',
        'labmaze==1.0.3',
        'lxml==4.6.2',
        'Markdown==3.3.4',
        'matplotlib==3.3.4',
        'moviepy==1.0.3',
        'mujoco-py==2.0.2.7',
        'numpy==1.19.2',
        'oauthlib==3.1.0',
        'opt-einsum==3.3.0',
        'Pillow==7.2.0',
        'proglog==0.1.9',
        'protobuf==3.15.5',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycparser==2.20',
        'pyglet==1.5.0',
        'PyOpenGL==3.1.5',
        'pyparsing==2.4.7',
        'python-dateutil==2.8.1',
        'requests==2.25.1',
        'requests-oauthlib==1.3.0',
        'rsa==4.7.2',
        'scipy==1.5.4',
        'six==1.15.0',
        'tensorboard==2.4.1',
        'tensorboard-plugin-wit==1.8.0',
        'tensorflow-estimator==2.4.0',
        'termcolor==1.1.0',
        'tf-agents==0.6.0',
        'tqdm==4.59.0',
        'typeguard==2.11.1',
        'typing-extensions==3.7.4.3',
        'urllib3==1.26.3',
        'Werkzeug==1.0.1',
        'wrapt==1.12.1',
        'xmltodict==0.12.0',
        'zipp==3.4.1',
        'safety_gym @ https://github.com/yardenas/safety-gym/tarball/dm_hack'
    ]
)
