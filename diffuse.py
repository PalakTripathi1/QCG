def diffuse(bits):
    # Define the diffusion operation 
    diffusion = QuantumCircuit(bits, name='diffusion')
    diffusion.h(range(bits))
    diffusion.x(range(bits))
    diffusion.h(bits - 1)
    diffusion.mcx(list(range(bits - 1)), bits - 1)
    diffusion.h(bits - 1)
    diffusion.x(range(bits))
    diffusion.h(range(bits))
    return diffusion