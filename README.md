Due to Github Rich Text conversion issues, the Model Run notebook for the **Seizure Prediction and Identification Final Conclusions** notebook above is at the following NBViewer: 
https://nbviewer.org/github/eipiisneg1/seizure_prediction_model/blob/07c8f76923ccb8f442810c6c01d9cda74f1d8b3a/cap2_model_runs.ipynb

# **Summary for the Seizure Prediction and Identification Final Conclusions notebook**

Born with Ohtahara Syndrome, Cortical Dysplasia, and after donating half her brain to science, my daughter drove me to learn how to model such complicated processes via mathematics, python, and data science. 

This pursuit began when I read Epilepsy is related to the same class of mathematical problems that would win a Clay Mathematics Institute million dollar prize for EXISTENCE AND SMOOTHNESS OF THE NAVIER–STOKES EQUATION. 

While the Navier-Stokes Equation is in $R^2 or R^3$, Epilepsy, and life in general, would exist on the continuem in possibly $R^\inf$. This last sentence come from page 10 in Steven Strogatz's phonomenal book: Nonlinear Dynamics and Chaos. 


Can simple modeling techniques be used to predict seizures?
Can changes in electrical output indicate a patient's so-called "aura?" An aura is when the patient can feel something off and knows a seizure is coming. 

Using a variety of models, including supervised, unsupervised, Tensorflow 2 neural networks and LSTM models, I attempt to predict seizures from a patient's baseline and in the process, I show this can't be done because, in my opinion, seizure prediction falls into the mathematical theory of Chaos, so can't be predicted by definition. 

However, I discovered I was asking the wrong question and find a simple and effective strategy using python, Fast Fourier Transforms, and unsupervised clustering algorithms. 

Predicting the seizure in advance proved impossible, but there were...

#### **Bonus Insights Emergent from the Analysis:**
1. Clustering provides a means to simplify Epilepsy diagnoses.
2. Fast Fourier Transforms and a patient's baseline can be used to alert hospitals and patient families a seizure is imminent
