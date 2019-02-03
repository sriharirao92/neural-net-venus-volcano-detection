# ArtificialNeuralNetwork_VenusVolcanoDetection
A 3 layer Artificial Neural Network to detect volcano eruptions on Venus from Images from NASA

## Context

NASA's Magellan (https://www2.jpl.nasa.gov/magellan/) spacecraft was launched on May 4, 1989 and arrived at Venus on August 10, 1990. The primary objectives of the Magellan mission were to map the surface of Venus with a synthetic aperture radar (SAR) and to determine the topographic relief of the planet. At the completion of radar mapping 98% of the surface was imaged at resolutions better than 100 m, and many areas were imaged multiple times. 
In the analysis of the data captured by the spacecraft they found volcanoes on the surface on Venus, volcanoes that can be used to make a automatic machine that can detect them.

## Content

We present the data split into train and test. The input data (*train_images.csv* and *test_images.csv*) consist on Images of one chanel 110x110, pixels from 0 to 255, where every image is one row of 12100 columns (all the 110 rows of 110 columns), this images can contain more then one volcano or maybe none . Associated to this we present the label data or "ground truth" (*train_labels.csv* and *test_labels.csv*), which contains four columns, described here:

Volcano?: if in the image there are volcanoes (Main target), 1 or 0.
for Volcano?=0 this three next features are NaN * Type: 1= definitely a volcano,2 =probably, 3= possibly, 4= only a pit is visible * Radius: is the radius of the volcan in the center of the image, in pixels * Number Volcanoes: The number of volcanoes in the image

The images that have volcanoes, have one centered on the image. The authors quote "ground truth" as a reminder that there is no absolute ground truth for this dataset. No one has been to Venus and image quality does not permit 100%, unambiguos identification of the volcanoes, even by human experts.

The data is unbalanced and that has to be taken account, the number of volcanoes is lower than no volcanoes.

## Missing Values 
Some images contain blank (black) regions which resulted from gaps in the Magellan acquisition or communication processes. These regions can generally be ignored.

## Acknowledgements
The original dataset has been carried out in part by the Jet Propulsion Laboratory, California Institute of Technology, under contract with the National Aeroenautics and Space Administration, and thanks to UCI Machine Learning Repository (http://archive.ics.uci.edu/ml) we use the original dataset to create this one to you in Kaggle!

## Inspiration
JARtool (jartool@aig.jpl.nasa.go) was a pioneering effort to develop an automatic system for cataloging small volcanoes in the large set of Venus images returned by the Magellan spacecraft. We use the original dataset to create this one with the same purpose..
