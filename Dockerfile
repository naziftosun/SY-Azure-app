FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd
COPY sshd_config /etc/ssh/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x init.sh

EXPOSE 80 2222

ENTRYPOINT ["./init.sh"]