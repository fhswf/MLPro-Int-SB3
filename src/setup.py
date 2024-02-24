from setuptools import setup


setup(name='mlpro-int-sb3',
version='0.1.0',
description='MLPro: Integration StableBaselines3',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_sb3'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=1.3.1",
        "mlpro_int_gymnasium[full]>=0.1.0",
        "stable_baselines3>=2.1.0"
        "gymnasium>=0.29"
    ],
},

zip_safe=False)