/*******************************************************************************
 * SAT4J: a SATisfiability library for Java Copyright (C) 2004, 2019 Artois University and CNRS
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 *  http://www.eclipse.org/legal/epl-v10.html
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU Lesser General Public License Version 2.1 or later (the
 * "LGPL"), in which case the provisions of the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of the LGPL, and not to allow others to use your version of
 * this file under the terms of the EPL, indicate your decision by deleting
 * the provisions above and replace them with the notice and other provisions
 * required by the LGPL. If you do not delete the provisions above, a recipient
 * may use your version of this file under the terms of the EPL or the LGPL.
 *
 * Based on the original MiniSat specification from:
 *
 * An extensible SAT solver. Niklas Een and Niklas Sorensson. Proceedings of the
 * Sixth International Conference on Theory and Applications of Satisfiability
 * Testing, LNCS 2919, pp 502-518, 2003.
 *
 * See www.minisat.se for the original solver in C++.
 *
 * Contributors:
 *   CRIL - initial API and implementation
 *******************************************************************************/

package org.sat4j.tools.counting;

import java.math.BigInteger;

import org.sat4j.specs.ISolver;

/**
 * ApproxMC implements the first version of the approximate model counter
 * proposed by Chakraborty, Meel and Vardi.
 * 
 * @author Romain WALLON
 */
public final class ApproxMC extends AbstractApproxMC {

    /**
     * Creates a new ApproxMC.
     * 
     * @param solver
     *            The solver to use as an oracle.
     * @param epsilon
     *            The tolerance of the count.
     * @param delta
     *            the confidence of the count.
     */
    public ApproxMC(ISolver solver, double epsilon, double delta) {
        super(solver, epsilon, delta);
    }

    /**
     * Creates a new ApproxMC.
     * 
     * @param solver
     *            The solver to use as an oracle.
     * @param samplingSet
     *            The set of variables to consider.
     * @param epsilon
     *            The tolerance of the count.
     * @param delta
     *            the confidence of the count.
     */
    public ApproxMC(ISolver solver, SamplingSet samplingSet, double epsilon,
            double delta) {
        super(solver, samplingSet, epsilon, delta);
    }

    /**
     * Creates a new ApproxMC.
     * 
     * @param solver
     *            The solver to use as an oracle.
     * @param samplingSet
     *            The set of variables to consider.
     */
    public ApproxMC(ISolver solver, SamplingSet samplingSet) {
        super(solver, samplingSet);
    }

    /**
     * Creates a new ApproxMC.
     * 
     * @param solver
     *            The solver to use as an oracle.
     */
    public ApproxMC(ISolver solver) {
        super(solver);
    }

    /*
     * (non-Javadoc)
     * 
     * @see org.sat4j.tools.counting.AbstractApproxMC#computeThreshold()
     */
    @Override
    protected int computeThreshold() {
        return (int) (3 * Math.exp(.5) * (1 + 1 / epsilon)
                * (1 + 1 / epsilon)) << 1;
    }

    /*
     * (non-Javadoc)
     * 
     * @see org.sat4j.tools.counting.AbstractApproxMC#computeIterCount()
     */
    @Override
    protected int computeIterCount() {
        return (int) (35 * Math.log(3 / delta) / Math.log(2));
    }

    /*
     * (non-Javadoc)
     * 
     * @see org.sat4j.tools.counting.AbstractApproxMC#internalCountModels(int)
     */
    @Override
    protected BigInteger internalCountModels(int threshold) {
        // This is equivalent to l = log2(pivot) - 1
        int l = Integer.SIZE - Integer.numberOfLeadingZeros(threshold) - 2;

        // Partitioning the space of all the models using parity constraints.
        for (int i = l; i <= samplingSet.nVars(); i++) {
            long count = boundedSAT(i - l, threshold + 1);

            if (1 <= count && count <= threshold) {
                // This cell is small enough and has to be scaled to the number
                // of cells generated by the hashing function.
                return BigInteger.valueOf(count).shiftLeft((i - l));
            }
        }

        // Reporting a counting error.
        return null;
    }

    /**
     * Counts up to {@code bound} models of the formula, after having added
     * {@code nbConstraints} parity constraints to the solver.
     * 
     * @param nbConstraints
     *            The number of constraints to add.
     * @param bound
     *            The maximum number of models to count.
     * 
     * @return The number of models that have been counted.
     */
    private long boundedSAT(int nbConstraints, int bound) {
        generator.generate(nbConstraints);
        long count = boundedSAT(bound);
        generator.clear();
        return count;
    }

}