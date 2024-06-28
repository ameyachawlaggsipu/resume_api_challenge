# Resume API Challenge

This project implements a REST API using AWS Lambda and DynamoDB for managing resumes. It retrieves resume data based on ID from DynamoDB.

## How It Works

- Uses AWS Lambda to handle API requests.
- Retrieves resume data from DynamoDB based on ID.
- Implements authentication mechanisms for secure access.
- Ensures robust error handling for resume retrieval operations.

## Example Output

- **Endpoint:** `https://e8muaduk8j.execute-api.us-east-2.amazonaws.com/default/resume_api?id=1`
- **Sample Output:**
  ```json
  {
    "id": "1",
    "name": "John Doe",
    "email": "jd@jdnoname.com",
    "school": "Oxford",
    "skills": ["Python", "AWS"]
  }

# Built With

This project utilizes the following technologies:

- **AWS Lambda** - Serverless computing platform.
- **DynamoDB** - NoSQL database service by AWS.
- **Python** - Programming language for Lambda functions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [ameya.chawla.ml@gmail.com](mailto:ameya.chawla.ml@gmail.com).
