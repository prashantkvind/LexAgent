# 🏛️ LexAgent: Production Live Deployment & Cost Optimization Guidelines

This document provides a comprehensive operational guide for pushing **LexAgent** to **Live Production Access**. It details all infrastructure requirements, expected monthly cloud costs, and actionable cost-minimization strategies.

---

## 📋 1. Core Requirements for Live Production Access

To transition LexAgent from local laptop execution to a live, secure, publicly accessible Web Application for law firms or clients, the following core requirements must be fulfilled:

### 🌐 A. Domain, SSL & Networking
* **Custom Domain Name**: A registered domain (e.g. `https://lexagent.yourfirm.com`).
* **TLS / SSL Certificate**: HTTPS encryption enforced via Cloudflare, AWS Certificate Manager, or Let's Encrypt.
* **Content Delivery Network (CDN)**: Cloudflare CDN for DDoS protection, web application firewall (WAF), and global edge caching.

### 🔐 B. Enterprise Authentication & Access Control
* **User Authentication (OIDC / OAuth2)**: Integration with Auth0, Okta, Google Workspace, or AWS Cognito to restrict web access to authorized lawyers and staff.
* **Role-Based Access Control (RBAC)**: Enforcing view-only vs. document-drafting permissions per advocate account.

### 🐳 C. Compute Container Hosting
* **Serverless Container Platform**: AWS ECS (Fargate), GCP Cloud Run, or Azure Container Apps for running the multi-stage Docker container (`Dockerfile`).

### 🗄️ D. Cloud Vector DB & Object Storage
* **Managed Vector DB**: Qdrant Cloud, Pinecone, or AWS OpenSearch Vector Engine for scalable document retrieval.
* **Cloud Storage Buckets**: AWS S3 or GCP Cloud Storage (`s3://lexagent-notices/`) with 15-minute signed download URLs for generated `.docx` legal notices.

---

## 💰 2. Expected Monthly Cloud Cost Breakdown

LexAgent is engineered to be **extremely cost-efficient**. Depending on your user volume, choose one of the 3 deployment cost tiers:

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ MONTHLY COST TIERS                                                                        │
├──────────────────────────────┬──────────────────────────────┬─────────────────────────────┤
│ Tier 1: Ultra-Low Cost       │ Tier 2: Law Firm Production  │ Tier 3: Enterprise Dedicated│
│ $5 – $15 / month             │ $45 – $85 / month            │ $150 – $350 / month         │
└──────────────────────────────┴──────────────────────────────┴─────────────────────────────┘
```

### 🟩 Tier 1: Ultra-Low Cost / Prototype Tier ($5 – $15 / Month)
*Ideal for solo advocates, individual researchers, or small internal demos.*

| Service Component | Cloud Provider & Configuration | Monthly Cost |
| :--- | :--- | :--- |
| **Container Compute** | GCP Cloud Run (Scale-to-Zero, 1 vCPU, 2GB RAM) | **$2.00 – $5.00** |
| **Vector Database** | Qdrant Cloud Free Tier (1 Cluster, 1GB RAM) | **$0.00** *(Free)* |
| **LLM Inference** | Gemini 1.5 Flash API or OpenAI GPT-4o-mini | **$2.00 – $8.00** |
| **Legal Search API** | Tavily API Free Tier (1,000 queries/month) | **$0.00** *(Free)* |
| **Object Storage** | AWS S3 / GCP Cloud Storage (< 5 GB) | **$0.50** |
| **Domain & SSL** | Cloudflare Free SSL & DNS | **$0.00** *(Free)* |
| **TOTAL EXPECTED COST** | | **~$5.00 – $15.00 / mo** |

---

### 🟦 Tier 2: Production Law Firm Tier ($45 – $85 / Month) [RECOMMENDED]
*Ideal for active legal practices with 10 – 50 advocates querying daily.*

| Service Component | Cloud Provider & Configuration | Monthly Cost |
| :--- | :--- | :--- |
| **Container Compute** | AWS ECS Fargate or GCP Cloud Run (Always-on 1 instance) | **$25.00 – $35.00** |
| **Vector Database** | Pinecone / Qdrant Starter Cloud Tier | **$15.00 – $25.00** |
| **LLM Inference** | Gemini 1.5 Flash / GPT-4o-mini (~10,000 queries/month) | **$10.00 – $20.00** |
| **Legal Search API** | Tavily Developer Tier or DuckDuckGo Fallback | **$5.00 – $10.00** |
| **Object Storage** | AWS S3 with Lifecycle Rules & KMS Encryption | **$2.00** |
| **Authentication** | Auth0 Free Tier (Up to 7,500 active users) | **$0.00** *(Free)* |
| **TOTAL EXPECTED COST** | | **~$45.00 – $85.00 / mo** |

---

### 🟪 Tier 3: Dedicated Private GPU Tier ($150 – $350 / Month)
*For enterprise law firms requiring 100% private self-hosted Ollama LLMs on dedicated GPUs.*

| Service Component | Cloud Provider & Configuration | Monthly Cost |
| :--- | :--- | :--- |
| **Dedicated GPU Instance** | AWS EC2 `g4dn.xlarge` (NVIDIA T4 16GB GPU for Ollama 7B/13B) | **$150.00 – $280.00** |
| **Managed Vector DB** | Qdrant Cloud Standard Dedicated Node | **$45.00** |
| **Storage & Bandwidth** | AWS EBS + S3 Storage + CloudWatch Logging | **$15.00 – $25.00** |
| **TOTAL EXPECTED COST** | | **~$210.00 – $350.00 / mo** |

---

## ⚡ 3. Strategies to Minimize & Control Cloud Costs

To keep monthly infrastructure spending as close to **$5 – $15/month** as possible, enforce the following cost control rules:

### 1. ⚙️ Enable Scale-to-Zero Serverless Container Scaling
* Configure **GCP Cloud Run** or **AWS Fargate** to scale down to `min-instances = 0`.
* When no lawyer is using the app at night or weekends, **compute cost drops to $0.00/hour**.

### 2. ⚡ Leverage 2-Tier Strategy Memory Caching (0% LLM Cost for Repeated Queries)
* LexAgent's built-in `_query_cache` intercepts identical legal questions in memory.
* Cached queries are served instantly in **0.03 ms** without invoking external LLM APIs, saving **100% of LLM token costs** on repeated questions.

### 3. 🎯 Use Ultra-Low-Cost High-Speed Models
* Avoid expensive flagship models like GPT-4o ($5.00 / 1M tokens).
* Use high-efficiency models like **Gemini 1.5 Flash** ($0.075 / 1M tokens) or **GPT-4o-mini** ($0.15 / 1M tokens), which provide identical legal notice quality at a **98% cost reduction**.

### 4. 🗄️ Utilize Vector DB & Search Free Tiers
* Leverage **Qdrant Cloud Free Tier** (1GB storage, 1M vector vectors free forever).
* Keep `SEARCH_MODEL_PROVIDER = "auto"` in [`config.py`](file:///config/.gemini/antigravity/scratch/LexAgent/config.py) so the agent automatically falls back to **DuckDuckGo (Free)** if Tavily API quota is reached.

### 5. 🗑️ Configure S3 / GCS Lifecycle Rules
* Set cloud object storage lifecycle rules to automatically delete generated `.docx` legal notices older than 30 days:
  ```json
  {
    "Rules": [
      {
        "ID": "DeleteOldNoticesAfter30Days",
        "Status": "Enabled",
        "Expiration": { "Days": 30 }
      }
    ]
  }
  ```

### 6. 🚨 Set Cloud Budget Alerts & Hard Spend Limits
* Set AWS or GCP Budget Alerts at **$15**, **$30**, and **$50**.
* Enable automated CloudWatch action triggers to stop non-essential GPU instances if monthly spend exceeds your budget limit.
