FROM python:2.7
WORKDIR /home/zhangwenjie/blog

COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY . .
CMD ./gunicorn.sh
