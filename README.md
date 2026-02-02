# smart E-commerce Customer Retention API

A machine learning-powered REST API built with FastAPI that predicts customer satisfaction levels and suggests immediate business actions (Discounts, Surveys, etc.) to improve retention.



## Key Features
- **Real-time Prediction:** Categorizes customers into 'Satisfied', 'Neutral', or 'Unsatisfied'.
- **Automated Business Logic:** Dynamically generates retention strategies (e.g., 20% discount for high-risk customers).
- **Data Validation:** Uses Pydantic for robust input data cleaning and validation.
- **Auto-Generated Docs:** Interactive API testing via Swagger UI.

##  Tech Stack
- **Backend:** FastAPI, Uvicorn
- **Machine Learning:** Scikit-learn, RandomForest, Pandas
- **Serialization:** Joblib
- **Language:** Python 3.9+

##  Business Logic
The API doesn't just predict; it prescribes actions:
| Prediction | Alert Level | Recommended Action |
| :--- | :--- | :--- |
| **Unsatisfied** | Critical | Send 20% Discount + Support Call |
| **Neutral** | Medium | Send Feedback Survey + 5% Discount |
| **Satisfied** | Normal | Maintain standard service |

##  Installation & Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/salimmessaad1/ecommerce-satisfaction-api.git](https://github.com/salimmessaad1/ecommerce-satisfaction-api.git)