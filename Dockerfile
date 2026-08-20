FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css
COPY google45fdf7cf0bba3261.html /usr/share/nginx/html/google45fdf7cf0bba3261.html
COPY privacy.html /usr/share/nginx/html/privacy.html
COPY favicon.ico /usr/share/nginx/html/favicon.ico
COPY favicon.png /usr/share/nginx/html/favicon.png
COPY icon.png /usr/share/nginx/html/icon.png

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]