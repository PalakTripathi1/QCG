def grover(N, bits, iterate):
    Circuit = QuantumCircuit(bits)

    # Initialize the qubits in superposition
    Circuit.h(range(bits))

    # Apply Grover's iterations
    factors_circuit =factor(N, n_qubits)
    diffusion = diffuse(bits)

    for _ in range(iterate):
        Circuit.append(factors_circuit, range(bits))
        Circuit.append(diffusion, range(bits))

    Circuit.measure_all()

    # Simulate the circuit
    sim = Aer.get_backend('qasm_simulator')
    compileit = transpile(Circuit, sim)
    objects = assemble(compileit)
    rest = sim.run(objects).rest()
    cnts = rest.get_counts()
    return cnts

# Example: Factorizing N = 35
N = 35
bits = 6  # Number of qubits to represent the factors
iterate = 3  # Number of Grover iterations

cnts = grover(N, bits, iterate)
plot_histogram(cnts)