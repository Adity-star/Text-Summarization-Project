# Text Summarizer Project

An advanced Natural Language Processing (NLP) application designed to automatically generate concise summaries from large blocks of text. With the ever-growing amount of information online and in documents, this project provides an efficient solution to extract key insights from text quickly and accurately.

![website](https://github.com/user-attachments/assets/d0cc1b5a-e0a0-4a22-90c1-16999af764a5)

---

## 📖 Description

The **Text-Summarizer-Project** is a versatile system capable of summarizing articles, research papers, news reports, and other lengthy documents. It uses state-of-the-art NLP techniques, combining extractive and abstractive summarization methods to produce concise and meaningful summaries.

Key features include:  
- **Text Preprocessing:** Cleans input text, removes noise, punctuation, and stopwords.  
- **Sentence Extraction:** Identifies key sentences representing main ideas.  
- **Semantic Understanding:** Leverages semantic analysis to comprehend meaning and relevance.  
- **Summarization Techniques:** Supports both extractive and abstractive summarization.  
- **Length Control:** Users can adjust summary length (short or comprehensive).  
- **User Interface:** Simple interface for text input and summary output.  

**Benefits:**  
- Time-saving by quickly condensing long texts.  
- Helps researchers, students, and professionals extract key insights.  
- Useful for journalists, content creators, and language learners.  
- Can be integrated into search engines or knowledge management systems.  

---

## 📂 Dataset

**SAMSum Dataset** ([Hugging Face Link](https://huggingface.co/datasets/samsum))  

- 16k messenger-like conversations with human-written summaries.  
- Covers dialogues between 2+ speakers, varying in style (informal, semi-formal, formal) with slang, emoticons, and typos.  
- Training/Validation/Test split:  
  - Train: 14,732  
  - Validation: 818  
  - Test: 819  

**Example Instance:**  
```json
{
  "id": "13818513",
  "summary": "Amanda baked cookies and will bring Jerry some tomorrow.",
  "dialogue": "Amanda: I baked cookies. Do you want some?\r\nJerry: Sure!\r\nAmanda: I'll bring you tomorrow :-)"
}
```
### Fields

- **dialogue**: Text of conversation  
- **summary**: Human-written concise summary  
- **id**: Unique identifier

---
## 🧠 Model Information

**PEGASUS (Google AI)** – A state-of-the-art transformer-based model for abstractive summarization.

### Key Features:

- Transformer-based neural network  
- Trained on large datasets of text and code  
- Generates fluent and informative summaries  
- Outperforms other summarization models on various tasks

### 📝 Notes on Training

- Initial training with 1 epoch due to low computing power  
- Achieved accuracy was low; further iterations are planned to improve performance
---

## 🚀 Key Features & Functionality

- Preprocessing, cleaning, and noise removal  
- Extractive and abstractive summarization techniques  
- Semantic sentence ranking and selection  
- Adjustable summary length  
- Robust MLOps framework using MLflow and DVC  
- Deployment-ready FastAPI service with Docker and AWS integration

---
## 📈 Results

| Metric    | Score |
|-----------|-------|
| ROUGE-L   | 44.1  |
| ROUGE-2   | 24.5  |
| Baseline Δ| +2    |

Outperforms standard baselines and demonstrates the effectiveness of hybrid PEGASUS-based summarization.

---
## 🛠️ Tech Stack

- **ML/DL:** Hugging Face Transformers, PEGASUS  
- **MLOps:** MLflow, DVC, Docker  
- **Backend/Deployment:** FastAPI, AWS EC2, S3, ECR  
- **CI/CD:** GitHub Actions
---
## 💻 How to Run

1. Clone the repository:

```bash
git clone https://github.com/praj2408/Text-Summarizer-Project.git
cd Text-Summarizer-Project
```
2.  create a conda environment.
 ```bash
conda create -n summary python==3.8 -y
conda activate summary
```
3. Install dependencies.
```bash
pip install -r requirements.txt
```
4. Run the FastAPI app locally.
```bash
python app.py
```
5. Open your browser at `http://localhost:8000` (or specified port) to interact with the service.

---
## ☁️ AWS CICD Deployment with GitHub Actions

### 1. AWS Setup:
  - Create IAM user with:  
    - EC2 access  
    - ECR (Elastic Container Registry) access

- Assign policies:  
  - `AmazonEC2FullAccess`  
  - `AmazonEC2ContainerRegistryFullAccess`

### 2. ECR Deployment:

  - Create an ECR repository.  
  - Build Docker image of the app:
  ```bash
  docker build -t text-summarizer .
  ```
  - Push Docker image to ECR.
### 3. Ec2 Deployment.
- Launch an EC2 instance
- Install Docker on EC2
```bach
  curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
- Pull the Docker Image.
- Launch the Docker container on EC2.

### GitHub Actions Integration

- Configure secrets:  
  - `AWS_ACCESS_KEY_ID`  
  - `AWS_SECRET_ACCESS_KEY`  
  - `AWS_REGION`  
  - `AWS_ECR_LOGIN_URI`  
  - `ECR_REPOSITORY_NAME`

- Automate deployment with CI/CD workflow.

---
## 🌟 Contributing

Contributions are welcome! Feel free to fork the repository, raise issues, and submit pull requests.

---

## 📝 License

This project is licensed under the [MIT License.](https://github.com/Adity-star/Text-Summarization-Project/tree/main#)
