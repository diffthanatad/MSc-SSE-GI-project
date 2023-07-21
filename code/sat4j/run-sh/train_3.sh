#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    java -jar ../dist/CUSTOM/sat4j-sat.jar $FILENAME -s Default -S $ARGV > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILENAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test data/fuzz_100_29348.cnf 10
my_test data/fuzz_100_32582.cnf 10
my_test data/fuzz_100_19612.cnf 10
my_test data/fuzz_100_26964.cnf 10
my_test data/fuzz_100_3712.cnf 10

my_test data/fuzz_100_17835.cnf 20
my_test data/fuzz_100_3725.cnf 20
my_test data/fuzz_100_16511.cnf 20
my_test data/fuzz_100_6965.cnf 20
my_test data/fuzz_100_1340.cnf 20
