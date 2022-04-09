FROM centos:7
RUN	yum update -y && \
	yum install git -y && \
	git clone https://github.com/studentNV/student-exam2.git && \
	yum install python3 -y && \
	python3 -m venv student-exam2/venv && \
	student-exam2/venv/bin/pip install --upgrade pip && \
	student-exam2/venv/bin/pip install --upgrade pip && \
	student-exam2/venv/bin/pip install -e student-exam2 && \
	pip3 install flask
RUN	touch /student-exam2/start-web.sh && \
	echo "#!/bin/bash" >> /student-exam2/start-web.sh && \
	echo "/usr/bin/python3 -m flask run --host=0.0.0.0" >> /student-exam2/start-web.sh && \
	echo "while :" >> /student-exam2/start-web.sh && \
	echo "do" >> /student-exam2/start-web.sh && \
	echo "sleep 10" >> /student-exam2/start-web.sh && \
	echo "done" >> /student-exam2/start-web.sh
ENV  FLASK_APP=student-exam2/js_example
ENV  LC_ALL=en_US.utf-8
ENTRYPOINT ["/bin/bash", "/student-exam2/start-web.sh"]
