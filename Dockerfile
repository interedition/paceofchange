FROM jupyter/datascience-notebook


COPY ./poems /home/jovyan/work/poems/
COPY ./poemeta.csv /home/jovyan/work/
COPY ./defactoring-pace-of-change.ipynb /home/jovyan/work/
COPY ./notebook_resources/ /home/jovyan/work/

USER root
RUN chown -R jovyan:users /home/jovyan/work

USER jovyan
