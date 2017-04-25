Red Hat/Fedora package to sanity check /dev/urandom, using the randomsanity.org service

Installing the RPM:

    sudo rpm -ivh https://github.com/lmacken/randomsanity_redhat/releases/download/v1.0/randomsanity-1.0-1.fc25.noarch.rpm

Enabling the systemd service:

    sudo systemctl enable randomsanity
