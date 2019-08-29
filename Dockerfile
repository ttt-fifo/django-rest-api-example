FROM python:3.7.4-alpine
ENV PYTHONUNBUFFERED 1
EXPOSE 5000
RUN addgroup -g 1008 appgroup && \
    adduser -h /code -s /bin/false -G appgroup -D -u 1008 appuser 
COPY --chown=appuser:appgroup ./requirements.txt /code
WORKDIR /code
RUN echo "http://mirror.leaseweb.com/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add --no-cache \
    gcc \
    libc-dev \
    geos-dev && \
    pip install --no-cache-dir -r requirements.txt
USER appuser
COPY --chown=appuser:appgroup ./ /code/
WORKDIR /code/api_example
RUN python ./manage.py migrate && \
    python ./providers/fixtures/language_data.py && \
    python ./providers/fixtures/currency_data.py && \
    python ./manage.py loaddata language_data && \
    python ./manage.py loaddata currency_data
CMD ["python", "./manage.py", "runserver", "0.0.0.0:5000"]
