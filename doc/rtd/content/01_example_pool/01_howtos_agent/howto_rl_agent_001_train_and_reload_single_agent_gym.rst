.. _Howto Agent RL 001:
Howto RL-AGENT-001: Train and Reload Single Agent (Gymnasium)
=============================================================


**Prerequisites**

Please install Gymnasium and the related integration package as follows:

.. code-block:: bash

    pip install mlpro-int-gymnasium[full] --upgrade


**Executable code**

.. literalinclude:: ../../../../../test/howtos/agent/howto_rl_agent_001_train_and_reload_single_agent_gym.py
	:language: python



**Results**

The Gymnasium Cartpole environment window appears. Afterwards, the training runs 
for a few episodes before terminating and printing the result. 

After termination the local result folders contain the training result files:
    - agent_actions.csv
    - env_rewards.csv
    - env_states.csv
    - evaluation.csv
    - summary.csv
    - trained model.pkl

Both training results are from the same agent.


**Cross Reference**

    - :ref:`API Reference <api_basics>`