#!/bin/sh

ARGV=$@

my_test() {
    FILENAME=$1
    EXPECTED=$2
    ../simp/minisat $FILENAME $ARGV > /dev/null
    RETURN=$?
    if [ $RETURN -ne $((EXPECTED)) ]
    then
        echo "FAILED ON FILE:" $FILE NAME
        echo "GOT:" $RETURN
        echo "EXPECTED:" $EXPECTED
        exit -1
    fi
}

my_test ../../../data/circuit_fuzz/fuzz_100_15380.cnf 10
my_test ../../../data/circuit_fuzz/fuzz_100_2035.cnf 10
my_test ../../../data/circuit_fuzz/fuzz_100_3086.cnf 10
my_test ../../../data/circuit_fuzz/fuzz_100_45.cnf 10
my_test ../../../data/circuit_fuzz/fuzz_100_31574.cnf 10

my_test ../../../data/circuit_fuzz/fuzz_100_32080.cnf 20
my_test ../../../data/circuit_fuzz/fuzz_100_827.cnf 20
my_test ../../../data/circuit_fuzz/fuzz_100_2308.cnf 20
my_test ../../../data/circuit_fuzz/fuzz_100_21470.cnf 20
my_test ../../../data/circuit_fuzz/fuzz_100_14302.cnf 20
