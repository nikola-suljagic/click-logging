# click-logging
Python tool to handle log messages that are sent from mikroE development board


## Project setup

* Install poetry python package manager
    - Ubuntu
        * Installation: `curl -sSL https://install.python-poetry.org | python3 -`
        * Verify installation: poetry --version

* Install python environment via poetry: `poetry install`
* Change permission for serial port: `sudo chmod 777 /dev/ttyUSB0`


## Logging

* Run logging: `poetry run python click_logging.py`
* Run logging with log file argument: `poetry run python click_logging.py --log-file "log_events.csv"`
* Stop logging by pressing `CTRL + C`
* Log artifacts should appear in **events.csv** if --log-file isn't specified or in log file that is specified via --log-file arg 
