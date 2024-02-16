# SHL2023
![](https://github.com/Therebe123/SHL2023/blob/main/cover.jpg)

The code of the team "WinGPT" from RUC participating in SHL2023.   

The project includes data preprocessing, feature extraction and model training.

**Python version: 3.11.3**

## Mainly used library
torch: 2.0.1

xgboost: 1.7.5

scikit-learn: 1.2.2

pandas: 2.0.1

numpy: 1.24.3

matplotlib: 3.7.1

## Overall information of the paper
### Title
Enhancing Locomotion Recognition with Specialized Features and Map Information via XGBoost

### URL
https://doi.org/10.1145/3594739.3610754

### Abstract
The goal of Sussex-Huawei Locomotion-Transportation (SHL) recognition challenge in 2023 is to recognize 8 modes of locomotion and transportation (activities) in a user-independent manner based on motion and GPS sensor data. The main challenges of this competition are sensor diversity, timestamp asynchrony, and the unknown positions of sensors in the test set. We, team "WinGPT", constructed special features like velocity from the raw dataset, and extracted various features from both time domain and frequency domain. Additionally, this article calculated the distance between users and the nearest places or roads as a feature using map information obtained from OpenStreetMap. We used a dataset with a total of 202 features to train classical machine learning models such as decision tree, random forest, LightGBM, and XGBoost, among which the XGBoost model performed the best, achieving a macro f1 score of 78.95% on the validation set. Moreover, based on our predictions, we determined that the sensor location in the test set was positioned on the hand. Through a post-processing procedure applied to the model, we ultimately achieved a final macro F1 score of 90.86% on the validation set from the hand.

## Competition results
A macro F1 score of 85.6% on the test set. 
Ranked seventh overall and third in the ML group.
