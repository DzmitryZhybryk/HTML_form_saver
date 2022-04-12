FROM python:3.9

ENV PYTHONPATH "${PYTHONPATH}:/csv_storage_app"
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /csv_storage_app

EXPOSE 5001

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "./app_storage.py"]