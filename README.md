# 👩‍⚕️ Medical Data Extraction 📄

Medical Data Extraction is an end-to-end OCR-powered system designed to automatically extract structured information from Patient Records and Prescription PDFs.

This project combines Computer Vision, Natural Language Processing, and Backend APIs to digitize healthcare documents, making them searchable, editable, and storable in a database.

✨ Key Highlights:

📄 OCR-based Text Extraction → Uses Tesseract + OpenCV to preprocess and extract text from medical PDFs.

🧠 Regex Parsing & NLP → Converts raw OCR text into structured fields (e.g., Name, Phone, Medicines, Dosage).

⚡ FastAPI Backend → High-performance API to handle extraction requests and database operations.

🎨 Streamlit Frontend → Interactive UI to upload files, review extracted data, and verify before saving.

🗄️ MySQL Database Integration → Patient and Prescription details are stored securely using Stored Procedures.

🧪 Unit Testing with Pytest → Ensures reliable parsing and backend functionality.

🚀 With this project, manual form-filling and data entry in healthcare can be reduced significantly, making insurance claims, patient records, and prescription management more efficient and error-free.

## Overview

1. [What is OCR?](#a1)
2. [Introduction to Project](#a2)
3. [Project Execution Steps](#a3)
4. [Code Walkthrough](#a4)
5. [What did I learn through this project?](#a5)
6. [Challenges Faced](#a6)
7. [Directory Structure](#a7)
8. [If you are cloning this repository](#a8)
9. [🚀 Update 1: Store data into MySQL DB after verification in UI](#a9)

## <a name="a1">1. What is OCR?</a>

OCR stands for Optical Character Recognition. It's a technology that enables the conversion of different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. Essentially, OCR software identifies text within images or scanned documents and converts it into machine-readable text.

Machine learning and AI play significant roles in OCR technology. Machine learning (ML) powers OCR to turn images into text. ML algorithms like convolutional neural networks (CNNs) are trained on massive datasets to recognize characters. ML also helps extract key features from images and utilizes language models to understand context and improve accuracy, especially for ambiguous characters. OCR systems continuously learn and adapt to specific domains and languages through ML, ensuring ever-better performance.

Here are some common applications and domains where OCR is used:

1. **Document Digitization**: OCR is extensively used to convert scanned documents, PDFs, and images into editable and searchable text. This is useful in offices, libraries, and archives for digitizing large volumes of documents for easier storage, retrieval, and sharing.

2. **Data Entry Automation**: OCR automates data entry processes by extracting text from documents such as invoices, receipts, and forms. This saves time and reduces errors associated with manual data entry tasks.

3. **Banking and Finance**: OCR is employed in banking for reading checks, processing forms, and extracting information from financial documents. It facilitates faster processing of transactions and improves accuracy in tasks like check reading and automated form filling.

4. **Healthcare**: In healthcare, OCR assists in digitizing medical records, prescriptions, and patient forms. It enables quick access to patient information, enhances data accuracy, and streamlines administrative tasks in hospitals and clinics.

5. **Retail and E-commerce**: OCR is used in retail for tasks like inventory management, barcode scanning, and automatic price recognition. In e-commerce, it helps extract product information from images and catalogs, improving searchability and customer experience.

6. **Automated License Plate Recognition (ALPR)**: OCR technology is utilized in ALPR systems for reading license plates on vehicles. It's employed in various applications such as traffic management, toll collection, parking enforcement, and security surveillance.

7. **Translation Services**: OCR assists in language translation by converting printed text from one language into machine-readable text, which can then be processed by translation software. This enables the automatic translation of documents and websites.

8. **Accessibility**: OCR helps individuals with visual impairments by converting printed text into accessible formats such as audio or Braille. It allows them to access information from printed materials like books, documents, and signs.

9. **Legal and Compliance**: In legal and compliance domains, OCR is used for searching and analyzing large volumes of legal documents, contracts, and regulatory filings. It facilitates faster retrieval of relevant information and aids in compliance monitoring.

10. **Education**: OCR is employed in educational institutions for tasks like grading exams, digitizing textbooks, and converting handwritten notes into editable text. It assists in creating accessible learning materials and automating administrative processes.

## <a name="a2">2. Introduction to Project</a>

> Whenever we go to hospital, we always fill up some kind of forms and our medical history is created using those forms, prescriptions, test reports. Sometimes, this medical history is used for other purposes like claiming health insurance etc

> Health Insurance company might receive thousands of such documents from multiple sources and creating a record of useful information from customers medical history is a very cumbersome task and requires huge manpower. And hence this kind of tasks can be sped up using OCR technology.

For this project we have two types of Medical Documents.

1. Patient Medical Record
2. Prescription

We are going to extract some important fields from these documents.
![4.jpg](4.jpg)

### Why this project?

Though I have been learning Data Science, then why am I doing this project? Mainly there are 3 reasons. 01. OCR is a subset of Computer Vision. OCR can be used in an NLP project like summarizing text using LLM. 02. This project involves very fundamental concepts of Python programming like OOP and Modular programming which are industry best practices. 03. Also this project involves creation of a backend server using FastAPI, which is known for its performance and many world-renowned companies such as Uber, Netflix and Microsoft use FastAPI to build their applications.

## <a name="a3">3. Project Execution Steps</a>

- **Step 1:** Convert pdf to image using `pdf2image` library
- **Step 2:** Preprocess the image (Apply `adaptive thresholding and binarization using OpenCV2`)
- **Step 3:** Extracting text from image by passing it through `tesseract OCR engine`
- **Step 4:** Finding useful information from text using `RegEx` and returning in JSON format
- **Step 5:** Creating a `FastAPI backend server` which serves data extraction requests by accepting a pdf_file, file_format and returning a JSON object.
- **Step 6:** To create a Demo of `frontend UI using Streamlit` and connect it with our FastAPI server using Python Requests module.
  ![Project Execution Steps](8.jpg)

## <a name="a4">4. Code Walkthrough</a>

Explore notebooks and source code of this project.

- Notebook 1: [Prescription_parser]
- Notebook 2: [Patient_details_parser]
- Backend: [Source code directory]


## <a name="a5">5. What did I learn through this project?</a>

- How to use OCR for real world projects and key image processing concepts like thresholding using `OpenCV2`.
- Polished up my Python coding skills by using `OOP, code refactoring and modular programming`.
- Setting up of a backend server using `FastAPI` framework.
- Unit testing using `Pytest`.
- How to use `Postman` for API testing.
- I could connect Streamlit frontend with FastAPI backend server using `Python requests` module.

## <a name="a6">6. Challenges faced during this project</a>

- In adapative thresholding, it requires lot of trial and error to reach optimum values of block size and constant.
- Pytest is not properly integrated with VSCode.
- Also I faced path related errors during unit testing even in PyCharm.
- When creating streamlit app, there are very few practical instructions available on internet for connecting it with a backend server and sending files across.

## <a name="a7">7. Directory Structure of Project</a>

```
medical-data-extraction
│   .gitignore
│   README.md
│   requirements.txt
│
├───backend
│   │
│   ├───resources
│   │   │
│   │   ├───patient_details
│   │   │       pd_1.pdf
│   │   │       pd_2.pdf
│   │   │
│   │   └───prescription
│   │           pre_1.pdf
│   │           pre_2.pdf
│   │
│   ├───src
│   │       extractor.py
│   │       main.py              //Fastapi Backend Server
│   │       parser_generic.py
│   │       parser_patient_details.py
│   │       parser_prescription.py
│   │       utils.py
│   │
│   ├───mysql_scripts
│   │       queries.sql
│   │
│   ├───tests
│   │       test_prescription_parser.py
│   │
│   └───uploads
│
├───frontend
│       app.py              //Streamlit app
│
├───Notebooks
│       prescription_parser_01.ipynb
│       patient_details_parser_02.ipynb
│       RegEx_03.ipynb
│
└───reference
        tesseract_papar_by_google.pdf
```

## <a name="a8">8. If you are cloning this repository?</a>

- Install all dependancies from `requirements.txt`
- For `pdf2image` you need to [download `poppler`](https://github.com/belval/pdf2image?tab=readme-ov-file#how-to-install)
- Install Tesseract OCR Engine in your PC
  - [Tesseract installation instrution : Github](https://github.com/tesseract-ocr/tesseract#installing-tesseract)
  - [Tesseract windows specific instructions: Github](https://github.com/UB-Mannheim/tesseract/wiki)
- Set required PATHs as per your environment.
- Update: Now you will have to link you db for storing data. Python code updated accordingly, and script for creation of db table and SPs is uploaded in the repo.

## <a name="a9">9. 🚀 Update 1: Store data into MySQL DB after verification in UI</a>

- In the Streamlit UI I have kept a submit button but there was no any event listener for the button. Now I have integrated DB functionality and you can store the data on UI back into MySQL Database using Stored Procedures.
- In the directory `mysql_scripts`, you can find queries used for creation of table and stored procedures. In the `backend\scr` directory a new module `db_utils` added, where you can find code for how you can connect your database with python. In the `main.py` 2 new POST methods created for updating the db tables.

> In the UI, once you receive OCR output, you can modify it before saving to db.

![Patients Table](13.png)
![Prescriptions Table](14.png)
