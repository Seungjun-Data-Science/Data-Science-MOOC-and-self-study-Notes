
## Multiple Featues of one Input

### Polynomial Regression

<img src='polynomial regression.JPG'>

### Modeling Seasonality

E.g. x = Month , y = House Prices

- On average, house prices tend to increase with time
- Most houses listed in summer + good houses sell quicky
- Few homes listed in Nov./Dec. + Transactions often leftover inventory or special circumstances

<img src='seasonality1.JPG'>
<img src='seasonality2.JPG'>
<img src='seasonality3.JPG'>

### Other examples of seasonality

- Weather modeling (e.g. temperature, rainfall)
- Flu monitoring
- Demand forecasting (e.g. jacket purchases: Having more stock during winter)
- Motion Capture Data

## Incorporating Multiple Inputs

### Multiple Regression Model

<img src='notation.JPG'>

- observations: N
- inputs: d
- features: D

<img src='model.JPG'>

### Computing Cost of Multiple Regression Model

<img src='multiple regression RSS.JPG'>

### Using Gradient to minimize Cost

Derivative of RSS

<img src='multiple regression RSS derivative.JPG'>

(1) Set Gradient to 0  (gradient = 0 )

<img src='solve for w.JPG'>

<img src='closed-form solution.JPG'>

(2) Gradient Descent

Here "partial" means partial derivative for jth feature

<img src='gradient descent for multiple regression.JPG'>
