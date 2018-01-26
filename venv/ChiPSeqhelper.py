#################################################
# Skyler Kuhn (NIH/NCI) [C]
# CCR Collaborative Bioinformatics Resource
# Leidos Biomedical Research, Inc.
#################################################
from __future__ import print_function, division
import sys
import time


def check_args(all_args):
    """
    :param all_args: # (this is a list of all provided command-line arguements)
    :return: arg_dict # if 6 or 11arguments are not provided an Exception is raised
    TLDR: This function checks the provided command-line arguments and them uses regex to check to see if they are valid,
    if they are not an Exception is raised!
    """
    def invalid_usage_message():
        """
        :return: docstring error message
        TDLR: An error Message is returned if the wrong number of command-line args are provided
        """
        return """\nFailed to Provide Required Input Arguments:
            --n
            --narrowPeak_file
            --treatment_bw_file
            --input_bw_file
            --output_folder\n* Invalid Input Arguments provided *"""

    def parse_args(args):  # maybe look into using a decorator here, the more python-ic way
        """
        Generator that returns,
        :param args: (the list of args provided by sys.argv)
        :return:
        """
        for i in range(1, len(args)-1, 2):  # the zero-th index is the program name
            j = i + 1
            yield args[i], args[j]

    if len(all_args) != 6 and len(all_args) != 11:  # maybe use an assert statement here
        raise Exception(invalid_usage_message())

    arg_dict = {}  # k:switch (ex. --n), v:arguement (ex. 5)
    if len(all_args) == 11:
        arg_dict = {switch: argument for switch, argument in parse_args(args=all_args)}
    else:          # 6 args formatted like this: python ChiPSeqhelper.py --n=1 --narrowfile=narrowFH.txt ...(etc.)
        for arg in all_args[1:]:
            stripped_args_list = arg.lstrip("-").split("=")
            arg_dict[stripped_args_list[0]] = stripped_args_list[1]

    return arg_dict


def benchmarker(any_function):
    """
    :param any_function: (function to be timed)
    :return: String giving timing info for a given function
    TDLR: Decorator that takes a function as a parameter and outputs its timing info (benchmarking)
    """

    def timing_wrapper(*args, **kwargs):
        t1 = time.time()
        any_function(*args, **kwargs)
        t2 = time.time()
        return "Time it took to run {} function:{}\n".format(some_function.__name__, str(t2 - t1))
    return timing_wrapper


def main():
    """
    Pseudo-main method
    :return:
    """
    arg_list = sys.argv
    print(arg_list)
    check_args(all_args=arg_list)
    # Start working with the Pipeline next


if __name__ == "__main__":
    main()



