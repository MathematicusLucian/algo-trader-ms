FROM nginx:alpine
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
###
RUN chmod 777 /usr/share/nginx/html 
RUN chmod 777 /usr/share/nginx/html/
###
EXPOSE 80 443
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]

# # FROM ubuntu
# FROM nginx:alpine
# # RUN apt-get update && apt-get install -y curl sudo
# # RUN curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
# # RUN sudo apt-get install -y nodejs
# # RUN echo "NODE Version:" && node --version
# # RUN echo "NPM Version:" && npm --version
# COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
# # RUN mkdir -p /user/src/banana
# # WORKDIR /usr/src/ui
# # RUN npm run build
# # WORKDIR /usr/nginx
# RUN chmod 777 /usr/share/nginx/html 
# EXPOSE 80 443
# ENTRYPOINT ["nginx"]
# CMD ["-g", "daemon off;"]