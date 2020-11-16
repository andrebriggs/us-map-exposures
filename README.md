# Tracking Exposure Notification System in the US

Visual map of the US states implementing the [ENS protocol](https://www.google.com/covid19/exposurenotifications/) to track COVID-19.

Install modules
```console
$ pip3 install -r requirements.txt
```

Run script
```console
$ python3 create-map.py
```

View HTML
```console
$ open GAEN_Exposure_Notificaton_US_States.html
```

The `US_GAEN_STATUS.csv` file has a scale of 0 to 1 where 0.5 means exposure notifications are "in progress" for that state.

The `us-states.json` file contains the gepgraphy for US states.