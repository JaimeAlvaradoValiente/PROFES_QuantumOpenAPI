import connexion
import six
import time
import os

from openapi_server import util

def executeAWS(s3_folder, machine, circuit, shots):
    os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
    if machine=="local":
        device = LocalSimulator()
        result = device.run(circuit, int(shots)).result()
        counts = result.measurement_counts
        return counts
        
    device = AwsDevice(machine)

    if "sv1" not in machine and "tn1" not in machine:
        task = device.run(circuit, s3_folder, int(shots), poll_timeout_seconds=5 * 24 * 60 * 60)
        counts = recover_task_result(task).measurement_counts
        return counts
    else:
        task = device.run(circuit, s3_folder, int(shots))
        counts = task.result().measurement_counts
        return counts

def recover_task_result(task_load):
    # recover task
    sleep_times = 0
    while sleep_times < 100000:
        status = task_load.state()
        print('Status of (reconstructed) task:', status)
        print('\n')
        # wait for job to complete
        # terminal_states = ['COMPLETED', 'FAILED', 'CANCELLED']
        if status == 'COMPLETED':
            # get results
            return task_load.result()
        else:
            time.sleep(1)
            sleep_times = sleep_times + 1
    print("Quantum execution time exceded")
    return None

    



from braket.circuits import Gate
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice


def grover_circuit_aws(machine, shots):  # noqa: E501
    
    """Get the circuit implementation of Grover Algorithm

     # noqa: E501

    :param machine: Name of the machine where to execute
    :type machine: str
    :param shots: Number of shots
    :type shots: 

    :rtype: None
    """


    gate_machines_arn= { "riggeti_aspen8":"arn:aws:braket:::device/qpu/rigetti/Aspen-8", "riggeti_aspen9":"arn:aws:braket:::device/qpu/rigetti/Aspen-9", "riggeti_aspen11":"arn:aws:braket:::device/qpu/rigetti/Aspen-11", "riggeti_aspen_m1":"arn:aws:braket:us-west-1::device/qpu/rigetti/Aspen-M-1", "DM1":"arn:aws:braket:::device/quantum-simulator/amazon/dm1","oqc_lucy":"arn:aws:braket:eu-west-2::device/qpu/oqc/Lucy", "borealis":"arn:aws:braket:us-east-1::device/qpu/xanadu/Borealis", "ionq":"arn:aws:braket:::device/qpu/ionq/ionQdevice", "sv1":"arn:aws:braket:::device/quantum-simulator/amazon/sv1", "tn1":"arn:aws:braket:::device/quantum-simulator/amazon/tn1", "local":"local"}
    s3_folder = ("amazon-braket-7c2f2fa45286", "api")
    circuit = Circuit()
    circuit.h(0)
    circuit.h(1)
    circuit.h(2)
    circuit.h(3)
    circuit.h(4)
    return executeAWS(s3_folder, gate_machines_arn[machine], circuit, shots)

    #return 'do some magic!'



from qiskit import execute, QuantumRegister, ClassicalRegister, QuantumCircuit, Aer
from numpy import pi


def grover_circuit_ibm(shots, machine=None):  # noqa: E501
    
    """Get the circuit implementation of Grover Algorithm

     # noqa: E501

    :param shots: Number of shots
    :type shots: 
    :param machine: Name of the machine where to execute
    :type machine: str

    :rtype: None
    """


    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(5, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    circuit.h(qreg_q[0])
    circuit.h(qreg_q[1])
    circuit.h(qreg_q[2])
    circuit.h(qreg_q[3])
    circuit.h(qreg_q[4])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[2], creg_c[2])
    circuit.measure(qreg_q[3], creg_c[3])
    circuit.measure(qreg_q[4], creg_c[4])
    backend = Aer.get_backend("qasm_simulator")
    x=int(shots)
    job = execute(circuit, backend, shots=x)
    result = job.result()
    counts = result.get_counts()
    return counts

    #return 'do some magic!'

