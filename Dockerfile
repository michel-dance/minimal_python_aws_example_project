FROM ubuntu:18.04

# Commands to prime the docker container
RUN apt-get update
RUN apt-get install -y libpq-dev python3 python3-venv make wget git python3-pip rustc gcc libssl-dev

ENV VIRTUAL_ENV=/opt/python
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ARG pip_index_url
ENV PIP_INDEX_URL=$pip_index_url

RUN python3 -m pip install --index-url="${PIP_INDEX_URL}" setuptools_rust
RUN python3 -m pip install --index-url="${PIP_INDEX_URL}" snips-nlu
RUN python3 -m pip install --index-url="${PIP_INDEX_URL}" minimal_aws_example_project

#CMD ["python3", "-m", "pip", "list"]
ENTRYPOINT ["python3", "-m", "example"]
