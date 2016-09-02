# https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook
FROM jupyter/scipy-notebook:98f275e5347e

MAINTAINER Matt Burton <matt@mcburton.net>

COPY ./poems /home/jovyan/work/poems/
COPY ./poemeta.csv /home/jovyan/work/
COPY ./defactoring-pace-of-change.ipynb /home/jovyan/work/
COPY ./notebook_resources/ /home/jovyan/work/notebook_resources

USER root
RUN chown -R jovyan:users /home/jovyan/work

USER jovyan
