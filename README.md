PARKINSON DISEASE DETECTOR
----
***
### What is Parkinson's Disease?
Parkinson's disease is a brain disorder that leads to shaking, stiffness, and difficulty with walking, balance, and coordination. Parkinson's symptoms usually begin gradually and get worse over time. As the disease progresses, people may have difficulty walking and talking.

![Image](/img/parkinson1.jpg)
Format: ![](url)

### What are the symptoms?
*Symptoms of PD vary from person to person, as does the rate of progression. A person who has Parkinson's may experience some of these more common "hallmark" symptoms:*

* Bradykinesia - slowness of movement, impaired dexterity, decreased blinking, drooling, expressionless face.
* Tremor at rest - involuntary shaking that decreases with purposeful movement. Typically starts on one side of the body, usually the hand.
* Rigidity - stiffness caused by involuntary increase in muscle tone.
* Postural instability - sense of imbalance. Patients often compensate by lowering their center of gravity, which results in a stooped posture.

***
So to predict if a person is affected by parkinson's disease,it is enough to check if the person is having the above symptoms.

## DATASET
***
The data in the datasets is in the form of:


**Dataset is delimited as CSV values as follows;**
* X ; Y; Z; Pressure; GripAngle; Timestamp; Test ID
**Test ID:** 
* 0: Static Spiral Test ( Draw on the given spiral pattern)
* 1: Dynamic Spiral Test ( Spiral pattern will blink in a certain time, so subjects need to continue on their draw)
* 2: Circular Motion Test (Subjectd draw circles around the red poin

--------------------
*The data contains hand-drawn spirals of static,dynamic and circular tests*
The dataset contains highly **imbalance data** i.e. of 15 healthy individuals and 62 parkinson affected people.
***
## Remodelling DATA
***
* The dataset consists of text-files of each individual 
* We created a csv file from the text_files using **datafile.py** which you can check in my repo
***

# Model Building:
***
 From the symptoms of Parkinsons's disease 
 **Rigidity**.**Bradykinesia**,**Tremor**   *The pressure and grip angle made by the person while drawing would help find out these symptoms dr/dt and dr/dθ  would help for rigidity symptom and time taken to draw wii differ from healthy person to parkinson affected person* 
### Feature Engineering
*We have chosen all 9 features namely mean values of Pressure,Grip angle,Time-taken,state(test-type), both mean and std values fordr/dt,dr/dθ and maximum radius of spiral*
**We built our model by using both Logistic regression and Random Forest Classifier**
***




***
**The Team:**
* P.Sai Teja Reddy
* P.Manikanta
* B.Trinadh Reddy


**Mentor:**
* Rakesh sir,
* SEEE department,
* SASTRA UNIVERSITY
***
