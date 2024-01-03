#First we have to import data

def load_data(orcl):
    """
    Task-1: Load historical data from the CSV file into a list of dictionaries.
    """
    info = []
    with open(orcl, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            data_point = dict(zip(header, values))
            info.append(data_point)
    return info

def calculate_sma(data, window=5):
    """
    Task-2: we have to calculate simple moving averages for a 5_day window.
    """
    sma_data = []
    for i in range(len(data)):
        if i < window - 1:
            sma = None  # SMA is not defined for the first few days
        else:
            close_prices = [float(data[j]['Close']) for j in range(i - window + 1, i + 1)]
            sma = sum(close_prices) / window
        sma_data.append({'Date': data[i]['Date'], 'SMA': sma})
    return sma_data

def calculate_rsi(data, window=14):
    """
    Task-2: In this task we have to calculate relative strength Index (RSI) for a 14-day window.
    """

    rsi_info = []
    losses = []
    gains = []


    for i in range(1, len(data)):
        close_price_diff = float(data[i]['Close']) - float(data[i - 1]['Close'])

        if close_price_diff > 0:
            gains.append(close_price_diff)
            losses.append(0)
        elif close_price_diff < 0:
            gains.append(0)
            losses.append(-close_price_diff)
        else:
            gains.append(0)
            losses.append(0)

        if i >= window:
            avg_gain = sum(gains[-window:]) / window
            avg_loss = sum(losses[-window:]) / window
            rs = avg_gain / avg_loss if avg_loss != 0 else float('inf')
            rsi = 100 - (100 / (1 + rs))
            rsi_info.append({'Date': data[i]['Date'], 'RSI': rsi})

    return rsi_info

def write_to_csv(data, file_path, header):
    """
    #write each indicator to a file
    """
    with open(file_path, 'w') as file:
        file.write(','.join(header) + '\n')
        for row in data:
            file.write(','.join(str(row[col]) for col in header) + '\n')

if __name__ == "__main__":
    # Task-1: Load historical data
    historical_data = load_data("orcl.csv")

    # Task-2: Calculate indicators
    sma_data = calculate_sma(historical_data)
    rsi_info = calculate_rsi(historical_data)

    # Task-3: Write indicators to files
    write_to_csv(sma_data, "orcl-sma.csv", header=['Date', 'SMA'])
    write_to_csv(rsi_info, "orcl-rsi.csv", header=['Date', 'RSI'])