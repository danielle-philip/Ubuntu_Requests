import os
import requests

def fetch_image():
    # 1. Ask the user for an image URL
    url = input("Enter the image URL: ")

    # 2. Create directory for storing images
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # 3. Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # 4. Extract filename from URL or generate one
        filename = url.split("/")[-1]
        if not filename:  # if no filename, generate one
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # 5. Save the image in binary mode
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"✅ Image fetched successfully!\nSaved as: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Could not fetch the image. Reason: {e}")

if __name__ == "__main__":
    fetch_image()
