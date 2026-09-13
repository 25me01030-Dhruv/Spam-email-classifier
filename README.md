# Spam-email-classifier

## 📊 Model Performance

Several machine learning models were evaluated for the spam classification task.

| Model | Accuracy | Precision |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayse | 96.71% | 100% |
| Gaussian Naive Bayse | 87.62% | 52.31% |
| **Bernoulli Naive Bayse** | **98.25%** |**100%** |

### 🏆 Best Performing Model

The **Bernoulli Naive Bayse algorithm** achieved the highest classification accuracy of **98.25%** when the TFIDF vectorizer was used.

The trained model was serialized and integrated with the Streamlit application for real-time spam classification.
