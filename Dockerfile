FROM python:3-slim

WORKDIR /usr/src/app
ADD . / ./

RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install opencv-contrib-python --user
RUN pip3 install Pillow
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y python-tk
RUN apt-get install sqlite3
RUN apt-get install -y sqlitebrowser

CMD ["python3","./main_screen.py"]
