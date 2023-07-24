#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    java -jar ./dist/CUSTOM/sat4j-sat.jar $FILENAME > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILENAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test data/fuzz_100_6339.cnf 10
my_test data/fuzz_100_7015.cnf 10
my_test data/fuzz_100_15771.cnf 10
my_test data/fuzz_100_13098.cnf 10
my_test data/fuzz_100_26988.cnf 10

my_test data/fuzz_100_5540.cnf 20
my_test data/fuzz_100_4204.cnf 20
my_test data/fuzz_100_890.cnf 20
my_test data/fuzz_100_13502.cnf 20
my_test data/fuzz_100_16903.cnf 20