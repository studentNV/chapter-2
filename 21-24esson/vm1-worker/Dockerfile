FROM centos:7
RUN yum install java-1.8.0-openjdk -y && \
    yum install wget -y && \
    wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz && \
    mkdir /opt/hadoop-3.1.2/ && \
    tar -xvf  hadoop-3.1.2.tar.gz -C /opt/hadoop-3.1.2/ && \
    rm hadoop-3.1.2.tar.gz && \
    useradd hadoop && useradd yarn && useradd hdfs && \
    usermod -a -G hadoop hdfs && \
    usermod -a -G hadoop yarn
RUN mkdir -p /opt/hadoop/mount1/datanode-dir /opt/hadoop/mount2/datanode-dir && \
    chown hdfs:hadoop /opt/hadoop/mount1/datanode-dir/ /opt/hadoop/mount2/datanode-dir/
RUN mkdir -p /usr/local/hadoop/current/ && \
    ln -s /opt/hadoop-3.1.2/* /usr/local/hadoop/current/ && \
    mkdir -p /opt/hadoop/mount1/nodemanager-local-dir /opt/hadoop/mount2/nodemanager-local-dir /opt/hadoop/mount1/nodemanager-log-dir /opt/hadoop/mount2/nodemanager-log-dir && \
    chown yarn:hadoop /opt/hadoop/mount1/nodemanager-local-dir /opt/hadoop/mount2/nodemanager-local-dir /opt/hadoop/mount1/nodemanager-log-dir /opt/hadoop/mount2/nodemanager-log-dir
RUN yum install wget -y && \
    wget https://gist.githubusercontent.com/rdaadr/2f42f248f02aeda18105805493bb0e9b/raw/6303e424373b3459bcf3720b253c01373666fe7c/hadoop-env.sh -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh  && \
    sed -i 's|"%PATH_TO_OPENJDK8_INSTALLATION%"|/usr/lib/jvm/jre-1.8.0-openjdk|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%PATH_TO_HADOOP_INSTALLATION"|/usr/local/hadoop/current/hadoop-3.1.2/|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    sed -i 's|"%HADOOP_HEAP_SIZE%"|512M|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hadoop-env.sh && \
    wget https://gist.githubusercontent.com/rdaadr/64b9abd1700e15f04147ea48bc72b3c7/raw/2d416bf137cba81b107508153621ee548e2c877d/core-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \
    sed -i 's|%HDFS_NAMENODE_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/core-site.xml && \
    wget https://gist.githubusercontent.com/rdaadr/2bedf24fd2721bad276e416b57d63e38/raw/640ee95adafa31a70869b54767104b826964af48/hdfs-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%NAMENODE_DIRS%|/opt/hadoop/mount1/namenode-dir,/opt/hadoop/mount2/namenode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    sed -i 's|%DATANODE_DIRS%|/opt/hadoop/mount1/datanode-dir,/opt/hadoop/mount2/datanode-dir|'  /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/hdfs-site.xml && \
    wget https://gist.githubusercontent.com/Stupnikov-NA/ba87c0072cd51aa85c9ee6334cc99158/raw/bda0f760878d97213196d634be9b53a089e796ea/yarn-site.xml -O /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml  && \
    sed -i 's|%YARN_RESOURCE_MANAGER_HOSTNAME%|vm1-headnode|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOCAL_DIR%|/opt/hadoop/mount1/nodemanager-local-dir,/opt/hadoopmount2/nodemanager-local-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml && \
    sed -i 's|%NODE_MANAGER_LOG_DIR%|/opt/hadoop/mount1/nodemanager-log-dir,/opt/hadoop/mount2/nodemanager-log-dir|' /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/yarn-site.xml
RUN mkdir /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chown -R :hadoop /usr/local/hadoop/current/hadoop-3.1.2/logs && \
    chmod -R g+wxr /usr/local/hadoop/current/hadoop-3.1.2/logs
RUN touch /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "#!/bin/bash" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "su -l hdfs -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/hdfs --daemon start datanode\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "su -l yarn -c \"/usr/local/hadoop/current/hadoop-3.1.2/bin/yarn --daemon start nodemanager\"" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh.sh && \
    echo "while :" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "do" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "sleep 10" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh && \
    echo "done" >> /usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh
ENTRYPOINT ["/bin/bash", "/usr/local/hadoop/current/hadoop-3.1.2/etc/hadoop/start-datanode-nodemanager.sh"]
