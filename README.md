# Email Sending API – FastAPI

### **Overview**
Build a simple, performant REST API using FastAPI that accepts a POST request to send an
email. Your implementation should parse incoming JSON, validate it, and deliver the message
via Gmail’s SMTP server without blocking the main event loop.

### API Endpoint
The API will be available at http://127.0.0.1:8000/send-email.


## 👨‍💻 Running Email Sending API

### 📥 Clone the Repository

```bash 
   git clone https://github.com/Hajiaga-Sadikhov/Email-Sending-API-FastAPI.git   
   cd Email-Sending-API-FastAPI
```

### Installation Dependencies
To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```


### Run the API

```bash
uvicorn main:app --reload
```
