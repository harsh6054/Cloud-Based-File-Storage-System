#  Cloud File Storage App (AWS S3 + Flask)

##  Project Overview
This project is a **web-based cloud file upload system** built using **Flask (Python)** and **AWS S3**.  
It allows users to upload files through a simple web interface, and the files are stored securely in an S3 bucket.

---

##  Features
-  Upload files to AWS S3
-  Simple web interface using Flask
-  Styled UI with CSS
-  Real-time upload status message
- Cloud-based storage system

---

##  Technologies Used
- Python 3
- Flask
- AWS S3 (boto3)
- HTML, CSS

---

##  Project Structure

file_storage_app/
│
├── app.py # Main Flask application
└── README.md # Project documentation


---

##  Setup Instructions

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/cloud-file-storage.git
cd cloud-file-storage
```
### 2️⃣ Install Dependencies
```bash
pip3 install flask boto3
```

### 3️⃣ Configure AWS Credentials
```bash
Option 1: IAM Role (Recommended for EC2)

Attach a role with:

AmazonS3FullAccess
Option 2: Access Keys
aws configure

Enter:

AWS Access Key
AWS Secret Key
Region: ap-south-1
```

### 4️⃣ Update Bucket Name
```bash
Open app.py and update:

S3_BUCKET_NAME = 'your-bucket-name'
```

### 5️⃣ Run the Application
```bash
python3 app.py
```

### 6️⃣ Access in Browser
```bash
http://<your-ec2-public-ip>:5000
🔐 Required Permissions

Make sure your IAM role/user has:

{
  "Effect": "Allow",
  "Action": ["s3:PutObject"],
  "Resource": "arn:aws:s3:::your-bucket-name/*"
}
```

