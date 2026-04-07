# Machine Learning for Robotics: MLP Backpropagation, Transfer Learning, CNNs, and Reinforcement Learning

## Overview
This project explored four core areas of machine learning in a robotics context:

- **backpropagation in multilayer perceptrons (MLPs)** for regression
- **backpropagation in MLPs** for classification
- **transfer learning with convolutional neural networks (CNNs)** for image classification
- **tabular Q-learning** for path planning in a grid-world environment

The work combined mathematical derivation, from-scratch implementation, model comparison, hyperparameter exploration, and reinforcement learning. The overall aim was not only to use machine learning tools, but to understand how these methods work at algorithmic level and how they can be applied to robotics-related decision making and perception tasks. :contentReference[oaicite:5]{index=5}

## Project Context
This project was completed for **ELEC0144 – Machine Learning for Robotics**. The assignment required three major strands of work:

- implementing **MLPs from scratch** to demonstrate understanding of backpropagation and optimisation
- applying **transfer learning** using pre-trained CNNs to classify new image classes
- writing a full **tabular Q-learning** implementation to learn an optimal path with maximum reward in a constrained environment. :contentReference[oaicite:6]{index=6}

The assignment was structured into four tasks:
1. regression with a **1-3-1 MLP**
2. classification with a **4-5-3-3 MLP**
3. transfer learning with **AlexNet** and **GoogLeNet**
4. path planning using **Q-learning**. :contentReference[oaicite:7]{index=7}

## My Contribution
This was a team coursework project, and my contribution focused on understanding and implementing the core learning algorithms, interpreting model behaviour, and helping connect theoretical derivations to practical results across the different tasks.

The project as a whole demonstrates my ability to work with:
- **from-scratch neural network implementation**
- **training algorithm comparison**
- **deep learning model adaptation**
- **hyperparameter tuning**
- **classification analysis**
- **reinforcement learning for decision making**
- and **technical reporting of machine learning results**.

## Task 1: Regression with a 1-3-1 MLP

### Objective
The first task required the derivation and implementation of backpropagation for a **1-3-1 neural network** with:
- 1 input node
- 3 hidden nodes with **tanh** activation
- 1 linear output node

The network was trained on noisy regression data and tested on unseen data. :contentReference[oaicite:8]{index=8}

### Technical Work
The report derives both:
- **forward propagation**
- and **backpropagation using stochastic gradient descent (SGD)**

for the network, beginning with one node and then generalising to the full layer structure. It then uses this derivation to implement a custom regression network from scratch. :contentReference[oaicite:9]{index=9}

The report also compares this SGD implementation with **ADAM**, and further explores how changing:
- the number of hidden layers or nodes
- and the choice of activation functions, including **ReLU**

affects performance. :contentReference[oaicite:10]{index=10}

### Key Results
According to the report:
- the custom SGD model produced a regression curve close to the expected target curve
- **ADAM converged substantially faster** than SGD
- and architecture/activation choices influenced both convergence and fit quality. :contentReference[oaicite:11]{index=11}

The report notes that ADAM stabilised after roughly **5,000 epochs**, while SGD required roughly **22,000 epochs**, showing the benefit of adaptive learning rates and momentum-like behaviour in optimisation. :contentReference[oaicite:12]{index=12}

## Task 2: Classification with a 4-5-3-3 MLP

### Objective
The second task required deriving and implementing backpropagation for a **4-5-3-3 network** to classify the **Iris dataset**, using:
- 4 input features
- 5 nodes in the first hidden layer with **tanh**
- 3 nodes in the second hidden layer with **tanh**
- 3 output nodes for class prediction. :contentReference[oaicite:13]{index=13}

The data had to be preprocessed by:
- converting the iris labels to numeric form
- randomising sample order
- and splitting the data into **70% training** and **30% validation**. :contentReference[oaicite:14]{index=14}

### Technical Work
This part of the project included:
- derivation of the classification backpropagation equations
- a custom implementation of the network from scratch
- comparison between **vanilla SGD**, **SGD with momentum**, and **ADAM**
- and architecture exploration using TensorFlow/Keras. :contentReference[oaicite:15]{index=15}

The zip contents show a structured codebase for this task, including:
- `nn.py`
- `sgd.py`
- `sgd_momentum.py`
- `adam.py`
- `pre_processing.py`
- and plotting scripts, which indicates a relatively modular implementation rather than a single monolithic notebook. :contentReference[oaicite:16]{index=16}

### Key Results
The report shows that the classification experiments compared different architectures and activations, including wider, deeper, and ReLU-based variants. It reports that:
- the **smaller 4-3-3 network** performed surprisingly well
- deeper models did not necessarily improve generalisation on Iris
- and **ReLU underperformed** compared with tanh in this small dataset setting, likely because of instability and inactive neurons. :contentReference[oaicite:17]{index=17}

This is a valuable result because it shows that stronger performance does not automatically come from adding complexity; architecture must match dataset size and structure.

## Task 3: Transfer Learning with CNNs

### Objective
The third task required transfer learning on a custom fruit image dataset with **5 classes**:
- durian
- papaya
- kiwi
- mangosteen
- mango

with **15 images per class**, giving **75 total images**, resized to **227 × 227 × 3**. :contentReference[oaicite:18]{index=18}

The assignment required using:
- **AlexNet**
- and **GoogLeNet**

with a **70% / 30%** training-validation split, and discussing how different learning parameters affected the outcome. :contentReference[oaicite:19]{index=19}

### Technical Work
The report explains that both pre-trained networks were adapted by:
- keeping the original convolutional feature extraction layers
- replacing the final classification layer to output **5 classes**
- and fine-tuning the models on the fruit dataset. :contentReference[oaicite:20]{index=20}

The repository contents support this clearly:
- `task_3_b.ipynb`
- `task_3_c.ipynb`
- `task_3_d_alexnet.ipynb`
- `task_3_d_googlenet.ipynb`
- tuning result CSV files
- and graph-generation scripts. :contentReference[oaicite:21]{index=21}

### Key Results
The report shows that **GoogLeNet outperformed AlexNet** on this fruit classification task:
- **AlexNet** reached a stable validation accuracy of **73.91%**
- **GoogLeNet** achieved a peak validation accuracy of **91.30%** and finished at **86.96%**. :contentReference[oaicite:22]{index=22}

The report attributes this to GoogLeNet’s more advanced architecture and stronger feature extraction ability. It also notes that GoogLeNet handled visually similar fruit classes more effectively, while AlexNet showed more confusion between visually similar pairs such as mango and papaya. :contentReference[oaicite:23]{index=23}

The hyperparameter analysis also showed:
- AlexNet was more sensitive to optimiser and learning rate choice
- GoogLeNet was more robust across parameter combinations
- and Adam gave smoother, more stable learning curves, while SGD often showed faster initial gains but more variance. :contentReference[oaicite:24]{index=24}

## Task 4: Reinforcement Learning with Tabular Q-Learning

### Objective
The final task required implementing **tabular Q-learning** in a grid-world environment, where the agent had to learn the best action for each state in order to maximise cumulative reward. The environment included:
- a **+10 terminal reward** at cell 12
- a **−10 terminal penalty** at cell 8
- an **obstacle** at cell 6
- and a **living reward of −1 per step**. :contentReference[oaicite:25]{index=25}

The agent could take four actions:
- up
- right
- down
- left

and was not allowed to leave the grid or enter the obstacle. :contentReference[oaicite:26]{index=26}

### Technical Work
The report presents the Q-learning setup using:
- a Markov Decision Process framework
- iterative Bellman-style Q-updates
- a learning rate
- a discount factor
- and an **epsilon-greedy** exploration strategy with decay. :contentReference[oaicite:27]{index=27}

It also explains and works through the **first three iterations** of the first episodes in detail, showing how rewards, invalid moves, and future action values influence the Q-table updates. :contentReference[oaicite:28]{index=28}

### Key Results
This task demonstrates the reinforcement learning side of the project:
- the agent begins with no useful knowledge
- updates Q-values through repeated interaction
- and gradually learns the best action for each state.

This is especially valuable from a robotics perspective because it links machine learning to **decision making and path planning**, not just function approximation or image classification. :contentReference[oaicite:29]{index=29}

## Engineering and Technical Skills Demonstrated
This project demonstrates skills in:
- **backpropagation derivation**
- **from-scratch neural network implementation**
- **SGD, momentum, and ADAM optimisation**
- **MLP regression and classification**
- **dataset preprocessing and train/validation splitting**
- **architecture comparison and hyperparameter tuning**
- **transfer learning with pre-trained CNNs**
- **classification analysis using confusion matrices and validation metrics**
- **reinforcement learning with Q-learning**
- **technical communication of ML experiments and results**

## Why This Project Matters
What makes this project strong is its breadth. It does not just show that I used machine learning libraries — it shows that I worked across several levels of abstraction:

- deriving learning rules mathematically
- implementing models from scratch
- comparing optimisers and architectures
- adapting deep networks to a new image dataset
- and applying reinforcement learning to a decision-making problem

That combination reflects both theoretical understanding and practical implementation skill.

## Repository Contents
- `README.md` – project summary
- `report/` – final coursework report
- `task_1/` – regression with 1-3-1 MLP
- `task_2/` – classification with 4-5-3-3 MLP
- `task_3/` – transfer learning with AlexNet and GoogLeNet
- `task_4/` – tabular Q-learning implementation
