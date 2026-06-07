
<img width="1693" height="741" alt="image" src="https://github.com/user-attachments/assets/f8dd5373-b186-4ba7-b49c-dc0ba8891cd5" />

# Credit Risk: Building a Probability of Default model with Databricks

## Objective

Build a Probability of Default (PD) model for credit operations in order to infer their risk of default, defining a system that automatically trains the models, compares them and deploys newer models that perform better, making them available for user usage and user consumption of predictions in new operations.


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


In Databricks, the training and deploying pipeline are deployed using DAB and follow the logic below:

<img width="1242" height="352" alt="image" src="https://github.com/user-attachments/assets/7bcd8b6d-e1e0-485e-931f-c934ddb71620" />


After training a new model, we check if it is performing better than the one already in production on new data. If yes, the production model is updated and deployed to the serving endpoint in Databricks.


## Business Usage of the Solution

The final model is available to be used within Databricks (loading the model and applying predictions) directly:


<img width="615" height="530" alt="image" src="https://github.com/user-attachments/assets/ac11fbcc-eab2-4ef7-a0b9-add9381001dd" />


And it is also available through a deployed serving endpoint in Databricks:


<img width="1012" height="727" alt="image" src="https://github.com/user-attachments/assets/361b38ad-ae84-4027-aa06-5584ba5334dc" />


In order to test the deployed model in a situation likely to happen in a financial industry, a ETL was built that extracts new credit operations and applies the model in production to predict their probabilities of default.

<img width="1576" height="770" alt="image" src="https://github.com/user-attachments/assets/a1b56bfe-b3cf-40b5-869b-7b8a569dd43a" />

The code, which was built in a noteboos, can be found in the folder etls/. In it, the approach we had was to use the model directly to apply the predictions, and not the serving endpoint. Every attempt to connect to it to apply the prediction resulted in errors associated with deficiencies of the Free Edition of Databricks (problems regarding using APIs in notebooks, from the experience we had). The output table here (mlops_prd.dbk_credit_analytics.operations_credit_risk) had the final operations with their probability of default:

<img width="1875" height="847" alt="image" src="https://github.com/user-attachments/assets/00d992ff-c1c5-471a-a8a9-850b4d98ef3f" />


## Conclusion

The model and pipelines built in Databricks, that assess the risk (probability of default) of credit operations, had satisfatory results (ROC AUC of 0.69 and KS of 0.29) considering the simplistic approaches taken here, for example number of features chosen. The model deployed in Databricks is available for the business to assess the operations' risk, with a ETL already built that automatically classifies each new operation. The training pipeline can also be ran automatically with a pre-defined frequency, and its current logic will only update the model in production if a newly trained model, on new data, outperforms the model already in production. 
