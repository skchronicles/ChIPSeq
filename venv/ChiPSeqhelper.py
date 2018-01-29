##############################################
# ChIP-Seq Pipeline: MAC parser -> IGV
# Author: Skyler Kuhn (NIH/NCI) [C]
# CCR Collaborative Bioinformatics Resource
# Version 1.0.2, Excepted Release: 01/30/2017
# See readme.txt for more information
##############################################

# Imports
from __future__ import print_function, division
import subprocess as sp
import sys
import time


def check_args(all_args):
    """
    :param all_args: # (this is a list of all provided command-line arguements)
    :return: arg_dict # if 6 or 11arguments are not provided an Exception is raised
    TLDR: This function checks the provided command-line arguments and them uses regex to check to see if they are valid,
    if they are not an Exception is raised!
    """
    def parse_args(args):  # maybe look into using a decorator here, the more python-ic way
        """
        Generator that returns,
        :param args: (the list of args provided by sys.argv)
        :return:
        """
        for i in range(1, len(args)-1, 2):  # the zero-th index is the program name
            j = i + 1
            yield args[i], args[j]

    def invalid_usage_message():
        """
        :return: docstring error message
        TDLR: An error Message is returned if the wrong number of command-line args are provided
        """
        return """Failed to Provide Required Input Arguments:
            --n
            --narrowPeak_file
            --treatment_bw_file
            --input_bw_file
            --output_folder\n* Invalid Input Arguments provided *
            \nUsage:\npython ChIPSeqhelper.py --n=5 --narrowPeak_file=narrow.txt --treatmentBW_file=treatment.txt --inputBW_file=inputfile.txt --output_folder=FolderName
            """

    if len(all_args) != 6 and len(all_args) != 11:  # maybe use an assert statement here
        raise Exception(invalid_usage_message())

    arg_dict = {}  # k:switch (ex. --n), v:arguement (ex. 5)
    if len(all_args) == 11:
        arg_dict = {switch.lstrip("-"): argument for switch, argument in parse_args(args=all_args)}
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


def run_shell_commands(parsed_args):  # Change to a class called ChIPSeqPipeline
    """
    :param parsed_args:
    :yeild: command to be executed
    """
    #yield "hellooooooo"
    yield "sort -knr [column_3] OutputofMACSfile | head -n 50 > NewOutputfile.txt"
    yield "call IGV via CLI: use mm10 as ref, use BW normalized files: treatment and control"
    yield "mkdir NAMEofFolder"
    yield "Loop through N peaks from IGV output and mv snapshots to NAMEofFolder"
    yield "Clean up the directory as needed-- rm any un-needed files!"


def main():
    """
    Pseudo-main method
    :return:
    """
    # Checking the Arguments pass through CL
    arg_list = sys.argv
    print(arg_list)
    args_dict = check_args(all_args=arg_list)
    print(args_dict)

    # Start working with interfacing into the Pipeline
    for command in run_shell_commands(parsed_args=args_dict):
        sp.Popen("echo {}".format(command).split()).wait()  # Popen takes a list as parameter


if __name__ == "__main__":
    main()
