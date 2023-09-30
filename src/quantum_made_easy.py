# quantum_made_easy.py
# Makes quantum computing on IBM Q easier
# Author: Piotr Krawiec

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from typing import Sequence


def run_circuit_on_aersimulator(
    circuits: QuantumCircuit, shots=1024
) -> list[dict[int, float]]:
    """Runs a circuit on a simulator and returns the result.

    Args:
        circuits (QuantumCircuit): A circuit to run.
        shots (int, optional): Number of shots. Defaults to 1024.

    Returns:
        Result: A result of the circuit.
    """
    simulator = AerSimulator()
    job = simulator.run(circuits, shots=shots)

    # Grab results from the job
    result = job.result()
    counts = result.get_counts(circuits)
    if not isinstance(counts, list):
        counts = [counts]
    return [{k: v / shots for k, v in c.items()} for c in counts]


def run_circuit_on_ibm_least_busy(
    service_name: str, circuit: QuantumCircuit | Sequence[QuantumCircuit]
) -> list[dict[int, float]]:
    """Runs a circuit on the least busy IBM Q device and returns the result.

    Args:
        service (str): A service to use.
        circuit (QuantumCircuit): A circuit to run.

    Returns:
        Result: A result of the circuit.
    """
    service = QiskitRuntimeService(name=service_name)
    backend = service.least_busy(simulator=False, operational=True)
    with Session(backend=backend):
        sampler = Sampler()
        result = sampler.run(circuit).result()

    return result.quasi_dists
