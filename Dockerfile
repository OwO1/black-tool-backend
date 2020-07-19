FROM ubuntu:18.04

RUN apt update
RUN apt -y install python3 python3-pip


# source code
COPY app /code/app
COPY app.py /code/app.py
COPY commands.py /code/app.py
COPY data.db /code/data.db
COPY enums.py /code/enums.py
COPY middlewares.py /code/middlewares.py
COPY requirements.txt /code/requirements.txt
COPY routes.py /code/routes.py
COPY run.py /code/run.py
COPY views.py /code/views.py

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/


WORKDIR /code

CMD ["python3", "run.py"]
