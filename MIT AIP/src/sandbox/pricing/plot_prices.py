import matplotlib.pyplot as plt
import os

def plot_and_save_prices(prices, folder="C:\\GIT\\Work\\MIT AIP\\docs\\figures", file_name="price_plot.png"):
    """
    Plots the generated prices over 24 hours and saves the plot as a file in the specified folder.
    :param prices: List of 24 hourly electricity prices.
    :param folder: The folder to save the plot in.
    :param file_name: The name of the file to save the plot as.
    """
    # Ensure the folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # File path for the plot
    file_path = os.path.join(folder, file_name)
    
    # Plot the prices
    hours = list(range(24))
    plt.figure(figsize=(10, 6))
    plt.plot(hours, prices, marker="o", linestyle="-", color="b")
    plt.title("Electricity Prices Over 24 Hours")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Price (€)")
    plt.xticks(hours)  # Show all hours on the x-axis
    plt.grid(True)
    
    # Save the plot to the file
    plt.savefig(file_path)
    plt.show()

    print(f"Plot saved at: {file_path}")

# Example usage:
if __name__ == "__main__":
    from price_generation import generate_next_day_prices  # Import the core logic
    
    # Generate the next day prices
    next_day_prices = generate_next_day_prices(base_price=50, volatility=5)
    
    # Plot and save the prices to the specified folder
    plot_and_save_prices(next_day_prices['prices'], folder="C:\\GIT\\Work\\MIT AIP\\docs\\figures", file_name="price_generation_plot.png")
