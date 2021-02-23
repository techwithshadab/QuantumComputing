# Remote Cirq Client for Floq

This client uses the cirq interface to communicate quantum circuit computation
to the Floq Service. This client is designed to be simple to use for those familiar
with the Cirq.Simulator interface.

## Basic Usage
```python
from remote_cirq import RemoteSimulator

sim = RemoteSimulator('my_api_key')

qubits = cirq.LineQubit.range(26)

param_resolver = cirq.ParamResolver({'a': 1})

a = sympy.Symbol('a')
circuit = cirq.Circuit(
	[cirq.X(q) ** a for q in qubits] +
	[cirq.measure(q) for q in qubits])

sim.run(circuit, param_resolver) #Results from the cloud hurray!
```

## More Usage
Currently the remote cirq client supports cirq's `SimulatesSamples` and the
upcoming `SimulatesExpectationValues`. These interfaces include methods for 
running sampling and calculating expectation values of single circuits, batches
of circuits or circuits to be resolved with parameter value sweeps.

### SimulatesSamples
The following functionality is provided with the `SimulatesSamples` interface:
```python

sim.run_batch(list_of_circuits, list_of_param_resolvers)
sim.run_sweep(circuit, cirq.study.Sweepable) # Sweep over params!
```

For more info see the cirq interface documentation 
[here](https://quantumai.google/reference/python/cirq/sim/SimulatesSamples)


Note - This client does not support the `async` run calls currently.


### SimulatesExpectationValues
The client also provides calculation of expectation values against 
`cirq.PauliSum` observables.

This interface is included in the upcoming Cirq 0.10.0 release.

The following functionality is provided:
```python
# Find expectation against a single Paulisum

magnetization_op = sum([cirq.Z(q) for q in qubits])
sim.simulate_expectation_values(
	circuit, 
	magnetization_op, 
	param_resolvers)

	# returns [exp_value]

# Or against multiple

sim.simulate_expectation_values(
	circuit, 
	[magnetization_op, cirq.X(qubits[0]) + cirq.Y(qubits[0])]
)
	# returns [exp1, exp2] - one expectation per observable

# Also run sweeps over param_resolver values
sim.simulate_expectation_values_sweep(
	circuit,
	[observable1, observable2],
	cirq.Sweepable
)
	# returns [[exp1, exp2], ...] - one list of expectations per param set
```

## PennyLane-Cirq with Floq

To use Floq-backend in PennyLane, please install the latest version of
PennyLane-Cirq plugin.

```
$ pip install pennylane-cirq==0.14.0
```

Then, you can create a PennyLane Quantum Device with Floq RemoteSimulator.

```python
import remote_cirq
import pennylane as qml
import numpy as np
import sys
wires = 26
np.random.seed(0)

weights = np.random.randn(1, wires, 3)
API_KEY = "YOUR_API_KEY_HERE"
sim = remote_cirq.RemoteSimulator(API_KEY)

dev = qml.device("cirq.simulator",
                 wires=wires,
                 simulator=sim,
                 analytic=False)

@qml.qnode(dev)
def my_circuit(weights):
	qml.templates.layers.StronglyEntanglingLayers(weights,
	                                              wires=range(wires))
	return qml.expval(qml.PauliZ(0))

print(my_circuit(weights))
```

## Caveats
Keep in mind that you are on the frontier and this is a very experimental 
service! There will be trials, tribulations, and bugs! 

Please let us know about issues you encounter - floq-devs@google.com

That being said there are a few known limitations at this point. In order to be
conservative we have implemented restrictions on the size of circuits, number
of observables, etc... We are working hard to push this forward, bear with us.

This client also has some limitations due to its dependence on cirq. A known 
issue in cirq 0.9.1 is deficiency in serialization. Cirq does not currently 
support serialization of of gates parameterized on more than one symbol.
Because Cirq rx, ry, and rz gates depend on an implicit internal symbol they
can fail. This is actively being resolved! **In the meantime try using XPow,
YPow, ZPow gates instead:**

```python
cirq.rx(s) -> cirq.XPowGate(exponent=s / np.pi, global_shift=-0.5)
```

Enjoy!
