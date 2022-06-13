FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/code
RUN mkdir $WEBAPP_DIR
WORKDIR $WEBAPP_DIR
ADD requerimientos.txt $WEBAPP_DIR/
RUN pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org" --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
RUN pip install -r requerimientos.txt
ADD . $WEBAPP_DIR/
