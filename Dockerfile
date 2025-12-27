FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dnd_character_creator ./dnd_character_creator
COPY scraped_data ./scraped_data

CMD ["dnd_character_creator.server.handler.handler"]
