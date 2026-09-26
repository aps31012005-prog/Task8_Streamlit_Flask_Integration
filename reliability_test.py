import requests
import time
import statistics

# ==============================
# Configuration
# ==============================

API_URL = "http://127.0.0.1:5000/predict"
IMAGE_PATH = "../test_images/test_image.jpg"

# Number of requests to test
TOTAL_REQUESTS = 20

successful_requests = 0
failed_requests = 0
response_times = []

print("Starting reliability test with 20 prediction requests...")
print()

# ==============================
# Reliability Test
# ==============================

for i in range(1, TOTAL_REQUESTS + 1):

    try:
        # Open image
        with open(IMAGE_PATH, "rb") as image_file:

            files = {
                "image": image_file
            }

            # Start timer
            start_time = time.perf_counter()

            # Send request to Flask API
            response = requests.post(
                API_URL,
                files=files,
                timeout=30
            )

            # End timer
            end_time = time.perf_counter()

            response_time = end_time - start_time
            response_times.append(response_time)

        # Check response
        if response.status_code == 200:

            try:
                result = response.json()

                if result.get("success") is True:
                    successful_requests += 1

                    print(
                        f"Request {i}/{TOTAL_REQUESTS} - "
                        f"Success ({response_time:.2f}s)"
                    )

                else:
                    failed_requests += 1

                    print(
                        f"Request {i}/{TOTAL_REQUESTS} - "
                        f"Failed ({response_time:.2f}s)"
                    )

            except ValueError:
                failed_requests += 1

                print(
                    f"Request {i}/{TOTAL_REQUESTS} - "
                    f"Failed: Invalid JSON ({response_time:.2f}s)"
                )

        else:
            failed_requests += 1

            print(
                f"Request {i}/{TOTAL_REQUESTS} - "
                f"Failed - HTTP {response.status_code} "
                f"({response_time:.2f}s)"
            )

    except Exception as e:

        failed_requests += 1

        print(
            f"Request {i}/{TOTAL_REQUESTS} - "
            f"Failed - {str(e)}"
        )


# ==============================
# Calculate Metrics
# ==============================

success_rate = (
    successful_requests / TOTAL_REQUESTS
) * 100

failure_rate = (
    failed_requests / TOTAL_REQUESTS
) * 100

if response_times:
    average_response_time = statistics.mean(response_times)
else:
    average_response_time = 0


# ==============================
# Display Results
# ==============================

print()
print("======================================")
print("       RELIABILITY TEST SUMMARY")
print("======================================")

print(f"Total requests tested : {TOTAL_REQUESTS}")
print(f"Successful requests   : {successful_requests}")
print(f"Failed requests       : {failed_requests}")
print(f"Success rate          : {success_rate:.2f}%")
print(f"Failure rate          : {failure_rate:.2f}%")
print(
    f"Average response time : "
    f"{average_response_time:.2f} seconds"
)

print("======================================")

if failed_requests == 0:
    print("Reliability test completed successfully!")
else:
    print("Reliability test completed with failures.")