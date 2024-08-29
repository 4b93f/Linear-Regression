# Linear Regression

The `Linear Regression` project is a python implementation of linear regression algorithms. This project aims to provide a clear understanding of linear regression and its applications in data analysis and machine learning. The implementation covers both simple linear regression and multiple linear regression techniques.

## Table of Contents

- [Linear Regression](#linear-regression)
	- [Table of Contents](#table-of-contents)
	- [About the Project](#about-the-project)
	- [Features](#features)
	- [Algorithm Overview](#algorithm-overview)
		- [Simple Linear Regression](#simple-linear-regression)
		- [Multiple Linear Regression](#multiple-linear-regression)
	- [Getting Started](#getting-started)
		- [Prerequisites](#prerequisites)
		- [Installation](#installation)

## About the Project

This project provides a python implementation of linear regression models to predict continuous outcomes based on input features. It includes:

- **Simple Linear Regression**: A model with one independent variable.
- **Multiple Linear Regression**: A model with multiple independent variables.

The project demonstrates how to implement and apply linear regression techniques to real-world data, including how to fit a model, make predictions, and evaluate performance.

## Features

- **Simple Linear Regression**: Fit a linear model with one feature and predict outcomes.
- **Multiple Linear Regression**: Fit a linear model with multiple features.
- **Parameter Estimation**: Calculate coefficients using Ordinary Least Squares (OLS).
- **Prediction**: Make predictions based on the fitted model.
- **Model Evaluation**: Evaluate the model's performance using metrics like Mean Squared Error (MSE) and R² score.
- **Data Preprocessing**: Handle and preprocess data for better model performance.

## Algorithm Overview

### Simple Linear Regression

Simple linear regression models the relationship between two variables by fitting a linear equation to observed data. The model can be represented as:

\[ y = \beta_0 + \beta_1 x \]

Where:
- \( y \) is the dependent variable (target).
- \( x \) is the independent variable (feature).
- \( \beta_0 \) is the y-intercept.
- \( \beta_1 \) is the slope of the line.

### Multiple Linear Regression

Multiple linear regression extends simple linear regression to include multiple features. The model is represented as:

\[ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n \]

Where:
- \( y \) is the dependent variable.
- \( x_1, x_2, \ldots, x_n \) are the independent variables (features).
- \( \beta_0 \) is the y-intercept.
- \( \beta_1, \beta_2, \ldots, \beta_n \) are the coefficients for the features.

## Getting Started

### Prerequisites

- **python**
- **Make** build tool.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/4b93f/Linear-Regression.git
   cd Linear-Regression
