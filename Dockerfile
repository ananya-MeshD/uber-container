# Use openSUSE Leap 15.6 as the base image 

FROM opensuse/leap:15.6 

 
 

# Refresh package lists and install required packages 

RUN zypper refresh && \ 

    zypper install -y python3 python3-pip nginx supervisor && \ 

    ln -s /usr/bin/python3 /usr/bin/python && \ 

    zypper clean 

 
 

# Install Flask 

RUN pip install flask 

 
 
 

# Install Python dependencies (including debugpy) 

RUN pip3 install debugpy 

 
 

# Create application and configuration directories 

RUN mkdir -p /app /var/log/supervisor 

 
 

# Copy the Supervisor configuration file 

COPY supervisord.conf /etc/supervisord.conf 

 
 

# Expose ports for Nginx and Python services 

EXPOSE 80 5000 5001 

 
 

# Set the working directory 

WORKDIR /app 

 
 

# Start Supervisor as the main process 

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"] 

 
 
