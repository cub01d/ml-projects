# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
FROM jupyter/base-notebook

LABEL maintainer="Andrew Stryker <andrew.stryker@ask.com>"

# install base packages
USER root

RUN apt-get update \
 && apt-get install -y build-essential

# set-up workspace
USER $NB_UID

COPY requirements.txt $HOME
COPY taboo-igloo-challenge.ipynb $HOME
COPY weapons-sample.jsonl $HOME
COPY test-words.txt $HOME
COPY images/no-guns.png $HOME/images/no-guns.png

RUN conda install pip
RUN pip install --upgrade pip
RUN pip install -r $HOME/requirements.txt
RUN python -m spacy download en_core_web_lg

# back to notebook user at exit
USER $NB_UID
