# Makefile
#
################################

.PHONY: clean all

clean:
	find . -type f -name '*.pyc' -delete


cron_0:
	PYTHONPATH=${PWD} python cron_0.py


cron_app:
	PYTHONPATH=${PWD} python cron_app.py


cron_app0:
	PYTHONPATH=${PWD} python cron_app0.py


all: clean cron_app
