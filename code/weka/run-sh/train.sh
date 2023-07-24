#!/bin/sh

java -cp build/classes weka.classifiers.trees.RandomForest $ARGV -t ./data/train.arff 