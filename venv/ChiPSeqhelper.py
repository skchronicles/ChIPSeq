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
    Driver for running shell commands, using yield statements forces asynchronous processing
    :param parsed_args:
    :yeild: command to be executed
    """

    yield "sort -knr [column_3] OutputofMACSfile | head -n 50 > NewOutputfile.txt"
    yield "call IGV via CLI: use mm10 as ref, use BW normalized files: treatment and control"
    yield "mkdir NAMEofFolder"
    yield "Loop through N peaks from IGV output and mv snapshots to NAMEofFolder"
    yield "Clean up the directory as needed-- rm any un-needed files!"


class ChipSeqPipeline(object):
    """
    Takes dictionary of validated arguments from check_args, sorts & selects MAC CLT output, and then calls IGV CLT
    """
    def __init__(self, args_dict):
        # Attributes
        self.args_dict = args_dict
        self.n = args_dict['n']                             # change this so it is not so hard-coded
        self.narrow_peaks = args_dict['narrowPeak_file']    # change this so it is not so hard-coded
        self.treatment_bw = args_dict['treatment_bw_file']  # change this so it is not so hard-coded
        self.input_bw = args_dict['input_bw_file']          # change this so it is not so hard-coded
        self.output_folder = args_dict['output_folder']     # change this so it is not so hard-coded
        # Methods
        self.run()

    def validate(self):   # insert check_args code into here
        """
        takes a list of __init__ attributes
        :return: boolean
        """
        pass   # Return True: if valid inputs

    def __run(self, command_list, pipe):
        """
        Private method used to run commands in shell
        When running pipe="yes", it runs:
        sort -k9nr,9 CHIP_Thpok_Biotin_vs_Input_Thpok_peaks.narrowPeak | head -50 > outputfile.narrowfile
        :param command_list:
        :pipe specify whether you want to pipe commands
        :return:
        """
        if pipe == "yes":
            p1 = sp.Popen(command_list, stdout=sp.PIPE)
            p2 = sp.Popen("head -50".split(), stdin=p1.stdout, stdout=sp.PIPE)
            p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
            output = p2.communicate()[0]

            fh = open("CHIP_Thpok_Biotin_vs_Input_Thpok_peaks_SORTEDqValue_TOP50.narrowPeak", "w")
            fh.write(output)
            fh.close()

        elif pipe == "no":
            sp.Popen(command_list).wait()

    def run(self):
        """
        Sorts the Output of MACS (by decreasing q-value) & selects tops 'n' results
        calls IGV CLT, loops through results -> saves screenshots to an Output folder
        :return: Output folder with IGv N-peaks results
        """
        self.validate()
        self.__run("sort -k9nr,9 CHIP_Thpok_Biotin_vs_Input_Thpok_peaks.narrowPeak".split(), "yes")
        #self.__run("echo call IGV via CLI: use mm10 as ref, use BW normalized files: treatment and control".split())
        #self.__run("echo mkdir NAMEofFolder".split())
        #self.__run("echo Loop through N peaks from IGV output and mv snapshots to NAMEofFolder".split())
        #self.__run("echo Clean up the directory as needed-- rm any un-needed files!".split())

    def __str__(self):
        return "Parameters: {}".format(self.args_dict)


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
    #for command in run_shell_commands(parsed_args=args_dict):
    #    sp.Popen("echo {}".format(command).split()).wait()  # Popen takes a list as parameter

    useChIPSeq = ChipSeqPipeline(args_dict)
    print(useChIPSeq)


if __name__ == "__main__":
    main()
