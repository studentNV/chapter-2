FROM centos:7
# for become agent
RUN yum update -y  && \
	yum install java-1.8.0-openjdk -y  && \
	yum install epel-release -y  && \
	yum install ansible -y  && \
	yum install python3 -y  && \
	useradd Jenkins -d /var/lib/Jenkins  && \
	yum install openssh-server -y && \
	su -l Jenkins -c "ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa <<< y"  && \
	su -l Jenkins -c "cat ~/.ssh/id_rsa.pub > ~/.ssh/authorized_keys"  && \
	chmod 644  /var/lib/Jenkins/.ssh/authorized_keys  && \
	ssh-keygen -A
EXPOSE 22
# for unit test
RUN yum install git -y && \
	git clone https://github.com/studentNV/student-exam2.git /opt/student-exam2 && \
	chown Jenkins:Jenkins -R /opt/student-exam2 && \
	su -l Jenkins -c "python3 -m venv /opt/student-exam2/venv" && \
	su -l Jenkins -c "/opt/student-exam2/venv/bin/pip install --upgrade pip" && \
	su -l Jenkins -c "/opt/student-exam2/venv/bin/pip install -e /opt/student-exam2" && \
	pip3 install flask && \
	FLASK_APP=opt/student-exam2/js_example && \
	LC_ALL=en_US.utf-8 && \
  su -l Jenkins -c "/opt/student-exam2/venv/bin/pip install -e '/opt/student-exam2[test]'"
# for docker
RUN yum install yum-utils devicemapper-persistent-data && \
	yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
	yum install -y docker-ce && \
	echo "Jenkins ALL=(ALL:ALL) NOPASSWD:/usr/bin/docker" >> /etc/sudoers && \
	echo "root ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers && \
	yum install sudo -y
# for deploy
RUN git clone https://github.com/studentNV/ansible-exam2.git /opt/ansible-exam2 && \
	chown Jenkins:Jenkins -R /opt/ansible-exam2
ENTRYPOINT ["/usr/sbin/sshd","-D"]
