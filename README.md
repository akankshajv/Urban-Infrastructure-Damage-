# Urban-Infrastructure-Damage-
SDG Goal: SDG 11 Sustainable Cities and Communities. Classify building structural health as intact or at risk following natural disasters using aerial survey data. Evaluate the system using multi class logarithmic loss. Fine tune the classification weights to heavily penalize missing the at risk minority class.

# Model Training

Training done by: 
* Asif Kamal
* Amar Biradar
* Suhana D
  
## Training the Model

The model uses Transfer Learning with the pretrained Xception architecture.
### Base Model

Pretrained on ImageNet
Top classification layers removed
<code>include_top = False
weights = imagenet
input_shape = (224,224,3)</code>

Freezing Base Layers
All pretrained layers are frozen to retain learned features.

## Model Compilation

Optimizer: Adam
Loss Function: Binary Crossentropy
Metric: Accuracy
Example:
<code>model.compile(
optimizer=Adam(learning_rate=0.0001),
loss='binary_crossentropy',
metrics=['accuracy']
)</code>

## Model Training Process

The model is trained using:
* Training dataset
* Validation dataset

Training parameters:
* Epochs: 30
* Batch Size: 32

Callbacks used:
* ModelCheckpoint – saves the best performing model
* EarlyStopping – stops training if validation performance stops improving

## Model Output

The trained model classifies images into:
Damaged Infrastructure
Non-Damaged Infrastructure

Saved model files:
hurricane_damage_model.keras
