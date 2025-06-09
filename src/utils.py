import matplotlib.pyplot as plt

def plot_eigenvector(vec, lambda_1, lambda_2, n=100, index=-1):
    plt.plot(vec[:n, index])
    plt.xlim(0, n - 1)
    plt.xlabel('i')
    plt.ylabel('v_n(i)')
    plt.title('Region n=2')
    filename = f"eigen_plot_lambda_{lambda_1}_{lambda_2}_v_{index+1}.png"
    plt.savefig(filename)
    print(f"Plot saved as {filename}")
