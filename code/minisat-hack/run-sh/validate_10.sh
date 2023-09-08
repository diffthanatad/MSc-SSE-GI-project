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

my_test data/fuzz_100_25509.cnf 10
my_test data/fuzz_100_14272.cnf 10
my_test data/fuzz_100_9659.cnf 10
my_test data/fuzz_100_570.cnf 10
my_test data/fuzz_100_15658.cnf 10
my_test data/fuzz_100_32622.cnf 10
my_test data/fuzz_100_28454.cnf 10
my_test data/fuzz_100_10971.cnf 10
my_test data/fuzz_100_6107.cnf 10
my_test data/fuzz_100_7669.cnf 10
my_test data/fuzz_100_21025.cnf 10
my_test data/fuzz_100_27000.cnf 10
my_test data/fuzz_100_29348.cnf 10
my_test data/fuzz_100_32582.cnf 10
my_test data/fuzz_100_19612.cnf 10
my_test data/fuzz_100_26964.cnf 10
my_test data/fuzz_100_3712.cnf 10
my_test data/fuzz_100_16654.cnf 10
my_test data/fuzz_100_29882.cnf 10
my_test data/fuzz_100_320.cnf 10
my_test data/fuzz_100_14452.cnf 10
my_test data/fuzz_100_880.cnf 10
my_test data/fuzz_100_9313.cnf 10
my_test data/fuzz_100_491.cnf 10
my_test data/fuzz_100_15380.cnf 10
my_test data/fuzz_100_2035.cnf 10
my_test data/fuzz_100_3086.cnf 10
my_test data/fuzz_100_45.cnf 10
my_test data/fuzz_100_31574.cnf 10
my_test data/fuzz_100_2846.cnf 10
my_test data/fuzz_100_595.cnf 10
my_test data/fuzz_100_28974.cnf 10
my_test data/fuzz_100_29783.cnf 10
my_test data/fuzz_100_8583.cnf 10
my_test data/fuzz_100_15331.cnf 10
my_test data/fuzz_100_13843.cnf 10
my_test data/fuzz_100_6348.cnf 10
my_test data/fuzz_100_2182.cnf 10
my_test data/fuzz_100_699.cnf 10
my_test data/fuzz_100_18544.cnf 10
my_test data/fuzz_100_707.cnf 10
my_test data/fuzz_100_14448.cnf 10
my_test data/fuzz_100_360.cnf 10
my_test data/fuzz_100_12028.cnf 10
my_test data/fuzz_100_818.cnf 10
my_test data/fuzz_100_16353.cnf 10
my_test data/fuzz_100_8354.cnf 10
my_test data/fuzz_100_28180.cnf 10
my_test data/fuzz_100_19666.cnf 10
my_test data/fuzz_100_817.cnf 10
my_test data/fuzz_100_28085.cnf 10
my_test data/fuzz_100_26944.cnf 10
my_test data/fuzz_100_25064.cnf 10
my_test data/fuzz_100_12426.cnf 10

my_test data/fuzz_100_30360.cnf 20
my_test data/fuzz_100_22184.cnf 20
my_test data/fuzz_100_10756.cnf 20
my_test data/fuzz_100_12729.cnf 20
my_test data/fuzz_100_30181.cnf 20
my_test data/fuzz_100_17975.cnf 20
my_test data/fuzz_100_28747.cnf 20
my_test data/fuzz_100_60.cnf 20
my_test data/fuzz_100_19.cnf 20
my_test data/fuzz_100_4111.cnf 20
my_test data/fuzz_100_33.cnf 20
my_test data/fuzz_100_17322.cnf 20
my_test data/fuzz_100_8451.cnf 20
my_test data/fuzz_100_26869.cnf 20
my_test data/fuzz_100_142.cnf 20
my_test data/fuzz_100_489.cnf 20
my_test data/fuzz_100_6758.cnf 20
my_test data/fuzz_100_7675.cnf 20
my_test data/fuzz_100_23258.cnf 20
my_test data/fuzz_100_895.cnf 20
my_test data/fuzz_100_553.cnf 20
my_test data/fuzz_100_398.cnf 20
my_test data/fuzz_100_7558.cnf 20
my_test data/fuzz_100_26652.cnf 20
my_test data/fuzz_100_956.cnf 20
my_test data/fuzz_100_30849.cnf 20
my_test data/fuzz_100_29862.cnf 20
my_test data/fuzz_100_29197.cnf 20
my_test data/fuzz_100_30146.cnf 20
my_test data/fuzz_100_31497.cnf 20
my_test data/fuzz_100_6939.cnf 20
my_test data/fuzz_100_587.cnf 20
my_test data/fuzz_100_13011.cnf 20
my_test data/fuzz_100_12902.cnf 20
my_test data/fuzz_100_17817.cnf 20
my_test data/fuzz_100_25.cnf 20
my_test data/fuzz_100_17835.cnf 20
my_test data/fuzz_100_3725.cnf 20
my_test data/fuzz_100_16511.cnf 20
my_test data/fuzz_100_6965.cnf 20
my_test data/fuzz_100_1340.cnf 20
my_test data/fuzz_100_208.cnf 20
my_test data/fuzz_100_24900.cnf 20
my_test data/fuzz_100_4444.cnf 20
my_test data/fuzz_100_27055.cnf 20
my_test data/fuzz_100_7674.cnf 20
my_test data/fuzz_100_10987.cnf 20
my_test data/fuzz_100_535.cnf 20
my_test data/fuzz_100_7823.cnf 20
my_test data/fuzz_100_695.cnf 20
my_test data/fuzz_100_31467.cnf 20
my_test data/fuzz_100_609.cnf 20
my_test data/fuzz_100_116.cnf 20
my_test data/fuzz_100_13194.cnf 20
my_test data/fuzz_100_219.cnf 20
my_test data/fuzz_100_26937.cnf 20
my_test data/fuzz_100_224.cnf 20
my_test data/fuzz_100_19668.cnf 20
my_test data/fuzz_100_29884.cnf 20
my_test data/fuzz_100_24676.cnf 20
my_test data/fuzz_100_20571.cnf 20
my_test data/fuzz_100_24191.cnf 20
my_test data/fuzz_100_22028.cnf 20
my_test data/fuzz_100_11224.cnf 20
my_test data/fuzz_100_111.cnf 20
my_test data/fuzz_100_810.cnf 20
my_test data/fuzz_100_11326.cnf 20
my_test data/fuzz_100_2909.cnf 20
my_test data/fuzz_100_30344.cnf 20
my_test data/fuzz_100_778.cnf 20
my_test data/fuzz_100_18896.cnf 20
my_test data/fuzz_100_21624.cnf 20
my_test data/fuzz_100_32080.cnf 20
my_test data/fuzz_100_827.cnf 20
my_test data/fuzz_100_2308.cnf 20
my_test data/fuzz_100_21470.cnf 20
my_test data/fuzz_100_14302.cnf 20
my_test data/fuzz_100_29127.cnf 20
my_test data/fuzz_100_28378.cnf 20
my_test data/fuzz_100_17115.cnf 20
my_test data/fuzz_100_689.cnf 20
my_test data/fuzz_100_349.cnf 20
my_test data/fuzz_100_22171.cnf 20
my_test data/fuzz_100_797.cnf 20
my_test data/fuzz_100_19730.cnf 20
my_test data/fuzz_100_367.cnf 20
my_test data/fuzz_100_115.cnf 20
my_test data/fuzz_100_18331.cnf 20
my_test data/fuzz_100_7756.cnf 20
my_test data/fuzz_100_21446.cnf 20
my_test data/fuzz_100_27427.cnf 20
my_test data/fuzz_100_19320.cnf 20
my_test data/fuzz_100_16551.cnf 20
my_test data/fuzz_100_18541.cnf 20
my_test data/fuzz_100_17777.cnf 20
my_test data/fuzz_100_26639.cnf 20
my_test data/fuzz_100_18548.cnf 20
my_test data/fuzz_100_13080.cnf 20
my_test data/fuzz_100_1563.cnf 20
my_test data/fuzz_100_16215.cnf 20
my_test data/fuzz_100_26201.cnf 20
my_test data/fuzz_100_14306.cnf 20
my_test data/fuzz_100_13727.cnf 20
my_test data/fuzz_100_15104.cnf 20
my_test data/fuzz_100_269.cnf 20
my_test data/fuzz_100_10492.cnf 20
my_test data/fuzz_100_18283.cnf 20
my_test data/fuzz_100_3216.cnf 20
my_test data/fuzz_100_11346.cnf 20
my_test data/fuzz_100_23431.cnf 20
my_test data/fuzz_100_15665.cnf 20
my_test data/fuzz_100_17081.cnf 20
my_test data/fuzz_100_1322.cnf 20
my_test data/fuzz_100_18595.cnf 20
my_test data/fuzz_100_20708.cnf 20
my_test data/fuzz_100_18681.cnf 20
my_test data/fuzz_100_5259.cnf 20
my_test data/fuzz_100_194.cnf 20
my_test data/fuzz_100_524.cnf 20
my_test data/fuzz_100_7786.cnf 20
my_test data/fuzz_100_5290.cnf 20
my_test data/fuzz_100_20562.cnf 20
my_test data/fuzz_100_17096.cnf 20
my_test data/fuzz_100_15367.cnf 20
my_test data/fuzz_100_13410.cnf 20
my_test data/fuzz_100_23681.cnf 20
my_test data/fuzz_100_16377.cnf 20
my_test data/fuzz_100_14069.cnf 20
my_test data/fuzz_100_25094.cnf 20
my_test data/fuzz_100_6173.cnf 20
my_test data/fuzz_100_31943.cnf 20
my_test data/fuzz_100_18832.cnf 20
my_test data/fuzz_100_454.cnf 20
my_test data/fuzz_100_949.cnf 20
my_test data/fuzz_100_5052.cnf 20
my_test data/fuzz_100_13610.cnf 20
my_test data/fuzz_100_29217.cnf 20
my_test data/fuzz_100_356.cnf 20
my_test data/fuzz_100_9733.cnf 20
my_test data/fuzz_100_28104.cnf 20
my_test data/fuzz_100_3676.cnf 20
my_test data/fuzz_100_581.cnf 20
my_test data/fuzz_100_13148.cnf 20
my_test data/fuzz_100_9393.cnf 20
my_test data/fuzz_100_7973.cnf 20
my_test data/fuzz_100_32676.cnf 20
my_test data/fuzz_100_15554.cnf 20
my_test data/fuzz_100_17588.cnf 20
my_test data/fuzz_100_18812.cnf 20
my_test data/fuzz_100_529.cnf 20
my_test data/fuzz_100_19549.cnf 20
my_test data/fuzz_100_6791.cnf 20
my_test data/fuzz_100_802.cnf 20
my_test data/fuzz_100_28416.cnf 20
my_test data/fuzz_100_22056.cnf 20
my_test data/fuzz_100_9358.cnf 20
my_test data/fuzz_100_16167.cnf 20
my_test data/fuzz_100_21201.cnf 20
my_test data/fuzz_100_643.cnf 20
my_test data/fuzz_100_11587.cnf 20
my_test data/fuzz_100_16696.cnf 20
my_test data/fuzz_100_25959.cnf 20
