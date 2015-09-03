# Docker demo image, as used on try.jupyter.org and tmpnb.org

FROM jupyter/demo

MAINTAINER CognitiveScale <devops@cognitivescale.com>

ENV COGU_HOME=/home/jovyan/notebooks/CogU \
    JUPYTER_SCRIPTS=/jupyter_scripts \
    GIT_REPO_URL=https://raw.githubusercontent.com/CognitiveScale/docker-demo-images/relpath-scripts \
    JUPYTER_STARTUP_DIR=/home/jovyan/.ipython/profile_default/startup

# For Jupyter 4, there is no profile_default.  Instead there is ~/.jupyter and need a hook to run scripts

USER root
RUN mkdir -p $JUPYTER_SCRIPTS

RUN cd $JUPYTER_SCRIPTS && \
    wget https://s3.amazonaws.com/c12e-cognitivecloud/notebook/ipynb_git_output_filter.py && \
    wget https://s3.amazonaws.com/c12e-cognitivecloud/notebook/strip_output_notebook.py && \
    apt-get -y install nodejs npm && \
    ln -s /usr/bin/nodejs /usr/bin/node

# Messy remapping for common files because git doesn't allow folder downloads and 
# docker requires ADD/COPY sources to be in the Dockerfile tree (no ../ allowed)
# The benefit is that we have common files available for all jupyter containers
#ADD https://raw.githubusercontent.com/CognitiveScale/docker-demo-images/relpath-scripts/scripts/dexy.yml $JUPYTER_SCRIPTS/
ADD $GIT_REPO_URL/scripts/dexy.yaml \
    $GIT_REPO_URL/scripts/dexy_requirements.txt \ 
    $GIT_REPO_URL/scripts/j2cli.sh \ 
    $GIT_REPO_URL/scripts/setup_git_filters.sh \ 
    $JUPYTER_SCRIPTS/
ADD $GIT_REPO_URL/scripts/page.html /srv/templates/page.html
ADD $GIT_REPO_URL/scripts/bash_kernel_wrapper.py \
    $GIT_REPO_URL/scripts/stateful_bash_magics.py \
    $JUPYTER_STARTUP_DIR/

RUN chown -R jovyan:jovyan $JUPYTER_SCRIPTS && \
    chown -R jovyan:jovyan /home/jovyan

USER jovyan

RUN $CONDA_DIR/envs/python2/bin/pip install -r $JUPYTER_SCRIPTS/dexy_requirements.txt
# Install bash_kernel to python front end
RUN pip install bash_kernel && \
    python -m bash_kernel.install 
    
CMD ["/bin/bash","-c","$JUPYTER_SCRIPTS/run.sh && ipython notebook"]

