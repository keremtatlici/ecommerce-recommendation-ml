
# Recommendation API

This project provides an API that offers recommendations to users. This API, built using FastAPI, takes user IDs and returns recommendations.

## Requirements

- Docker
- fastapi
- uvicorn
- scipy
- scikit-learn
- pydantic
- implicit
## Setup and Run

This section shows how to run the API using Docker.

### Running the API with Docker

1. Copy the Dockerfile and Install Requirements

   Navigate to your project directory and run the following commands to build your Docker image:

   docker build -t recommendation-api .

2. Start the Docker Container

   Use the following command to start the Docker container:

   docker run -p 8000:8000 recommendation-api

   This command runs the API on IP address 0.0.0.0 and port 8000.

## API Usage

### API Endpoints

#### /api/recommend/

- Method: POST
- Description: Returns recommendations for the specified user ID.
- Request Body:

{
  "userid": "7670b27dcd2805736b5efb8e2ef06917"
}

### Example Request

Below is an example of how to make a request using curl:

curl -X POST "http://localhost:8000/api/recommend/" -H "Content-Type: application/json" -d '{"userid": "7670b27dcd2805736b5efb8e2ef06917"}'

### Example Response
```
{
    "user_id": "7670b27dcd2805736b5efb8e2ef06917",
    "recommendations": [
        {
            "item_id": "30b8a8a8c59f1af8aa2e4a808ea41dd0",
            "score": "0.78794867"
        },
        {
            "item_id": "15fe95fe0d762beed6a1d4f4a0a534c9",
            "score": "0.5908718"
        },
        {
            "item_id": "0bcb5964abe7ad28f57daf85c400ac02",
            "score": "0.57574815"
        },
        {
            "item_id": "e29705cb6cb221e2ca48b929266a941e",
            "score": "0.56214345"
        },
        {
            "item_id": "3fbaa36da78967b475c4f9b0fa28b1bd",
            "score": "0.55542296"
        },
        {
            "item_id": "c4b62a9021501de8f460ea310beb8084",
            "score": "0.55239314"
        },
        {
            "item_id": "2b9d1e58381f5a1d0aac0bb2b186aa63",
            "score": "0.5344231"
        },
        {
            "item_id": "ef602c04aeecbe2c3b0d39ee02a3c9d9",
            "score": "0.5335619"
        },
        {
            "item_id": "d6afa22ab475d41e7dc9b721f3f795ad",
            "score": "0.50748825"
        },
        {
            "item_id": "75e898d4114c419eb3dfecb66d865f46",
            "score": "0.50272304"
        }
    ]
}
````

