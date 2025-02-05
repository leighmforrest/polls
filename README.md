# Polls

## Github Actions

This repo is set up to deploy the application with one command: `git push`. Github Actions make this possible. For Github Actions to work, secrets need to be set up.

### Repository Secrets

| Variable | Value |
| ----------- | ----------- |
| APP_DIRECTORY | Absoulte path of the project directory on the server.        |
|PRIVATE_KEY | The private key found on your local machine that is used to SSH into the VPS server.
| SERVER_IP | IP address of the VPS server.|
| USERNAME | Username of the sudo user on the VPS.


## Server Setup

### Artifacts

In the repo, there are generic files in the `artifacts` directory used to set up the Supervisor daemon to run gunicorn `gunicorn.conf` and the nginx configuration file: `nginx.conf` Both are set up to run a socket file in `/run` directory.

### Permissions for Socket File

You need to have the directory and proper permissions for the socket file. Set them up as follows:

    sudo mkdir -p /run/<PROJECT_NAME>  # Create directory for socket
    sudo chown <APP_USER>:www-data /run/<PROJECT_NAME>  # Give ownership to app user
    sudo chmod 770 /run/<PROJECT_NAME>  # Allow both app user and www-data access

### Static Files

TODO

#### Commands for the Server

    ./manage.py collectstatic # do this before setting permissions
    sudo chown -R <APP_USER>:www-data <APP_DIRECTORY>/staticfiles/
    sudo chmod -R 775 <APP_DIRECTORY>/staticfiles/
    sudo usermod -aG www-data <APP_USER> # Add APP_USER to www-data


