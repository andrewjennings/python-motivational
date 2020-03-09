FROM python:2-alpine

ADD . /code
WORKDIR /code
RUN apk --update add alpine-sdk freetype freetype-dev zlib zlib-dev jpeg-dev && pip install -r requirements.txt
ENTRYPOINT ["python","motivational.py"]
CMD ["--help"]
