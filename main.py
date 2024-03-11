import pytesseract
import cv2
import pandas as pd
import sqlite3
#import dateparser


# Set path for pytesseract (will need to change for different computers potentially if not set to PATH)
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to process receipt image and extract text
def process_receipt(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Clean the image using OpenCV
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


    # Use Tesseract OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(threshold_img)
    
    # Separate the text into lines and print the lines
    lines = extracted_text.split("\n")
    
    # Create a list to store the receipt items
    receipt_item_list = []

    for line in lines:
        # Remove any leading or trailing white spaces
        if line.strip() != "":
            # print the line and the index of the line
            #print(f"Line {lines.index(line)}: {line.strip()}")

            # print lines that have a "$" in them
            if "$" in line:
                #print(line.strip())
                # add lines to a list
                receipt_item_list.append(line.strip())

    print('Receipt Items:')

    # Iterate through indexes 1-3 of the receipt item list
    for i in range(1, 4):
        print(receipt_item_list[i])
        # Separate the item from the price
        item = receipt_item_list[i].split("$")[0]
        price = receipt_item_list[i].split("$")[1]
        print(f"Item: {item} Price: {price}")


    # Print the extracted text
    #print(extracted_text)

# Path to the receipt image
receipt_image_path = r"C:\Users\Bradley\Downloads\generated-walmart-receipt-430x1024.jpg"

# Process the receipt image
process_receipt(receipt_image_path)