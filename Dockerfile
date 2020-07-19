FROM ubuntu:18.04

RUN apt update
RUN apt -y install python3 python3-pip


# source code
COPY apps /code/apps
COPY app.py /code/app.py
COPY commands.py /code/commands.py
COPY data.db /code/data.db
COPY enums.py /code/enums.py
COPY middlewares.py /code/middlewares.py
COPY requirements.txt /code/requirements.txt
COPY routes.py /code/routes.py
COPY run.py /code/run.py
COPY views.py /code/views.py

WORKDIR /code
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

CMD ["python3", "run.py"]

