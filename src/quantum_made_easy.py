# quantum_made_easy.py
# Makes quantum computing on IBM Q easier
# Author: Piotr Krawiec

from copy import deepcopy

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from typing import Sequence


def run_circuit_on_aersimulator(
    circuit: QuantumCircuit, shots=1024
) -> tuple[list[float], list[complex]]:
    """Runs a circuit on a simulator and returns the result.

    Args:
        circuit (QuantumCircuit): A circuit to run.
        shots (int, optional): Number of shots. Defaults to 1024.

    Returns:
        Result: A result of the circuit.
    """
    circuit_ = deepcopy(circuit)
    simulator = AerSimulator(method="statevector")
    circuit_.save_statevector()
    job = simulator.run(circuit_, shots=shots)

    # Grab results from the job
    result = job.result()
    counts = result.get_counts(circuit_)
    return [v / shots for _, v in counts.items()], list(result.get_statevector(circuit_))


def run_circuit_on_ibm_least_busy(
    service_name: str, circuit: QuantumCircuit | Sequence[QuantumCircuit], simulator=False
) -> list[float]:
    """Runs a circuit on the least busy IBM Q device and returns the result.

    Args:
        service (str): A service to use.
        circuit (QuantumCircuit): A circuit to run.

    Returns:
        Result: A result of the circuit.
    """
    service = QiskitRuntimeService(name=service_name)
    backend = service.least_busy(simulator=simulator, operational=True)
    with Session(backend=backend):
        sampler = Sampler()
        result = sampler.run(circuit).result()

    return list(result.quasi_dists.values())
