FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dnd ./dnd
COPY scraped_data ./scraped_data


CMD ["dnd.server.handler.handler"]
