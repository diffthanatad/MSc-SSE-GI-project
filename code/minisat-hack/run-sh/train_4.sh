#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    ./simp/minisat_HACK_999ED_CSSC $FILENAME $ARGV > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILENAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test data/fuzz_100_29882.cnf 10
my_test data/fuzz_100_320.cnf 10
my_test data/fuzz_100_14452.cnf 10
my_test data/fuzz_100_880.cnf 10
my_test data/fuzz_100_9313.cnf 10

my_test data/fuzz_100_219.cnf 20
my_test data/fuzz_100_26937.cnf 20
my_test data/fuzz_100_224.cnf 20
my_test data/fuzz_100_19668.cnf 20
my_test data/fuzz_100_29884.cnf 20
