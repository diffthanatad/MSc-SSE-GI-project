#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    java -jar ./dist/CUSTOM/sat4j-sat.jar $FILENAME $ARGV > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILENAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test data/fuzz_100_6348.cnf 10
my_test data/fuzz_100_2182.cnf 10
my_test data/fuzz_100_699.cnf 10
my_test data/fuzz_100_18544.cnf 10
my_test data/fuzz_100_707.cnf 10

my_test data/fuzz_100_11346.cnf 20
my_test data/fuzz_100_23431.cnf 20
my_test data/fuzz_100_15665.cnf 20
my_test data/fuzz_100_17081.cnf 20
my_test data/fuzz_100_1322.cnf 20