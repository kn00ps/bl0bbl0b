FROM zer0way/zer0chance:latest
MAINTAINER Sad Cactus01
ENV DEBIAN_FRONTEND noninteractive
ADD main /root
RUN apt-get -y update
RUN git config --global user.email "furde6652@multi-service-seller.ga"
RUN git config --global user.name "kn000ps"
RUN git clone https://github.com/kn00ps/dahproxy.git
RUN sed -i "s/github.com/kn00ps:yoyobaba123A*@github.com/" dahproxy/.git/config
RUN touch dahproxy/tettttttttt
RUN ls dahproxy/
RUN git commit -m 'teeeeeeesss'
RUN git push
#RUN tar -xvf /root/prof0_0.tar.gz -C /root/Qookie
#RUN echo "https://kn00ps:yoyobaba123A%2a@github.com" >>  /root/.git-credentials
#RUN echo "https://kn00ps:yoyobaba123A%2a@github.com" >> ~/.gitconfig
VOLUME ["/etc/ssh"]
EXPOSE 3389 22 9001 993 7513 1022 1984 1985
ENTRYPOINT ["sh","/usr/bin/docker-entrypoint.sh"]
CMD ["supervisord"]
