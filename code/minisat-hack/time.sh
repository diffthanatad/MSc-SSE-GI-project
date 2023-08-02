{ time ./run-sh/test.sh -lbd-cut=5 -lbd-cut-max=10 -cp-increase=15000 -core-tolerance=0.02 -R-val=1.4 -var-decay=0.8 -cla-decay=0.999 -rnd-freq=0.0 -ccmin-mode='2' -phase-saving='2' -no-rnd-init -luby=0 -gc-frac=0.2 -verb='1' -pre -no-asymm -no-rcheck -elim -grow=0 -cl-lim=20 -sub-lim=1000 -simp-gc-frac=0.5 2> error_test.txt ; } 2> time_test.txt

