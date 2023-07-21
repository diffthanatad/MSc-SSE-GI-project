#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    java -jar ./dist/CUSTOM/sat4j-sat.jar $FILENAME -s Default -S $ARGV > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILENAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test data/fuzz_100_25509.cnf 10
my_test data/fuzz_100_14272.cnf 10
my_test data/fuzz_100_9659.cnf 10
my_test data/fuzz_100_570.cnf 10
my_test data/fuzz_100_15658.cnf 10

my_test data/fuzz_100_30360.cnf 20
my_test data/fuzz_100_22184.cnf 20
my_test data/fuzz_100_10756.cnf 20
my_test data/fuzz_100_12729.cnf 20
my_test data/fuzz_100_30181.cnf 20
