import os


def pytest_configure() -> None:
    os.environ.setdefault("POSTGRES_SERVER", "localhost")
    os.environ.setdefault("POSTGRES_PORT", "5432")
    os.environ.setdefault("POSTGRES_USER", "postgres")
    os.environ.setdefault("POSTGRES_PASSWORD", "test-password")
    os.environ.setdefault("POSTGRES_DB", "example")
