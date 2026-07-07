FROM public.ecr.aws/lambda/python:3.12

WORKDIR /var/task

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml

COPY dnd ./dnd
COPY scraped_data ./scraped_data


CMD ["dnd.server.handler.handler"]
