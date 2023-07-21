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

my_test data/fuzz_100_28454.cnf 10
my_test data/fuzz_100_10971.cnf 10
my_test data/fuzz_100_6107.cnf 10
my_test data/fuzz_100_7669.cnf 10
my_test data/fuzz_100_21025.cnf 10

my_test data/fuzz_100_23258.cnf 20
my_test data/fuzz_100_895.cnf 20
my_test data/fuzz_100_553.cnf 20
my_test data/fuzz_100_398.cnf 20
my_test data/fuzz_100_7558.cnf 20
