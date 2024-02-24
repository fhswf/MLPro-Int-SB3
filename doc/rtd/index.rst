.. MLPro Documentations documentation master file, created by
   sphinx-quickstart on Wed Sep 15 12:06:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MLPro-Int-SB3 - Integration of Stable-Baselines3 into MLPro 
==============================================================

Welcome to MLPro-Int-SB3, an extension to MLPro to integrate the Stable-Baselines3 package.
MLPro is a middleware framework for standardized machine learning in Python. It is 
developed by the South Westphalia University of Applied Sciences, Germany, and provides 
standards, templates, and processes for hybrid machine learning applications. Stable-Baselines3, in 
turn, provides a diverse suite of reliable implementations of reinforcement learning algorithms in PyTorch.

MLPro-Int-SB3 offers wrapper classes that allow the reuse of environments from Stable-Baselines3 in MLPro,
or the other way around.


**Preparation**
   Before running the examples, please install the latest versions of MLPro, Stable-Baselines3, and MLPro-Int-SB3 as follows:

   .. code-block:: bash

      pip install mlpro-int-sb3[full] --upgrade


**See also**
   - `MLPro - Machine Learning Professional <https://mlpro.readthedocs.io>`_ 
   - `MLPro-RL - Sub-framework for reinforcement learning <https://mlpro.readthedocs.io/en/latest/content/03_machine_learning/mlpro_rl/main.html>`_
   - `Stable-Baselines3 - Reliable Reinforcement Learning Implementations <https://stable-baselines3.readthedocs.io/en/master/>`_ 
   - `Further MLPro extensions <https://mlpro.readthedocs.io/en/latest/content/04_extensions/main.html>`_
   - `MLPro-Int-SB3 on GitHub <https://github.com/fhswf/MLPro-Int-SB3>`_


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Home

   self


.. toctree::
   :maxdepth: 2
   :caption: Example Pool
   :glob:

   content/01_example_pool/*


.. toctree::
   :maxdepth: 2
   :caption: API Reference
   :glob:

   content/02_api/*


.. toctree::
   :maxdepth: 2
   :caption: About
   :glob:

   content/03_about/*
