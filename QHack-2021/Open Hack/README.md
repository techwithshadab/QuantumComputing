### Team Name: 

*qt*

### Project Description: 

<h3> Quantum-Aided Medical Image Diagnosis </h3>

#### Inspiration
Breast cancer is the most common form of cancer in women, and invasive ductal carcinoma (IDC) is the most common form of breast cancer. Accurately identifying and categorizing breast cancer subtypes is an important clinical task, and automated methods can be used to save time and reduce error.

<p align="center" width="400">
  <img src="../images/IDC.png"  />
</p>

### Dataset:

#### Context
Invasive Ductal Carcinoma (IDC) is the most common subtype of all breast cancers. To assign an aggressiveness grade to a whole mount sample, pathologists typically focus on the regions which contain the IDC. As a result, one of the common pre-processing steps for automatic aggressiveness grading is to delineate the exact regions of IDC inside of a whole mount slide.

#### Content
The original dataset consisted of 162 whole mount slide images of Breast Cancer (BCa) specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted (198,738 IDC negative and 78,786 IDC positive). Each patch’s file name is of the format: uxXyYclassC.png — > example 10253idx5x1351y1101class0.png . Where u is the patient ID (10253idx5), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-IDC and 1 is IDC.


### Source code: 

*[Code](https://github.com/shadab-entrepreneur/QuantumComputing/edit/main/QHack-2021/Open%20Hack/)*

### Resource Estimate: 

*A 1-2 paragraph written Resource Estimate, indicating how you expect to use the additional AWS credits, if awarded, to finish your Open Hackathon project.*
