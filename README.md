# Spam mail classifier

## 📊 Model Performance

Several machine learning models were evaluated for the spam classification task.

| Model | Accuracy | Precision |
|---|---:|---:|
| Multinomial Naive Bayes | 96.71% | 100% |
| Gaussian Naive Bayes | 87.62% | 52.31% |
| **Bernoulli Naive Bayes** | **98.25%** | **100%** |

### 🏆 Best Performing Model

The **Bernoulli Naive Bayes** algorithm achieved the highest classification accuracy of **98.25%** with a **TF-IDF Vectorizer**, while maintaining **100% precision**.

The trained model was serialized and integrated with the **Streamlit** application for real-time spam classification.
