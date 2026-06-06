
<img width="1693" height="741" alt="image" src="https://github.com/user-attachments/assets/f8dd5373-b186-4ba7-b49c-dc0ba8891cd5" />

# Credit Risk: Building a Probability of Default model with Databricks

## Objective

Build a Prediction of Default (PD) model for credit operations in order to infer their risk of default, defining a system that automatically trains the models, compares them and deploys newer models that perform better, making them available for user usage and user consumption of predictions in new operations. 


## Tools and Tech Used

Programming:

✅ Python & Spark (PySpark)

Technology:

✅ Google BigQuery;

✅ Databricks
  
  • DABs;
  
  • Databricks Connect (VS Code);
  
  • Mlflow;
  
  • Serving Endpoint;
  
  • Catalog & Jobs;
  
  • Service Principals;
  
  • Git folder;
  
  • And more.
  
✅ GitHub.


## The Model

Probability of Default (PD) models have well defined premisses defined by Regulators. In order to follow these rules, the interpretable Logistic Regression model (without regularization) was used to model the probability that the operation will default. Also, the features (inputs) of the model were designed to by dummy features. In order to do this, every feature (numerical and categorical) was put into bins according to their Weight of Evidence (WoE). Finally, the model had its probabilities calibrated using Platt's method. Defaulted operations are classified as the ops that have one of the following status descriptions: 

<img width="1138" height="355" alt="image" src="https://github.com/user-attachments/assets/39c3076c-e7fa-4003-a585-b98b8d3acf91" />


The final model in production had, on unseen data, a KS of 0.296 and a ROC AUC of 0.696 and 12 inputs, representing satisfatory performance in probability of default prediction:


<img width="1222" height="600" alt="image" src="https://github.com/user-attachments/assets/99795c78-35a3-4c66-899e-9a2a97843be0" />


## Business Usage of the Solution
