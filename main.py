import logging
import sys

from src.tacq.TemplateAcquisition import TemplateAcquisition


if __name__ == "__main__":
    if len(sys.argv) == 6:
        logging.basicConfig(format="- %(message)s", level=logging.ERROR, datefmt="%H:%M:%S")
        param_nb_examples = int(sys.argv[1])   # Number of examples to use
        param_examples_file = sys.argv[2]  # File containing the examples
        param_timeout_solver = int(sys.argv[3])  # Timeout for the experiment in seconds
        if sys.argv[4] == "1":
            logging.basicConfig(format="- %(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")
            param_verbose = True  # Verbose mode
        else:
            logging.basicConfig(format="- %(message)s", level=logging.ERROR, datefmt="%H:%M:%S")
            logging.disable(logging.CRITICAL)
            param_verbose = False
        param_max_cpu = int(sys.argv[5]) # Maximum number of CPU cores to use
        ta = TemplateAcquisition()
        ta.learn(param_examples_file, param_nb_examples, param_timeout_solver, param_verbose, param_max_cpu)
        print("=== Learned Network ===")
        print(ta.get_network())
        print("=== Learned Template ===")
        print(ta.get_template())

    else:
        print("Usage: python -u main.py <nb_examples> <examples_file> <timeout_solver> <verbose> <max_cpu>")
        print("Example: python -u main.py 1000 examples.csv 3600 1 8")
        print("This will learn a CSP from the first 1000 examples in examples.csv with a timeout of 3600 seconds, "
              "verbose mode enabled, and using 8 CPU cores.")
        sys.exit(1)