from serial import Serial
import ast
import datetime
import pandas as pd
import logging
from argparse import ArgumentParser

logging.basicConfig(encoding="utf-8", level=logging.INFO)


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="ClickLogging",
        description="Python tool for catching event messages from mikroE development board",
    )

    parser.add_argument(
        "--log-file",
        type=str,
        default="events.csv",
        help="Specify file where events will be stored in .csv format",
    )

    args = parser.parse_args()

    ser = Serial(
        "/dev/ttyUSB0",
        timeout=None,
        baudrate=921600,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
    )

    events = []
    try:
        while True:
            data = ser.readline()
            try:
                data_str = data.decode("utf-8")
                event_data = ast.literal_eval(data_str)
                event_data["time"] = str(datetime.datetime.now())
                events.append(event_data)
                logging.info(msg=f"[EVENT] {event_data}")
            except ValueError:
                logging.error("Can't create dict from event")
    except KeyboardInterrupt as ki:
        events_df = pd.DataFrame(events)

        events_df.to_csv(args.log_file, index=False)
