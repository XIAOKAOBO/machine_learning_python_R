# simple linear regression

dataset = read.csv('Salary_Data.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

regressor = lm(Salary~YearsExperience,data=training_set)

# predict

y_pred=predict(regressor,newdata=test_set)
library(ggplot2)
ggplot()+geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),color='red')+geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata=training_set)))+ggtitle('Hahaha')+xlab('ye')+ylab('sal')

