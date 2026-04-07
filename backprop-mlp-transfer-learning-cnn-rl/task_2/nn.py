from nn import NeuralNet
import numpy as np


def sgd_momentum(
    nn: NeuralNet,
    training_data: list,
    testing_data: list,
    epochs: int,
    learning_rate: float,
    batch_size: int,
    rho: int,
):
    """Train network using stocahstic gradient descent + momentum

    v(t + 1) = rho * t + nabla
    w(t + 1) = w(t) - lr * v(t + 1)

    Arguments:
        nn -- neural network instance
        training_data -- List of tuples (x, y) for input x and target y
        tresting_data -- List of tuples (x, y) for input x and target y
        epochs -- Number of complete passes through training data
        learning_rate -- Step size for gradient descent
        batch_size -- Number of samples per gradient update
        rho -- value between 0 and 1,  how much of the previous velocity is retained
    """
    n = len(training_data)

    train_loss, test_loss = [], []
    train_accuracy, test_accuracy = [], []

    # Momentum v(0)
    v_w, v_b = [np.zeros(w.shape) for w in nn.weights], [
        np.zeros(b.shape) for b in nn.biases
    ]

    for epoch in range(epochs):

        ep_train_loss, ep_train_preds = 0.0, []
        ep_test_loss, ep_test_preds = 0.0, []
        ep_train_true, ep_test_true = [], []

        # TRAIN
        batches = [
            training_data[k : k + batch_size] for k in range(0, n, batch_size)
        ]  # split into batches

        for batch in batches:
            # Initialize gradient accumulator for each layer, shape (weights[l].shape)
            nabla_w = [np.zeros(w.shape) for w in nn.weights]
            nabla_b = [np.zeros(b.shape) for b in nn.biases]

            # accumulate gradients over batch
            for x, y in batch:

                y_one_hot = np.zeros((3, 1))  # Shape: (num_classes, 1)
                y_one_hot[y] = 1  # Set 1 at the correct class index

                # Forward pass
                activations, zs = nn.forward(
                    x
                )  # activations[l] shape: (layer_size[l], 1)
                loss = nn.cross_entropy_loss(y_pred=activations[-1], y_true=y_one_hot)
                pred = np.argmax(activations[-1])

                delta_nabla_w, delta_nabla_b = nn.backwards(
                    activations=activations, zs=zs, y=y_one_hot
                )

                # running sum of gradients nabla for each layer, shape (weights[l].shape)
                nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
                nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]

                # add loss and preds for tracking
                ep_train_loss += loss
                ep_train_preds.append(pred)
                ep_train_true.append(y)

            # Momentum
            v_w = [rho * v + nw for v, nw in zip(v_w, nabla_w)]
            v_b = [rho * v + nb for v, nb in zip(v_b, nabla_b)]

            # Update weights and biases for each layer using average gradient over batch
            nn.weights = [
                w - (learning_rate / len(batch)) * v
                for w, v in zip(nn.weights, v_w)  # over each layer
            ]
            nn.biases = [
                b - (learning_rate / len(batch)) * v
                for b, v in zip(nn.biases, v_b)  # over each layer
            ]

        # EVALUTAION
        for x, y in testing_data:
            # One hot encode
            y_one_hot = np.zeros((3, 1))
            y_one_hot[y] = 1

            # Forward pass only
            activations, _ = nn.forward(x)
            loss = nn.cross_entropy_loss(y_pred=activations[-1], y_true=y_one_hot)
            pred = np.argmax(activations[-1])

            ep_test_loss += loss
            ep_test_preds.append(pred)
            ep_test_true.append(y)

        # Epoch metrics
        train_loss.append(ep_train_loss / len(training_data))
        test_loss.append(ep_test_loss / len(testing_data))

        train_acc = np.mean(np.array(ep_train_preds) == np.array(ep_train_true))
        test_acc = np.mean(np.array(ep_test_preds) == np.array(ep_test_true))

        train_accuracy.append(train_acc)
        test_accuracy.append(test_acc)

    return train_loss, test_loss, train_accuracy, test_accuracy
