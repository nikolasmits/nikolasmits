import matplotlib.pyplot as plt
import numpy as np

# Results from AlexNet
alexnet_results = {
    'train_loss': [1.5558, 0.8578, 0.4369, 0.2010, 0.1340, 0.0409, 0.0218, 0.0167, 0.0149, 0.0050],
    'val_loss': [1.3137, 1.0378, 0.8573, 0.7670, 0.8139, 0.8875, 0.9446, 0.9552, 0.9367, 0.9047],
    'val_accuracy': [39.13, 52.17, 60.87, 73.91, 65.22, 65.22, 73.91, 73.91, 73.91, 73.91]
}

# Results from GoogLeNet
googlenet_results = {
    'train_loss': [1.6392, 1.4326, 1.1561, 0.8058, 0.5391, 0.3241, 0.2150, 0.1442, 0.0626, 0.0423],
    'val_loss': [1.5639, 1.4548, 1.2880, 1.1097, 0.9210, 0.7739, 0.6679, 0.5831, 0.5272, 0.4919],
    'val_accuracy': [39.13, 47.83, 56.52, 65.22, 82.61, 86.96, 91.30, 91.30, 86.96, 86.96]
}

# Create figure with two subplots
plt.figure(figsize=(15, 6))

# Plot 1: Training and Validation Loss
plt.subplot(1, 2, 1)
epochs = range(1, 11)

plt.plot(epochs, alexnet_results['train_loss'], 'r-', label='AlexNet Training Loss')
plt.plot(epochs, alexnet_results['val_loss'], 'r--', label='AlexNet Validation Loss')
plt.plot(epochs, googlenet_results['train_loss'], 'b-', label='GoogLeNet Training Loss')
plt.plot(epochs, googlenet_results['val_loss'], 'b--', label='GoogLeNet Validation Loss')

plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Validation Accuracy
plt.subplot(1, 2, 2)
plt.plot(epochs, alexnet_results['val_accuracy'], 'r-', label='AlexNet')
plt.plot(epochs, googlenet_results['val_accuracy'], 'b-', label='GoogLeNet')

plt.title('Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy (%)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('network_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
