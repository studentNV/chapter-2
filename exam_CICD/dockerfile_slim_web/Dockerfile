FROM python:3.8-slim-buster
RUN apt clean all && apt update -y && \
	pip3 install Flask  && \
	apt install git -y && \
	git clone https://github.com/studentNV/student-exam2.git
ENV FLASK_APP=student-exam2/js_example
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
