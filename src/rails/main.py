from fastapi import FastAPI

from rails.rails import Rails

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/rails")
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
