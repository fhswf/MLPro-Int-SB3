.. _Howto MB RL 001:
Howto RL-MB-001: Train and Reload Model Based Agent (Gym)
======================================================================


**Executable code**

.. literalinclude:: ../../../../../test/howtos/mb/howto_rl_mb_001_train_and_reload_model_based_agent_gym.py
	:language: python



**Results**

After the environment is initiated, the training will run for the specified amount of limits. The expected initial console output can be seen below.

.. code-block:: bash

    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": -- Training episode 0 started... 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent "": Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  S  Agent "": Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": -- Training run 0 started... 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": -- Training episode 0 started... 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  W  Training "RL": ------------------------------------------------------------------------------ 
    
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent "": Action computation started 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent "": Action computation finished 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  S  Agent "": Adaptation started 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent "": Action computation started
    ...
    
After termination the local result folder contains the training result files:
    - agent_actions.csv
    - env_rewards.csv
    - env_states.csv
    - evaluation.csv
    - summary.csv
    - trained model.pkl



**Cross Reference**

    - :ref:`API Reference <api_basics>`