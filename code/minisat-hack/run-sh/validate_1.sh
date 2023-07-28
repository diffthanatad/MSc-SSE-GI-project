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

my_test data/fuzz_100_15380.cnf 10
my_test data/fuzz_100_2035.cnf 10
my_test data/fuzz_100_3086.cnf 10
my_test data/fuzz_100_45.cnf 10
my_test data/fuzz_100_31574.cnf 10
my_test data/fuzz_100_32080.cnf 20
my_test data/fuzz_100_827.cnf 20
my_test data/fuzz_100_2308.cnf 20
my_test data/fuzz_100_21470.cnf 20
my_test data/fuzz_100_14302.cnf 20

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
