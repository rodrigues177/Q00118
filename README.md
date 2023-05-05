# Asteroid Classification

### Members
#### Tiago de Sousa Rodrigues - Q00118
#### Yeo Shi Lee Tan - E13329


## Introduction
To **gain insights into the characteristics** of asteroids that could potentially impact Earth and to analyze this data and identify patterns and trends that can **inform recommendations for monitoring and preventing potentially hazardous asteroid impacts**.

## Methods
Check Balance of Dataset:
* Imbalanced
* 5x more non-hazardous asteroids than hazardous asteroids
* Important to know so that we can train our machine learning models to take this into account

![Balance](/images/ML_Balance.png)

Pre-Processing Data:
* Normalized the dataset
* Removed same features of differing units
* Removed features regarding identification/timing
* Important to know so that we can reduce processing time when training model

![Distribution](/images/ML_Distribution.png)
  
Correlation:
* Conducted a heatmap and pairplot to see correlation
* Important to know the relationships amongst the variables
  
![Heatmap](/images/ML_Heatmap.png)
  
We found three main correlated groups (in descending order):
* Jupiter Tisserand Invariant, Mean Motion, Aphelion Distance, Orbital Period, Semi Major Axis (~0.9)
* Eccentricity, Aphelion Distance (~0.7)
* Absolute Magnitude, Estimated Diameter in Km (max) (~0.6)
 
![Pairplot](/images/ML_Pairplot.png)
  
Machine Learning Models:
 


## Experimental Design
**Permutation Importance:**
* Defined to be the decrease in a model score when a single feature value is randomly shuffled
* Purpose is to see which feature in the model is most important in determining whether an asteroid is hazardous or not
* The higher the score of permutation importance, the more important the feature is in the model

## Results
The **most important features** are, in descending order:
* Minimum Orbit Intersection, with a score of 0.223
* Absolute Magnitude, with a score of 0.176

![Permutation Importance Results](/images/Permutation_Importance_Results.png)

This can be attributed to the fact that as stated from the Center for Near Earth Object Studies website, "Potentially Hazardous Asteroids (PHAs) are currently defined based on parameters that measure the asteroid's potential to make threatening close approaches to the Earth. Specifically, all asteroids with an Earth Minimum Orbit Intersection Distance (MOID) of 0.05 au or less and an absolute magnitude (H) of 22.0 or less are considered PHAs.". Our results align with this such that the two main defining features of our model to whether an asteroid is hazardous or not are the minimum orbit intersection and absolute magnitude.

## Conclusions
