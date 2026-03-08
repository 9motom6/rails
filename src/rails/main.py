from fastapi import FastAPI
from pydantic import BaseModel, Field

from rails.rails import Rails

app = FastAPI()


class RailsResponse(BaseModel):
    """Response containing the count of rail configurations."""

    count: int = Field(description="Number of possible rail configurations")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/rails", response_model=RailsResponse)
async def rails(length: int):
    """
    Calculate the number of rails needed for a given length.

    Args:
        length: The total length to cover with rails.

    Returns:
        A dictionary containing the count of rails needed.
    """
    count = Rails().count_rails_iterative(length=length)
    return {"count": count}


def main():
    print("Hello from rails!")


if __name__ == "__main__":
    main()
