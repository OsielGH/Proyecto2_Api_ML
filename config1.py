#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age']


#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['Fare']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Sex']

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'Pclass',
    'Sex',  
    'Age', 
    'SibSp', 
    'Parch', 
    'Fare',
    'Embarked',
]