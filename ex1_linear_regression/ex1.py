#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

## Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions 
#  in this exericse:
#
#     warmUpExercise.m
#     plotData.m
#     gradientDescent.m
#     computeCost.m
#     gradientDescentMulti.m
#     computeCostMulti.m
#     featureNormalize.m
#     normalEqn.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

def warmUpExercise():
	"""an example function that returns the 5x5 identity matrix."""
	return np.eye(5, dtype=float)

def plotData(X, y):
	"""Plots the data points x and y into a new figure.
	Additionally, it gives the figure axes labels of population and profit.
	"""
	# ====================== YOUR CODE HERE ======================
	# Instructions: Plot the training data into a figure using the 
	#               "figure" and "plot" commands. Set the axes labels using
	#               the "xlabel" and "ylabel" commands. Assume the 
	#               population and revenue data have been passed in
	#               as the x and y arguments of this function.
	#
	# Hint: You can use the 'rx' option with plot to have the markers
	#       appear as red crosses. Furthermore, you can make the
	#       markers larger by using plot(..., 'rx', 'MarkerSize', 10);

	plt.xlabel('population')
	plt.ylabel('profit')
	plt.plot(X,y, 'rx', markersize=10)
	plt.show()

def part1():
	## ==================== Part 1: Basic Function ====================
	# Complete warmUpExercise
	print '-' * 30
	print('Running warmUpExercise ... ')
	print('5x5 Identity Matrix: ')
	x = warmUpExercise()
	print x
	print '-' * 30

def part2():
	## ======================= Part 2: Plotting =======================
	print('Plotting Data ...')
	data = np.genfromtxt('ex1data1.txt', delimiter=',')
	X = data[:, 0:-1]
	y = data[:, 1]
	# Plot Data
	plotData(X, y);
	print '-' * 30

#part1()
part2()

# ## =================== Part 3: Gradient descent ===================
# fprintf('Running Gradient Descent ...\n')

# X = [ones(m, 1), data(:,1)]; # Add a column of ones to x
# theta = zeros(2, 1); # initialize fitting parameters

# # Some gradient descent settings
# iterations = 1500;
# alpha = 0.01;

# # compute and display initial cost
# computeCost(X, y, theta)

# # run gradient descent
# theta = gradientDescent(X, y, theta, alpha, iterations);

# # print theta to screen
# fprintf('Theta found by gradient descent: ');
# fprintf('#f #f \n', theta(1), theta(2));

# # Plot the linear fit
# hold on; # keep previous plot visible
# plot(X(:,2), X*theta, '-')
# legend('Training data', 'Linear regression')
# hold off # don't overlay any more plots on this figure

# # Predict values for population sizes of 35,000 and 70,000
# predict1 = [1, 3.5] *theta;
# fprintf('For population = 35,000, we predict a profit of #f\n',...
#     predict1*10000);
# predict2 = [1, 7] * theta;
# fprintf('For population = 70,000, we predict a profit of #f\n',...
#     predict2*10000);

# fprintf('Program paused. Press enter to continue.\n');
# pause;

# ## ============= Part 4: Visualizing J(theta_0, theta_1) =============
# fprintf('Visualizing J(theta_0, theta_1) ...\n')

# # Grid over which we will calculate J
# theta0_vals = linspace(-10, 10, 100);
# theta1_vals = linspace(-1, 4, 100);

# # initialize J_vals to a matrix of 0's
# J_vals = zeros(length(theta0_vals), length(theta1_vals));

# # Fill out J_vals
# for i = 1:length(theta0_vals)
#     for j = 1:length(theta1_vals)
# 	  t = [theta0_vals(i); theta1_vals(j)];    
# 	  J_vals(i,j) = computeCost(X, y, t);
#     end
# end


# # Because of the way meshgrids work in the surf command, we need to 
# # transpose J_vals before calling surf, or else the axes will be flipped
# J_vals = J_vals'
# # Surface plot
# figure;
# surf(theta0_vals, theta1_vals, J_vals)
# xlabel('\theta_0'); ylabel('\theta_1');

# # Contour plot
# figure;
# # Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
# contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
# xlabel('\theta_0'); ylabel('\theta_1');
# hold on;
# plot(theta(1), theta(2), 'rx', 'MarkerSize', 10, 'LineWidth', 2);
