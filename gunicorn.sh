#!/bin/bash
#conda activate just_do_it #（在linux上创建好自己的环境，可选）
#nohup source blogvenv/bin/activate &
nohup gunicorn -w 4 -b 0.0.0.0:5000 myblog:app > gunicorn.log 2>&1 & #（带日志）
