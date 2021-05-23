def qft_cirq(n, qubits, circuit):
    for i in range(n):
        circuit.append(H(qubits[i]), strategy = InsertStrategy.NEW)
        for k in range(i+1 , n):
            CR_k = CZPowGate(exponent = 2/ 2**(k-i+1))
            circuit.append(CR_k(qubits[k], qubits[i]), strategy = InsertStrategy.NEW)
        
    
    
    for i in range(n//2):
        circuit.append(SWAP(qubits[i],qubits[n-i-1]), strategy = InsertStrategy.NEW)     

def iqft_cirq(n, qubits, circuit):
    for i in range(n//2):
        circuit.append(SWAP(qubits[i], qubits[n-i-1]), strategy = InsertStrategy.NEW)
    
    for i in range(n-1, -1, -1):
        
        for k in range(n-1, i, -1):
            CR_k = CZPowGate(exponent =- 2/ 2**(k-i+1))
            circuit.append(CR_k(qubits[k], qubits[i]), strategy = InsertStrategy.NEW)
            
        circuit.append(H(qubits[i]), strategy = InsertStrategy.NEW)
    
