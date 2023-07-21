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

my_test data/fuzz_100_17714.cnf 10
my_test data/fuzz_100_14661.cnf 10
my_test data/fuzz_100_30392.cnf 10
my_test data/fuzz_100_31989.cnf 10
my_test data/fuzz_100_32265.cnf 10
my_test data/fuzz_100_1470.cnf 10
my_test data/fuzz_100_29268.cnf 10
my_test data/fuzz_100_19709.cnf 10
my_test data/fuzz_100_155.cnf 10
my_test data/fuzz_100_5082.cnf 10
my_test data/fuzz_100_29746.cnf 10
my_test data/fuzz_100_18691.cnf 10
my_test data/fuzz_100_13680.cnf 10
my_test data/fuzz_100_9273.cnf 10
my_test data/fuzz_100_18479.cnf 10
my_test data/fuzz_100_15572.cnf 10
my_test data/fuzz_100_27807.cnf 10
my_test data/fuzz_100_23292.cnf 10
my_test data/fuzz_100_22094.cnf 10
my_test data/fuzz_100_10807.cnf 10
my_test data/fuzz_100_27287.cnf 10
my_test data/fuzz_100_11431.cnf 10
my_test data/fuzz_100_9716.cnf 10
my_test data/fuzz_100_934.cnf 10
my_test data/fuzz_100_27903.cnf 10
my_test data/fuzz_100_6562.cnf 10
my_test data/fuzz_100_10133.cnf 10
my_test data/fuzz_100_15545.cnf 10
my_test data/fuzz_100_11558.cnf 10
my_test data/fuzz_100_2424.cnf 10
my_test data/fuzz_100_10419.cnf 10
my_test data/fuzz_100_23187.cnf 10
my_test data/fuzz_100_22526.cnf 10
my_test data/fuzz_100_4634.cnf 10
my_test data/fuzz_100_32764.cnf 10
my_test data/fuzz_100_26687.cnf 10
my_test data/fuzz_100_17061.cnf 10
my_test data/fuzz_100_13860.cnf 10
my_test data/fuzz_100_18535.cnf 10
my_test data/fuzz_100_26389.cnf 10
my_test data/fuzz_100_25436.cnf 10
my_test data/fuzz_100_4744.cnf 10
my_test data/fuzz_100_32015.cnf 10
my_test data/fuzz_100_1888.cnf 10
my_test data/fuzz_100_13600.cnf 10
my_test data/fuzz_100_16431.cnf 10
my_test data/fuzz_100_25320.cnf 10
my_test data/fuzz_100_14977.cnf 10
my_test data/fuzz_100_25474.cnf 10
my_test data/fuzz_100_8602.cnf 10
my_test data/fuzz_100_21829.cnf 10
my_test data/fuzz_100_8139.cnf 10
my_test data/fuzz_100_3144.cnf 10
my_test data/fuzz_100_28635.cnf 10
my_test data/fuzz_100_29205.cnf 10
my_test data/fuzz_100_30719.cnf 10
my_test data/fuzz_100_20561.cnf 10
my_test data/fuzz_100_3066.cnf 10
my_test data/fuzz_100_690.cnf 10
my_test data/fuzz_100_7467.cnf 10
my_test data/fuzz_100_17150.cnf 10
my_test data/fuzz_100_2022.cnf 10
my_test data/fuzz_100_2393.cnf 10
my_test data/fuzz_100_14633.cnf 10
my_test data/fuzz_100_411.cnf 10
my_test data/fuzz_100_9118.cnf 10
my_test data/fuzz_100_8846.cnf 10
my_test data/fuzz_100_8610.cnf 10
my_test data/fuzz_100_19687.cnf 10

my_test data/fuzz_100_6463.cnf 20
my_test data/fuzz_100_3546.cnf 20
my_test data/fuzz_100_23226.cnf 20
my_test data/fuzz_100_27424.cnf 20
my_test data/fuzz_100_29181.cnf 20
my_test data/fuzz_100_7085.cnf 20
my_test data/fuzz_100_911.cnf 20
my_test data/fuzz_100_22469.cnf 20
my_test data/fuzz_100_17352.cnf 20
my_test data/fuzz_100_29710.cnf 20
my_test data/fuzz_100_11470.cnf 20
my_test data/fuzz_100_23726.cnf 20
my_test data/fuzz_100_6906.cnf 20
my_test data/fuzz_100_31328.cnf 20
my_test data/fuzz_100_10683.cnf 20
my_test data/fuzz_100_11455.cnf 20
my_test data/fuzz_100_7453.cnf 20
my_test data/fuzz_100_31215.cnf 20
my_test data/fuzz_100_26658.cnf 20
my_test data/fuzz_100_6645.cnf 20
my_test data/fuzz_100_28413.cnf 20
my_test data/fuzz_100_26796.cnf 20
my_test data/fuzz_100_4152.cnf 20
my_test data/fuzz_100_16461.cnf 20
my_test data/fuzz_100_14730.cnf 20
my_test data/fuzz_100_11340.cnf 20
my_test data/fuzz_100_8669.cnf 20
my_test data/fuzz_100_8069.cnf 20
my_test data/fuzz_100_25891.cnf 20
my_test data/fuzz_100_7979.cnf 20
my_test data/fuzz_100_15882.cnf 20
my_test data/fuzz_100_30720.cnf 20
my_test data/fuzz_100_21921.cnf 20
my_test data/fuzz_100_10336.cnf 20
my_test data/fuzz_100_15955.cnf 20
my_test data/fuzz_100_290.cnf 20
my_test data/fuzz_100_25860.cnf 20
my_test data/fuzz_100_7454.cnf 20
my_test data/fuzz_100_23087.cnf 20
my_test data/fuzz_100_4872.cnf 20
my_test data/fuzz_100_30555.cnf 20
my_test data/fuzz_100_11723.cnf 20
my_test data/fuzz_100_15478.cnf 20
my_test data/fuzz_100_22912.cnf 20
my_test data/fuzz_100_15927.cnf 20
my_test data/fuzz_100_12828.cnf 20
my_test data/fuzz_100_1574.cnf 20
my_test data/fuzz_100_15449.cnf 20
my_test data/fuzz_100_14390.cnf 20
my_test data/fuzz_100_5272.cnf 20
my_test data/fuzz_100_21348.cnf 20
my_test data/fuzz_100_140.cnf 20
my_test data/fuzz_100_7468.cnf 20
my_test data/fuzz_100_8700.cnf 20
my_test data/fuzz_100_27992.cnf 20
my_test data/fuzz_100_11385.cnf 20
my_test data/fuzz_100_13072.cnf 20
my_test data/fuzz_100_15786.cnf 20
my_test data/fuzz_100_167.cnf 20
my_test data/fuzz_100_14289.cnf 20
my_test data/fuzz_100_28075.cnf 20
my_test data/fuzz_100_20955.cnf 20
my_test data/fuzz_100_32655.cnf 20
my_test data/fuzz_100_4178.cnf 20
my_test data/fuzz_100_27540.cnf 20
my_test data/fuzz_100_3173.cnf 20
my_test data/fuzz_100_8906.cnf 20
my_test data/fuzz_100_13461.cnf 20
my_test data/fuzz_100_22701.cnf 20
my_test data/fuzz_100_28725.cnf 20
my_test data/fuzz_100_13102.cnf 20
my_test data/fuzz_100_26729.cnf 20
my_test data/fuzz_100_10827.cnf 20
my_test data/fuzz_100_22473.cnf 20
my_test data/fuzz_100_31750.cnf 20
my_test data/fuzz_100_32695.cnf 20
my_test data/fuzz_100_3880.cnf 20
my_test data/fuzz_100_19139.cnf 20
my_test data/fuzz_100_15075.cnf 20
my_test data/fuzz_100_17583.cnf 20
my_test data/fuzz_100_15896.cnf 20
my_test data/fuzz_100_8042.cnf 20
my_test data/fuzz_100_28924.cnf 20
my_test data/fuzz_100_23735.cnf 20
my_test data/fuzz_100_2287.cnf 20
my_test data/fuzz_100_7482.cnf 20
my_test data/fuzz_100_24784.cnf 20
my_test data/fuzz_100_24913.cnf 20
my_test data/fuzz_100_740.cnf 20
my_test data/fuzz_100_22860.cnf 20
my_test data/fuzz_100_24280.cnf 20
my_test data/fuzz_100_9741.cnf 20
my_test data/fuzz_100_30501.cnf 20
my_test data/fuzz_100_19638.cnf 20
my_test data/fuzz_100_6999.cnf 20
my_test data/fuzz_100_13445.cnf 20
my_test data/fuzz_100_2783.cnf 20
my_test data/fuzz_100_5432.cnf 20
my_test data/fuzz_100_28057.cnf 20
my_test data/fuzz_100_1659.cnf 20
my_test data/fuzz_100_31552.cnf 20
my_test data/fuzz_100_17670.cnf 20
my_test data/fuzz_100_8917.cnf 20
my_test data/fuzz_100_31502.cnf 20
my_test data/fuzz_100_17116.cnf 20
my_test data/fuzz_100_18850.cnf 20
my_test data/fuzz_100_29018.cnf 20
my_test data/fuzz_100_14562.cnf 20
my_test data/fuzz_100_20513.cnf 20
my_test data/fuzz_100_31444.cnf 20
my_test data/fuzz_100_20097.cnf 20
my_test data/fuzz_100_29466.cnf 20
my_test data/fuzz_100_20673.cnf 20
my_test data/fuzz_100_10131.cnf 20
my_test data/fuzz_100_23655.cnf 20
my_test data/fuzz_100_11289.cnf 20
my_test data/fuzz_100_8555.cnf 20
my_test data/fuzz_100_861.cnf 20
my_test data/fuzz_100_374.cnf 20
my_test data/fuzz_100_9592.cnf 20
my_test data/fuzz_100_17245.cnf 20
my_test data/fuzz_100_27813.cnf 20
my_test data/fuzz_100_29444.cnf 20
my_test data/fuzz_100_9409.cnf 20
my_test data/fuzz_100_8499.cnf 20
my_test data/fuzz_100_5056.cnf 20
my_test data/fuzz_100_31794.cnf 20
my_test data/fuzz_100_27856.cnf 20
my_test data/fuzz_100_27097.cnf 20
my_test data/fuzz_100_29143.cnf 20
my_test data/fuzz_100_15240.cnf 20
my_test data/fuzz_100_24112.cnf 20
my_test data/fuzz_100_5791.cnf 20
my_test data/fuzz_100_17482.cnf 20
my_test data/fuzz_100_981.cnf 20
my_test data/fuzz_100_1.cnf 20
my_test data/fuzz_100_16484.cnf 20
my_test data/fuzz_100_9351.cnf 20
my_test data/fuzz_100_1408.cnf 20
my_test data/fuzz_100_27580.cnf 20
my_test data/fuzz_100_22874.cnf 20
my_test data/fuzz_100_847.cnf 20
my_test data/fuzz_100_25584.cnf 20
my_test data/fuzz_100_998.cnf 20
my_test data/fuzz_100_209.cnf 20
my_test data/fuzz_100_12029.cnf 20
my_test data/fuzz_100_28786.cnf 20
my_test data/fuzz_100_28016.cnf 20
my_test data/fuzz_100_1863.cnf 20
my_test data/fuzz_100_26756.cnf 20
my_test data/fuzz_100_3427.cnf 20
my_test data/fuzz_100_5842.cnf 20
my_test data/fuzz_100_31463.cnf 20
my_test data/fuzz_100_6431.cnf 20
my_test data/fuzz_100_14755.cnf 20
my_test data/fuzz_100_15188.cnf 20
my_test data/fuzz_100_17864.cnf 20
my_test data/fuzz_100_19494.cnf 20
my_test data/fuzz_100_8539.cnf 20
my_test data/fuzz_100_12437.cnf 20
my_test data/fuzz_100_17491.cnf 20
my_test data/fuzz_100_24953.cnf 20
my_test data/fuzz_100_30987.cnf 20
my_test data/fuzz_100_3040.cnf 20
my_test data/fuzz_100_15517.cnf 20
my_test data/fuzz_100_32743.cnf 20
my_test data/fuzz_100_7883.cnf 20
my_test data/fuzz_100_7091.cnf 20
my_test data/fuzz_100_29359.cnf 20
my_test data/fuzz_100_7672.cnf 20
my_test data/fuzz_100_24419.cnf 20
my_test data/fuzz_100_28968.cnf 20
my_test data/fuzz_100_31412.cnf 20
my_test data/fuzz_100_4683.cnf 20
my_test data/fuzz_100_20181.cnf 20
my_test data/fuzz_100_697.cnf 20
my_test data/fuzz_100_23228.cnf 20
my_test data/fuzz_100_27062.cnf 20
my_test data/fuzz_100_20761.cnf 20
my_test data/fuzz_100_10606.cnf 20
my_test data/fuzz_100_13019.cnf 20
my_test data/fuzz_100_14700.cnf 20
my_test data/fuzz_100_9816.cnf 20
my_test data/fuzz_100_12969.cnf 20
my_test data/fuzz_100_4179.cnf 20
my_test data/fuzz_100_29927.cnf 20
my_test data/fuzz_100_7371.cnf 20
my_test data/fuzz_100_3299.cnf 20
my_test data/fuzz_100_7385.cnf 20
my_test data/fuzz_100_24480.cnf 20
my_test data/fuzz_100_8910.cnf 20
my_test data/fuzz_100_736.cnf 20
my_test data/fuzz_100_9906.cnf 20
my_test data/fuzz_100_19720.cnf 20
my_test data/fuzz_100_5968.cnf 20
my_test data/fuzz_100_27728.cnf 20
my_test data/fuzz_100_7219.cnf 20
my_test data/fuzz_100_25045.cnf 20
my_test data/fuzz_100_15445.cnf 20
my_test data/fuzz_100_8522.cnf 20
my_test data/fuzz_100_9399.cnf 20
my_test data/fuzz_100_8372.cnf 20
my_test data/fuzz_100_30081.cnf 20
my_test data/fuzz_100_1190.cnf 20
my_test data/fuzz_100_12210.cnf 20
my_test data/fuzz_100_17745.cnf 20
my_test data/fuzz_100_22130.cnf 20
my_test data/fuzz_100_26318.cnf 20