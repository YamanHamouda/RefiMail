# Refimail ✉️✨

Refimail is a smart writing assistant that transforms the tone and clarity of your emails. Whether you're writing something formal, casual, emotional, or playful, Refimail helps you express yourself the way you intend.

---

## 🧠 What It Does

Paste your rough email draft into Refimail, choose a tone that fits your message, and get back a reworded version that better matches your intent. It’s built for everyday communication and lets you quickly shift how your message comes across.

---

## 💻 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python using Flask
- **Cloud Services**:
  - AWS S3 for storing email input and output
  - AWS Lambda to process and rewrite messages
  - Amazon Bedrock to apply tone adjustments using a anthropic claude

---

## 🔄 How It Works

1. You enter a message and select a tone (like Formal, Friendly, Playful, or Childish).
2. The JavaScript sends the tone and email to the backend.
3. The Flask backend uploads your message and selected tone to an S3 bucket.
4. A Lambda function is triggered when the file is uploaded.
5. From the Lambda function, the message and tone are sent to Amazon Bedrock in a defaulted prompt.
6. The rewritten message is saved in an output S3 bucket.
7. The email is extracted from the S3 bucket in the Python backend and sent to the front end
8. Then the new refined email is displayed for the user.
