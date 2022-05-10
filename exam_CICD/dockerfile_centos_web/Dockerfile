FROM centos:7
RUN     yum update -y && \
        yum install git -y && \
        git clone https://github.com/studentNV/student-exam2.git && \
        yum install python3 -y && \
        python3 -m venv student-exam2/venv && \
        student-exam2/venv/bin/pip install --upgrade pip && \
        student-exam2/venv/bin/pip install -e student-exam2 && \
        pip3 install flask
ENV  FLASK_APP=student-exam2/js_example
ENV  LC_ALL=en_US.utf-8
ENTRYPOINT flask run --host=0.0.0.0
