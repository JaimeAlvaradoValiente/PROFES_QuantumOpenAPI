import connexion
import six

from openapi_server.models.quantum import Quantum  # noqa: E501
from openapi_server import util

def executeAWS(s3_folder, machine, circuit):

    if machine=="local":
        device = LocalSimulator()
        result = device.run(circuit, shots=100000).result()
        counts = result.measurement_counts
        return counts
        
    device = AwsDevice(machine)

    if "sv1" not in machine and "tn1" not in machine:
        task = device.run(circuit, s3_folder, shots=100, poll_timeout_seconds=5 * 24 * 60 * 60)
        counts = recover_task_result(task).measurement_counts
        return counts
    else:
        task = device.run(circuit, s3_folder, shots=100)
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






def find_service_by_category(qua):  # noqa: E501
    
    """Finds quantum service by category

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param qua: Status values that need to be considered for filter
    :type qua: List[str]

    :rtype: List[Quantum]
    """


    
