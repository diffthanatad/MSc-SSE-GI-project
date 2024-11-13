#!/bin/sh

ARGV=$@

java -cp build/classes weka.classifiers.trees.RandomForest $ARGV -t ./data/test.arff
RETURN=$?

if [ $RETURN -ne 0 ]
then
    echo "FAILED ON FILE: ./data/test.arff"
    echo "GOT:" $RETURN
    echo "EXPECTED: 0"
    exit -1
fi
