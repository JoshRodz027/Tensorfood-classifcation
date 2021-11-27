# Add a line here to specify the docker image to inherit from.

FROM registry.aisingapore.net/polyaxon/aiap_pytorch_tf2_cpu:latest

ARG WORK_DIR="/home/polyaxon"
ARG USER="polyaxon"

WORKDIR $WORK_DIR

# Add lines here to copy over your src folder and 
# any other files you need in the image (like the saved model).
COPY ./src $WORK_DIR/src
COPY tensorfood.h5 $WORK_DIR
COPY test_img.jpg $WORK_DIR
COPY conda.yml $WORK_DIR


# Add a line here to update the conda environment using the conda.yml. 
# The environment to update is 'base'.

RUN conda env update -f conda.yml -n base
# RUN conda env update -f conda.yml -n polyaxon

RUN chown -R 1000450000:0 $WORK_DIR

USER $USER

EXPOSE 8000

# Add a line here to run your app
CMD ["python", "-m", "src.app"]
    # runs src.app within the polyaxon env without actually activating it

