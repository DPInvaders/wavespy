FROM centos:7
RUN yum install -y python3 python-psutil python-twisted wmctrl gnupg fakeroot rpm-build
RUN mkdir pyacry2
COPY . wavespy
RUN cd wavespy && python3 setup.py bdist_rpm