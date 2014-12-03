#!/bin/bash
 
NAME="briefme_cms"                                                     # Name of the application
DJANGODIR=/home/cirotteau/apps/contexte/eu-hackathon/eu-hackathon/positions_explorer/          # Django project directory
BIND="127.0.0.1:8005"                                                  # binding
USER=cirotteau                                                         # the user to run as
GROUP=cirotteau                                                        # the group to run as
NUM_WORKERS=9                                                          # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=positions_explorer.settings                              # which settings file should Django use
DJANGO_WSGI_MODULE=wsgi                                                # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source ../../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=$BIND \
  --log-level=debug \
  --log-file=-
