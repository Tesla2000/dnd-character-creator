FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dnd_character_creator ./dnd_character_creator

CMD ["dnd_character_creator.server.handler.handler"]
