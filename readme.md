# Readme

## Features

### Main

* Title : `String`
* Refrences - where it appears : `Array[String]`
* In force/Not in Force : `Boolean`
* Replaced by : `Article`

### Dates

* Date of document : `Date`
* Date of effect : `Date`
* Date of signature : `Date`
* Date of end of validity : `Date`

### Languages



### Classifactions

* Eurovoc descriptors : `Array[String]` (on average with length 5)
* Subject matter : `Array[String]` (on average length 2)
* Directory code : `Array[String Hierarchy[4]]` (on average lentgh of 1.31)

### Miscellaneous

* Author : `Array[String]`
* Form : `String` (Institutional agreement, International etc.)

### Relationship

* Amended by : `Article`
* Amendmant to : `Article`

### Text



## Methods

### Problem Transformation with Dubbed Copy
### Binary Relevance: One classifier for each class label
### Dimensionality reduction (SVD)


## Proposal structure

### Goal/Objective - EUROVOC multi-label classification

* Dataset summary: Data structure, Possible problems
* The problem we chose: EUROVOC + motivation

### Preprocessing

1. Parse html - using what tool? (beautifulsoup)
2. Extract features
3. Extract text
4. Preprocessing on text - using what tool? (scikit-learn)
5. Load everthing into a database (for ex. SQLite) -> Motivation: dataset doesn't fit into memory

### Baseline models

Problem Transformation:
* Problem Transformation with Dubbed Copy
* Binary Relevance: One classifier for each class label
* Dimensionality reduction (SVD)

Classifaction:
* Use classic supervised learning learners (ex. Decision trees, Naive Bayes, SVMs) provided by scikit-learn

### Evaluation

* Link to multilabel classifcation survey - have to be provided by scikit-learn


