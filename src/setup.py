from setuptools import setup


setup(name='mlpro-int-sb3',
version='1.0.2',
description='MLPro: Integration StableBaselines3',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_sb3'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro_int_gymnasium>=1.0.2",
        "mlpro_int_mujoco[full]>=1.0.1",
        "gymnasium!=1.0.0",
        "stable_baselines3>=2.3.0",
        "torch>=2.0.0,<=2.3.1",
        "numpy>=1.0.0,<=1.26.4",
        "setuptools >= 75.0.0"
    ],
},

zip_safe=False)