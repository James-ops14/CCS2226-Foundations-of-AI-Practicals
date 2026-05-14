"""
Task 1: MNIST Digit Classification

Objective:
- Download and load the MNIST handwritten digit dataset.
- Train a machine learning model to distinguish digits 0-9 using MNIST.
- Display accuracy and save sample prediction visualization.

Note:
The program downloads MNIST from OpenML when an internet connection is
available. If the download is unavailable, it falls back to sklearn's smaller
digits dataset so the practical can still run offline.
"""

import os
from pathlib import Path

os.environ.setdefault("LOKY_MAX_CPU_COUNT", "1")

import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml, load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay


TASK_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = TASK_DIR / "output"
DATA_DIR = TASK_DIR / "data"
OUTPUT_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)


def show_plots_if_interactive():
    # Show the graphs only when a display window is available.
    if "agg" not in plt.get_backend().lower():
        plt.show()
    plt.close("all")


def load_mnist_data():
    # First I try to download the real MNIST dataset.
    try:
        mnist = fetch_openml(
            "mnist_784",
            version=1,
            as_frame=False,
            data_home=DATA_DIR,
            parser="liac-arff"
        )
        return mnist.data, mnist.target.astype(int), "MNIST from OpenML", (28, 28)
    except Exception as error:
        # If download fails, this smaller dataset lets the code still run.
        print("Could not download/load MNIST from OpenML.")
        print(f"Reason: {error}")
        print("Using sklearn's smaller built-in digits dataset instead.\n")

        digits = load_digits()
        return digits.data, digits.target, "sklearn digits fallback", (8, 8)


def main():
    # Load the digit images and their correct labels.
    X, y, dataset_name, image_shape = load_mnist_data()

    # Use part of MNIST so the program does not take too long.
    if len(X) > 10000:
        X, _, y, _ = train_test_split(
            X,
            y,
            train_size=10000,
            random_state=42,
            stratify=y
        )

    # Split the dataset into training data and testing data.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    # Train the model using K-Nearest Neighbors.
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # Predict the answers for the test data.
    y_pred = model.predict(X_test)

    # Compare the predictions with the real answers.
    accuracy = accuracy_score(y_test, y_pred)

    print("=" * 60)
    print("MNIST DIGIT CLASSIFICATION")
    print("=" * 60)
    print(f"Dataset: {dataset_name}")
    print(f"Samples used: {len(X)}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save some example digits and predictions.
    plt.figure(figsize=(12, 6))

    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(X_test[i].reshape(image_shape), cmap="gray")
        plt.title(f"Actual: {y_test[i]}\nPredicted: {y_pred[i]}")
        plt.axis("off")

    plt.suptitle("Sample MNIST Digit Predictions", fontsize=14)
    plt.tight_layout()

    sample_path = OUTPUT_DIR / "mnist_sample_predictions.png"
    plt.savefig(sample_path, dpi=300)

    # Save a confusion matrix to show the mistakes clearly.
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.title("MNIST Confusion Matrix")

    matrix_path = OUTPUT_DIR / "mnist_confusion_matrix.png"
    plt.savefig(matrix_path, dpi=300)

    print("\nVisualizations saved:")
    print(f"- {sample_path}")
    print(f"- {matrix_path}")

    show_plots_if_interactive()


if __name__ == "__main__":
    main()
