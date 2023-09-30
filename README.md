# 

## Running on Quantum Computer

To run the code on a quantum computer, you need to have an IBM Quantum account and an API token. You can get the token from the [IBM Quantum Experience](https://quantum-computing.ibm.com/).

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# Save an IBM Quantum account and set it as your default account. 
QiskitRuntimeService.save_account(channel="ibm_quantum", token="<token>", name="<service_name>")
```