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

my_test data/fuzz_100_595.cnf 10
my_test data/fuzz_100_28974.cnf 10
my_test data/fuzz_100_29783.cnf 10
my_test data/fuzz_100_8583.cnf 10
my_test data/fuzz_100_15331.cnf 10

my_test data/fuzz_100_27427.cnf 20
my_test data/fuzz_100_19320.cnf 20
my_test data/fuzz_100_16551.cnf 20
my_test data/fuzz_100_18541.cnf 20
my_test data/fuzz_100_17777.cnf 20