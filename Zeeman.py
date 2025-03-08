import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_B = 9.274e-24  # Bohr magneton (J/T)
h = 6.626e-34  # Planck's constant (J·s)
eV_to_J = 1.602e-19  # Energy conversion factor (eV to J)
c = 3e8  # Speed of light (m/s)

# Define quantum numbers
L = 1  # Orbital angular momentum
S = 0.5  # Spin
I = 0.5  # Nuclear spin
A = 1e-6 * eV_to_J  # Hyperfine coupling constant (in J)

# Magnetic field values
B_values = np.linspace(0, 2, 200)  # Magnetic field (Tesla)

# Landé g-factor formula
def lande_g(L, S, J):
    return (3/2) + (S * (S + 1) - L * (L + 1)) / (2 * J * (J + 1))

# Hyperfine energy
def hyperfine_energy(F, J, I, A):
    return A * 0.5 * (F * (F + 1) - I * (I + 1) - J * (J + 1))

# Zeeman energy shift
def zeeman_energy(g_J, m, B):
    return g_J * mu_B * m * B

# Compute energy levels
def compute_energy_levels(L, S, I, B_values):
    J_values = [L + S, abs(L - S)]
    energy_levels = []
    
    for J in J_values:
        g_J = lande_g(L, S, J)
        F_values = [J + I, abs(J - I)]
        for F in F_values:
            m_values = np.arange(-F, F + 1, 1)
            for m in m_values:
                hyperfine = hyperfine_energy(F, J, I, A)
                zeeman = zeeman_energy(g_J, m, B_values)
                total_energy = hyperfine + zeeman
                energy_levels.append((F, m, total_energy / eV_to_J))
    
    return energy_levels

# Calculate levels
energy_levels = compute_energy_levels(L, S, I, B_values)

# Plot results
plt.figure(figsize=(12, 8))

for F, m, energy in energy_levels:
    plt.plot(B_values, energy, label=f"F={F}, m={m}")

plt.title("Complex Zeeman Effect with Hyperfine Splitting")
plt.xlabel("Magnetic Field Strength (T)")
plt.ylabel("Energy (eV)")
plt.legend(ncol=2, fontsize=8)
plt.grid()
plt.show()
