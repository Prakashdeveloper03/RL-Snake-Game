import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot(scores, mean_scores):
    """
    Plot the scores and mean scores during training.

    Args:
        scores (list): List of scores for each game.
        mean_scores (list): List of mean scores over a certain period.

    Returns:
        None
    """
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title("Training...")
    plt.xlabel("Number of Games")
    plt.ylabel("Score")
    plt.plot(scores)  # Plot individual scores
    plt.plot(mean_scores)  # Plot mean scores
    plt.ylim(ymin=0)  # Set the minimum value of the y-axis to 0
    plt.text(
        len(scores) - 1, scores[-1], str(scores[-1])
    )  # Display the last score value
    plt.text(
        len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1])
    )  # Display the last mean score value
    plt.show(block=False)
    plt.pause(0.1)
