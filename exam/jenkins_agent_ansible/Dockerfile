FROM centos:7
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
ENTRYPOINT ["/usr/sbin/sshd","-D"]
