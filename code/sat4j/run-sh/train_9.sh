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

my_test data/fuzz_100_19666.cnf 10
my_test data/fuzz_100_817.cnf 10
my_test data/fuzz_100_28085.cnf 10
my_test data/fuzz_100_26944.cnf 10
my_test data/fuzz_100_25064.cnf 10

my_test data/fuzz_100_7973.cnf 20
my_test data/fuzz_100_32676.cnf 20
my_test data/fuzz_100_15554.cnf 20
my_test data/fuzz_100_17588.cnf 20
my_test data/fuzz_100_18812.cnf 20
