# 🌌 Exploring Majorana Zero Modes in Quantum Spin Chains

#  What Is It About?

This project simulates a special type of quantum system—a chain of tiny magnets (called spins)—and explores the possibility of finding Majorana zero modes, which are strange, stable particles that could one day power error-proof quantum computers.

Think of this as exploring a tiny universe governed by quantum rules to search for particles that are incredibly hard to detect but could change the future of technology.



#  Why Do This?

Quantum computers are powerful, but they are also very sensitive to errors. Tiny disturbances from the environment can ruin a calculation.

Majorana zero modes (MZMs) are theoretical particles that might store quantum information in a stable way, immune to noise and interference. If we can understand how and when they appear in simple systems, we can use that knowledge to design better quantum materials and devices.

This project focuses on one such system: the transverse-field Ising model (TFIM) and its extensions. These are simplified models of interacting quantum spins.



#  Basics You Should Know

#  What Is a Spin Chain?

Imagine a row of quantum particles where each particle acts like a tiny magnet, pointing either up or down. These spins can interact with each other and with external magnetic fields.

The way they interact is described by a mathematical object called a Hamiltonian, which tells us the energy of different configurations.

# 🔹 What Is the Transverse-Field Ising Model (TFIM)?

It's one of the simplest models of a spin chain. The particles prefer to align with their neighbors (like friends copying each other), but an external magnetic field pulls them in another direction.

This tension causes a quantum phase transition, similar to how water turns into ice.

# 🔹 What Are Majorana Zero Modes?

These are special states that can appear at the ends of a quantum wire. They are:
- Neutral (no charge),
- Their own antiparticles,
- Immune to local noise,
- Theoretically ideal for topological quantum computing.

They usually appear when the system enters a topological phase, which is what we’re trying to find.



# 🛠️ What This Project Does

This project simulates a 3-spin extension of the TFIM, which includes both nearest and next-nearest neighbor interactions. Here's a high-level outline of what we did:

1. Built the Hamiltonian of the extended spin model using known formulas.
2. Mapped spins to fermions using the Jordan-Wigner transformation — this makes the math easier by turning the spin system into a particle system.
3. Transformed to momentum space and applied the Bogoliubov-de Gennes transformation to diagonalize the system — revealing its energy levels.
4. Numerically simulated the system with open ends to check for Majorana zero modes localized at the chain edges.
5. Plotted the results to visually confirm when and where these edge states appear.
6. Analyzed the topological nature of the system using a mathematical quantity called the winding number, which changes when the system enters or exits a topological phase.

# 1. Transverse-Field Ising Model (TFIM)
A fundamental 1D spin model with spins interacting along one direction and subjected to a transverse magnetic field. The competition between the spin interaction (J) and the field (h) drives a quantum phase transition.

General form:H = -J ∑ σ_i^x σ_{i+1}^x - h ∑ σ_i^z

# 2. Jordan-Wigner Transformation
Used to convert the spin model into a model of non-interacting fermions, enabling exact diagonalization in 1D.

# 3. Bogoliubov-de Gennes (BdG) Transformation
Used to diagonalize the fermionic Hamiltonian in momentum space by introducing quasiparticle operators.



# ⚙️ What Was Done

- We implemented the three-spin extension of the TFIM:
H = - ∑ ( g σ_i^x + λ₁ σ_{i-1}^x σ_i^z + λ₂ σ_i^x σ_{i-1}^z σ_{i+1}^z )

- This model was mapped to a quadratic fermionic Hamiltonian using Jordan-Wigner.
- The resulting Hamiltonian was diagonalized numerically using BdG methods.
- Simulations were run under open boundary conditions to detect edge-localized Majorana modes.
- Eigenvector plots were generated to visualize the localization of zero-energy modes.
- A winding number (topological invariant) was computed to identify topological phase transitions.



#  Topological Insight

- The number of MZMs at the edges changes across critical lines in the (λ₁, λ₂) parameter space.
- These changes are tied to a winding number that quantifies how the BdG Hamiltonian "wraps" in phase space.
- Breaking time-reversal symmetry shows that 2-MZM phases are fragile, while 1-MZM phases remain robust.



#  Sample Results

- Regions with 0, 1, or 2 Majorana modes were confirmed via diagonalization.
- Edge-localized eigenvectors confirm Majorana nature.
- Numerical phase diagram matches theoretical predictions.




#  What We Found

- We discovered regions in parameter space where the system hosts 0, 1, or 2 Majorana zero modes at its ends.
- These MZMs only appear under open boundary conditions, not in closed loops.
- The appearance of MZMs matches critical lines where the system undergoes a phase transition.
- The winding number, a topological invariant, changes by exactly the number of MZMs appearing.



#  Why This Matters

- Quantum Computing: Majorana zero modes could be used to build topological qubits, which are naturally resistant to errors.
- Material Science: The model studied here is similar to real systems like nanowires or superconducting chains.
- Theoretical Physics: Helps us understand how topological phases arise in simple models, providing intuition for more complex systems.



# Visuals Included

- Phase diagrams showing where phase transitions occur.
- Plots of eigenvectors that clearly show edge-localized zero-energy modes.
- Winding number changes that signal topological phase transitions.



# 🖥️ How to Run

# 📋 Requirements

- Python 3.8 or higher
- numpy
- matplotlib

# ▶️ Run with:

```bash
pip install numpy matplotlib
python simulate_majorana.py
