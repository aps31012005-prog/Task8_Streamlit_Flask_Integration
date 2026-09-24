# Task 8: Integrating Streamlit Frontend with Flask API

## 1. Project Title

### CIFAR-10 Deep Learning Prediction System
### Streamlit Frontend Integrated with Flask REST API

---

## 2. Objective

The objective of this task is to establish communication between a Streamlit frontend and a Flask backend for real-time deep learning inference.

The Streamlit application provides the user interface for uploading an image, while the Flask API receives the image, processes it using a trained CIFAR-10 CNN model, generates a prediction, and returns the result to the Streamlit frontend.

The main objectives of this task are:

- To integrate a Streamlit frontend with a Flask REST API.
- To transfer user input from Streamlit to Flask using HTTP requests.
- To perform real-time inference using a trained deep learning model.
- To return prediction results from Flask in JSON format.
- To display the prediction dynamically in the Streamlit interface.
- To test and validate the complete frontend-backend workflow.

---

## 3. Project Description

This project integrates two major components:

1. Streamlit frontend
2. Flask backend API

The trained CNN model is used for CIFAR-10 image classification.

The user uploads an image through the Streamlit interface. The image is transferred to the Flask `/predict` API using an HTTP POST request. The Flask backend preprocesses the image and passes it to the trained CNN model.

The model generates a predicted CIFAR-10 class and confidence value. Flask returns this information as a JSON response. Streamlit then displays the prediction dynamically to the user.

The complete workflow is:

```text
User
  ↓
Streamlit Frontend
  ↓
HTTP POST Request
  ↓
Flask REST API
  ↓
Image Preprocessing
  ↓
CIFAR-10 CNN Model
  ↓
Prediction
  ↓
JSON Response
  ↓
Streamlit Result Display
4. Technologies Used

The following technologies and Python libraries are used:

Python
TensorFlow
Keras
Flask
Streamlit
NumPy
Pillow
Requests
5. Reference Model

The application uses a previously trained CIFAR-10 convolutional neural network model.

Model file:

model/cifar10_cnn.keras

The model was developed in the previous task and is reused in this task for prediction.

The Flask backend loads the trained model and performs inference whenever an image is submitted through the /predict endpoint.

6. CIFAR-10 Classes

The model performs classification across the following ten CIFAR-10 classes:

Airplane
Automobile
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck
7. Project Structure

The main project structure is:

Task8_Streamlit_Flask_Integration/
│
├── app.py
├── flask_api.py
├── requirements.txt
├── README.md
│
├── model/
│   └── cifar10_cnn.keras
│
└── pages/
    └── 1_Image_Prediction.py
Description of Files
app.py

This is the main Streamlit application file. It starts the Streamlit frontend and provides the application interface.

flask_api.py

This file contains the Flask REST API. It loads the trained CIFAR-10 CNN model and provides endpoints for checking the API and generating predictions.

requirements.txt

This file contains the Python packages required to run the project.

README.md

This file contains project documentation, workflow information, testing details, and instructions for running the application.

model/cifar10_cnn.keras

This is the trained CIFAR-10 CNN model used by the Flask backend for image classification.

pages/1_Image_Prediction.py

This Streamlit page provides the image upload interface and communicates with the Flask backend for real-time prediction.

8. System Architecture

The overall architecture of the integrated application is:

                    USER
                      |
                      | Upload Image
                      v
             +-------------------+
             |   STREAMLIT UI    |
             |     Frontend      |
             +---------+---------+
                       |
                       | HTTP POST Request
                       v
             +-------------------+
             |     FLASK API     |
             |     /predict      |
             +---------+---------+
                       |
                       v
             +-------------------+
             | Image Processing  |
             |  & Preprocessing  |
             +---------+---------+
                       |
                       v
             +-------------------+
             |    CNN MODEL      |
             |     CIFAR-10      |
             +---------+---------+
                       |
                       v
             +-------------------+
             |    Prediction     |
             | Class + Confidence|
             +---------+---------+
                       |
                       | JSON Response
                       v
             +-------------------+
             |   STREAMLIT UI    |
             |  Result Display   |
             +-------------------+
9. Application Workflow

The application follows the following workflow.

Step 1: Start Flask Backend

The Flask backend is started using:

python flask_api.py

The API runs locally on:

http://127.0.0.1:5000
Step 2: Verify Flask API

The Flask home endpoint can be accessed using:

http://127.0.0.1:5000/

The API returns a JSON response confirming that the Flask backend is running.

Example:

{
    "endpoint": "/predict",
    "message": "CIFAR-10 Flask Prediction API is running",
    "method": "POST"
}
Step 3: Start Streamlit Frontend

The Streamlit application is started using:

streamlit run app.py

The Streamlit application runs locally and provides the user interface.

Step 4: Upload Image

The user navigates to the Image Prediction page and uploads a JPG, JPEG, or PNG image.

Step 5: Check Flask Connection

The Streamlit frontend checks whether the Flask API is available.

If the Flask API is running, the application displays:

Flask API is connected and running.

If the Flask API is unavailable, an error message is displayed asking the user to start the Flask backend.

Step 6: Send Image to Flask

After an image is uploaded, Streamlit sends the image to the Flask API using an HTTP POST request.

The request is sent to:

http://127.0.0.1:5000/predict

The uploaded image is transferred using the form-data field:

image
Step 7: Flask Processes the Image

The Flask backend receives the image and performs the following preprocessing operations:

Opens the uploaded image.
Converts the image to RGB format.
Resizes the image to 32 × 32 pixels.
Converts the image into a NumPy array.
Converts the pixel values to floating-point values.
Normalizes pixel values by dividing by 255.
Adds the required batch dimension.
Step 8: CNN Model Prediction

The preprocessed image is passed to the trained CIFAR-10 CNN model.

The model generates probability values for the ten CIFAR-10 classes.

The class with the highest probability is selected as the predicted class.

Step 9: Flask JSON Response

The Flask backend returns the prediction in JSON format.

Example:

{
    "predicted_class": "Frog",
    "confidence": 99.07
}
Step 10: Display Result in Streamlit

The Streamlit frontend receives the JSON response and displays:

Uploaded image
Predicted class
Confidence percentage
Flask API response
Integration success message

The user can therefore see the prediction without directly interacting with the Flask API.

10. Flask API Endpoints
10.1 Home Endpoint
GET /

Purpose:

The home endpoint verifies that the Flask API is running.

Example response:

{
    "endpoint": "/predict",
    "message": "CIFAR-10 Flask Prediction API is running",
    "method": "POST"
}
10.2 Prediction Endpoint
POST /predict

Purpose:

The /predict endpoint receives an image and generates a CIFAR-10 prediction using the trained CNN model.

The image must be sent using the following form-data field:

Key: image
Type: File
11. Error Handling

Error handling has been implemented in both the Flask backend and Streamlit frontend.

11.1 No Image Provided

If the Flask API receives a request without an image, it returns an error response.

Example:

{
    "error": "No image provided. Please upload an image."
}
11.2 Flask API Not Running

The Streamlit frontend checks the Flask API connection.

If the Flask API is not running, the Streamlit application displays an appropriate error message.

11.3 Connection Error

If Streamlit cannot connect to Flask, the application displays a connection error and asks the user to make sure that flask_api.py is running.

11.4 Request Timeout

A timeout is configured for the API request.

If the request takes too long, Streamlit displays a timeout message.

11.5 Unexpected Errors

Unexpected exceptions are handled and displayed to the user through the Streamlit interface.

12. Testing Methodology

The integrated application was tested at multiple levels.

Backend Testing

The Flask API was tested independently using Postman.

Frontend Testing

The Streamlit interface was tested by uploading images and checking the returned prediction.

Integration Testing

The complete Streamlit → Flask → CNN Model → Prediction workflow was tested.

Error Testing

The application was tested without uploading an image to verify that the empty-input case was handled correctly.

13. Test Case 1: Flask API Health Check
Test Objective

To verify that the Flask backend is running correctly.

Request
GET http://127.0.0.1:5000/
Observed Response
{
    "endpoint": "/predict",
    "message": "CIFAR-10 Flask Prediction API is running",
    "method": "POST"
}
Result

The Flask API responded successfully.

Status
PASS
14. Test Case 2: Flask API Prediction Using Postman
Test Objective

To verify that the Flask /predict endpoint can receive an image and generate a prediction.

Request
POST http://127.0.0.1:5000/predict
Request Body
Body → form-data
Key → image
Type → File

A Frog image was uploaded for testing.

Observed Response
{
    "confidence": 99.07,
    "predicted_class": "Frog"
}
Result

The Flask API successfully processed the image and returned a prediction.

Status
PASS
15. Test Case 3: Streamlit Frog Image Prediction
Test Objective

To verify communication between the Streamlit frontend and Flask backend.

Input

A Frog image was uploaded through the Streamlit Image Prediction page.

Workflow
Streamlit
    ↓
HTTP POST Request
    ↓
Flask /predict
    ↓
CNN Model
    ↓
Prediction
    ↓
JSON Response
    ↓
Streamlit
Observed Result

The Streamlit application displayed:

Predicted Class: Frog
Confidence: 99.01%

The Flask API response was also displayed in the Streamlit interface.

The application displayed the successful workflow message:

Streamlit → Flask → CNN Model → Prediction workflow completed successfully.
Status
PASS
16. Test Case 4: Truck Image Prediction
Test Objective

To verify that the integrated system can process another CIFAR-10 image through the complete frontend-backend workflow.

Input

A Truck image was uploaded through the Streamlit frontend.

Process

The image was:

Uploaded through Streamlit.
Sent to the Flask API.
Preprocessed by Flask.
Passed to the CNN model.
Converted into a prediction.
Returned to Streamlit as a JSON response.
Observed Result

The prediction was generated and displayed dynamically in the Streamlit interface.

Status
PASS
17. Test Case 5: Empty Image Input
Test Objective

To verify that the application handles the situation where the user does not upload an image.

Input

No image was uploaded.

Expected Behaviour

The application should not send an invalid prediction request and should ask the user to upload an image.

Observed Behaviour

The Streamlit application displayed an information message asking the user to upload a JPG, JPEG, or PNG image.

Status
PASS
18. API Testing with Postman

The Flask API was independently tested using Postman before completing the frontend integration.

The prediction request used:

POST http://127.0.0.1:5000/predict

The request body was configured as:

Body → form-data
Key → image
Type → File

A Frog image was uploaded.

The API successfully returned:

{
    "confidence": 99.07,
    "predicted_class": "Frog"
}

This confirmed that the Flask backend and trained CNN model were functioning correctly.

19. Streamlit-Flask Integration Testing

After verifying the Flask API independently, the Streamlit frontend was connected to the Flask backend.

The complete workflow was successfully tested:

Streamlit Frontend
        |
        | HTTP POST
        v
Flask REST API
        |
        v
Image Preprocessing
        |
        v
CIFAR-10 CNN Model
        |
        v
Prediction
        |
        v
JSON Response
        |
        v
Streamlit Frontend

The Streamlit frontend successfully received the prediction from Flask and displayed it dynamically.

20. Test Summary
Test Case	Description	Result
Test 1	Flask API health check	PASS
Test 2	Flask prediction using Postman	PASS
Test 3	Streamlit Frog prediction	PASS
Test 4	Streamlit Truck prediction	PASS
Test 5	Empty image input	PASS
21. Results

The integrated application successfully established communication between the Streamlit frontend and Flask backend.

The application allows a user to upload an image through Streamlit.

The image is then sent to the Flask API using an HTTP POST request.

The Flask API preprocesses the image and passes it to the trained CIFAR-10 CNN model.

The model generates a prediction and confidence value.

The Flask backend returns the result in JSON format.

Streamlit receives the response and dynamically displays the prediction.

For the tested Frog image, the Streamlit application displayed:

Predicted Class: Frog
Confidence: 99.01%

The Flask API independently returned:

Predicted Class: Frog
Confidence: 99.07%
22. Observations

The following observations were made during testing:

The Flask backend successfully loaded the trained CNN model.
The Flask home endpoint successfully confirmed that the API was running.
The /predict endpoint successfully accepted image uploads.
Postman successfully communicated with the Flask API.
The Streamlit frontend successfully communicated with the Flask backend.
Images could be transferred from Streamlit to Flask.
Flask successfully performed image preprocessing.
The trained CNN model successfully generated predictions.
The prediction was returned to Streamlit in JSON format.
Streamlit dynamically displayed the predicted class and confidence.
The Flask API response could also be viewed directly in the Streamlit interface.
The application handled an empty image input appropriately.
Connection and timeout errors were handled by the Streamlit frontend.
23. Evaluation Criteria
23.1 Successful Integration

The Streamlit frontend was successfully integrated with the Flask backend using HTTP requests.

The frontend sends uploaded images to the Flask /predict endpoint and receives the prediction as a JSON response.

23.2 Real-Time Prediction Capability

The application performs prediction after an image is uploaded.

The image is transferred to the Flask backend, processed by the CNN model, and the prediction is returned to the Streamlit interface dynamically.

23.3 Application Reliability

The application was tested using multiple valid images and an empty-input case.

The Streamlit frontend also contains handling for connection errors, request timeouts, and unexpected API responses.

24. How to Run the Project
Step 1: Open the Project Folder

Open the following project folder in VS Code:

Task8_Streamlit_Flask_Integration
Step 2: Install Dependencies

Open a terminal inside the project folder and run:

python -m pip install -r requirements.txt
Step 3: Start Flask Backend

Open the first terminal and run:

python flask_api.py

The Flask API will run at:

http://127.0.0.1:5000

Keep this terminal running.

Step 4: Start Streamlit Frontend

Open a second terminal in the same project folder and run:

streamlit run app.py

The Streamlit application will start locally.

Step 5: Open Streamlit Application

Open the Streamlit URL shown in the terminal.

Navigate to:

Image Prediction
Step 6: Upload an Image

Upload a JPG, JPEG, or PNG image.

The Streamlit frontend will send the image to the Flask backend.

Step 7: View Prediction

The prediction result will be displayed in Streamlit.

The result includes:

Predicted class
Confidence
Flask API response
Integration status
25. Important Execution Note

The Flask backend must be running before using the image prediction functionality.

The correct execution order is:

1. Start Flask
       ↓
2. Start Streamlit
       ↓
3. Open Streamlit UI
       ↓
4. Upload Image
       ↓
5. Flask Processes Image
       ↓
6. CNN Generates Prediction
       ↓
7. Result Displayed in Streamlit
26. Conclusion

This task successfully integrated a Streamlit frontend with a Flask REST API for real-time deep learning inference.

The Streamlit application acts as the frontend where users can upload images.

The Flask REST API acts as the backend responsible for receiving the uploaded image, preprocessing it, loading the trained CIFAR-10 CNN model, and generating the prediction.

The prediction is returned from Flask in JSON format and displayed dynamically in the Streamlit frontend.

Testing using Postman confirmed that the Flask API could independently process an image and return a prediction.

Further integration testing confirmed successful communication between Streamlit and Flask.

The completed system demonstrates:

Successful frontend-backend integration
HTTP-based image transfer
Real-time deep learning inference
JSON-based API communication
Dynamic prediction display
Basic error handling
Application reliability through testing

Therefore, the Task 8 implementation successfully demonstrates the integration of a Streamlit frontend with a Flask backend for a real-time CIFAR-10 deep learning prediction application.