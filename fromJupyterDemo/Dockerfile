# Docker demo image, as used on try.jupyter.org and tmpnb.org

FROM jupyter/demo

MAINTAINER CognitiveScale <devops@cognitivescale.com>

ENV COGU_HOME=/home/jovyan/notebooks/CogU \
    JUPYTER_SCRIPTS=/jupyter_scripts \
    GIT_REPO_URL=https://github.com/CognitiveScale/docker-demo-images/tree/relpath-scripts \
    JUPYTER_STARTUP_DIR=/home/jovyan/.ipython/profile_default/startup

# For Jupyter 4, there is no profile_default.  Instead there is ~/.jupyter and need a hook to run scripts

USER root
#COPY dexy.yaml dexy_requirements.txt run.sh j2cli.sh setup_git_filters.sh $JUPYTER_SCRIPTS/ 
ADD https://github.com/CognitiveScale/docker-demo-images/tree/relpath-scripts/scripts $JUPYTER_SCRIPTS/
ADD https://raw.githubusercontent.com/CognitiveScale/docker-demo-images/relpath-scripts/scripts/page.html /srv/templates/page.html
#ADD page.html /srv/templates/page.html
ADD $GIT_REPO_URL/scripts/bash_kernel_wrapper.py $GIT_REPO_URL/scripts/stateful_bash_magics.py $JUPYTER_STARTUP_DIR

RUN cd $JUPYTER_SCRIPTS && \
    wget https://s3.amazonaws.com/c12e-cognitivecloud/notebook/ipynb_git_output_filter.py && \
    wget https://s3.amazonaws.com/c12e-cognitivecloud/notebook/strip_output_notebook.py && \
    chown -R jovyan:jovyan $JUPYTER_SCRIPTS && \
    chown -R jovyan:jovyan /home/jovyan && \
    apt-get -y install nodejs npm && \
    ln -s /usr/bin/nodejs /usr/bin/node 

USER jovyan

RUN $CONDA_DIR/envs/python2/bin/pip install -r $JUPYTER_SCRIPTS/dexy_requirements.txt
# Install bash_kernel to python front end
RUN python -m bash_kernel.install

USER jovyan

CMD ["/bin/bash","-c","$JUPYTER_SCRIPTS/run.sh && ipython notebook"]

