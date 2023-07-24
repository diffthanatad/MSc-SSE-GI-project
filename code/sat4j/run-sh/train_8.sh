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

my_test data/fuzz_100_360.cnf 10
my_test data/fuzz_100_12028.cnf 10
my_test data/fuzz_100_818.cnf 10
my_test data/fuzz_100_16353.cnf 10
my_test data/fuzz_100_8354.cnf 10

my_test data/fuzz_100_16377.cnf 20
my_test data/fuzz_100_14069.cnf 20
my_test data/fuzz_100_25094.cnf 20
my_test data/fuzz_100_6173.cnf 20
my_test data/fuzz_100_31943.cnf 20