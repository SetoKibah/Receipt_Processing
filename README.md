# Receipt OCR

This project is a Python application that uses Optical Character Recognition (OCR) to extract and process information from receipts.

## Description

The application takes an image of a receipt as input. It then uses the OpenCV library to convert the image to grayscale and apply a binary threshold, which helps to improve the accuracy of the OCR process.

The Tesseract OCR tool is then used to extract text from the image. The extracted text is split into lines, and each line is checked for the presence of a dollar sign ("$"). Lines containing a dollar sign are assumed to represent itemized charges on the receipt, and are added to a list of receipt items.

The final output of the application is a list of the itemized charges on the receipt.

In future implementations, this will process the information gleaned from the receipt and arrange it neatly in a database, separating grocery and non-grocery expenses in a dataframe, all organized by date that can be recaleld and tracked for performance metrics.


## Usage

To use this application, run the `main.py` script with a receipt image as input. The application will print a list of the itemized charges on the receipt.

```bash
python main.py