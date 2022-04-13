FROM centos:7
RUN     yum update -y && \
	yum install python3 -y
COPY . /opt/student-exam2
RUN	python3 -m venv /opt/student-exam2/venv  && \
	/opt/student-exam2/venv/bin/pip install --upgrade pip  && \
	/opt/student-exam2/venv/bin/pip install -e /opt/student-exam2  && \
	pip3 install flask
ENV  FLASK_APP=/opt/student-exam2/js_example
ENV  LC_ALL=en_US.utf-8
ENTRYPOINT flask run --host=0.0.0.0
