FROM dhi.io/python:3.12-dev AS builder
WORKDIR /app
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["/venv/bin/python3", "-m", "uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]

FROM dhi.io/python:3.12
WORKDIR /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY --from=builder /app .
EXPOSE 8000
CMD ["/venv/bin/python3", "-m", "uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]

