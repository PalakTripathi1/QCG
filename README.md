# QCG
Grover’s algorithm is a quantum algorithm that solves the unstructured search problem. In an unstructured search problem, we are given a set of N elements and we want to find a single marked element. A classical computer would need to search through all N elements in order to find the marked element, which would take time O(N). Grover’s algorithm, on the other hand, can find the marked element in time  O(√ N).

Grover’s algorithm is a powerful tool that can be used to solve a variety of problems. For example, it can be used to find patterns in data, break cryptographic keys, and solve optimization problems. As quantum computers become more powerful, Grover’s algorithm will become increasingly important.

The algorithm works by applying a series of quantum operations to the input state, which is initialized as a superposition of all possible search states. The key idea behind Grover’s algorithm is to amplify the amplitude of the marked state (i.e., the state containing the item that we are searching for) by iteratively applying a quantum operation known as the Grover operator.
The Grover operator has two quantum operations: 

The reflection on the mean 
The inversion of the marked state. 
The algorithm starts in a state that is a superposition of all N elements. This state is expressed as:
![image](https://github.com/PalakTripathi1/QCG/assets/127396297/c8dc5f40-fbff-437a-bd55-ced8efe96563)
where ∣x⟩ is the state corresponding to the element x.

 Next is the Diffusion Operator as:
 Diffusion operator: 
The diffusion operator is a quantum operation that amplifies the amplitudes of the states that correspond to the marked element. The diffusion operator can be written as:
![image](https://github.com/PalakTripathi1/QCG/assets/127396297/1935283b-6698-491c-b5ba-8b72b092ad6c)
where I is the identity operator.

The Schematic Circuit can be shown as:
![image](https://github.com/PalakTripathi1/QCG/assets/127396297/a3257bb4-5a08-47e0-96c3-4e08f06dafe3)


The Code is explained as:
Input: N: number of items in the list, factor(x): a function that returns true if x is the target item, and false otherwise

Step 1: Initialize state

Hadamard transform on all bits
Step 2: Iterate over Grover’s algorithm

for k = 1 to sqrt(N) do

    Step 2a: Apply the factor

Apply the factor(oracle) to the state
    # Step 2b: Apply the diffusion operator

Hadamard transform on all qubits
Apply an X gate on all qubits
Apply a multi-controlled Z gate (which flips the sign of the state only if all bits are in the state |1>)
Apply an X gate on all qubits
Hadamard transform on all qubits
end for

Step 3: Measure the state and output the result

Measure the state and output the result



