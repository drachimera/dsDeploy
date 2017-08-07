FROM centos:7
MAINTAINER "Matthew Markland" <markland.matthew@mayo.edu>

# Systemd stuff from
# https://serverfault.com/questions/824975/failed-to-get-d-bus-connection-operation-not-permitted#825027
ENV container docker
RUN yum -y update; yum clean all
RUN yum -y install systemd; yum cleanall; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum -y install \
            man \
            man-pages \
            which \
            less \
            zlib-devel \
            bzip2-devel \
            bzip2 \
            unzip \
            xz-devel \
            pcre-devel \
            curl-devel \
            texinfo \
            readline-devel \
            xorg-x11-server-devel libX11-devel libXt-devel \
            java-sdk \
            wget \
            gcc \
            gcc-c++ \
            gcc-gfortran \
            make \
            ed \
            libiodbc \ 
            cairo-devel \
            libpng \
            blas-devel \
            lapack-devel \
            mesa*

RUN wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh
RUN bash Anaconda3-4.4.0-Linux-x86_64.sh -f -b
ENV PATH "/root/anaconda3/bin/:$PATH"

RUN conda update libgcc
RUN conda install pyodbc
RUN pip install nose2
RUN pip install -U tabulate
RUN pip install -U future
RUN pip install ibm_db_sa
RUN conda install seaborn
RUN pip install simpy
RUN conda install scikit-learn
RUN conda install sqlalchemy
RUN pip install py4j

#for jupyter notebook
EXPOSE 8888

# This is for systemd also.
VOLUME [ "/sys/fs/cgroup" ]

#CMD ["/usr/sbin/init"]
CMD ["sh"]
