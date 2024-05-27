# RealTime Network Speed Monitor

This is a Python application that monitors and displays the real-time network download and upload speeds. It uses the `psutil` library to gather network statistics and `tkinter` for the graphical user interface.

## Code Overview

The main logic of the application is in the `main.py` file. It defines two main functions:

- `get_net_speed()`: This function calculates the network speed by sampling the sent and received bytes over a time interval.

- `refresh()`: This function updates the download and upload speed labels in the GUI every 250 milliseconds.

The application uses a themed Tkinter window to display the network speeds. The download and upload speeds are displayed in separate labels.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/m4xy07/Realtime-Network-Usage-Monitor.git
```

2. Navigate to the project directory:

```sh
cd Realtime-Network-Usage-Monitor
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the main.py file:

```sh
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
