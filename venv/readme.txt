########################################
# Requester: Vishal Koparde
# Receiver: Skyler Kuhn
# Received: 01/15/2018
########################################

# For our ChIPSeq pipeline, we are trying to implement the following:
    Read in the peaks called by MACS (CHIP_Thpok_Biotin_vs_Input_Thpok_peaks.narrowPeak)
    Sort them by decreasing q-value
    Select the top n (n=50 for now)
    Load the following in IGV:
    Reference genome (in this case, mm10)
    Normalized bigwig for treatment (CHIP_Thpok_Biotin.R1.trim.not_blacklist_plus.sorted.mapq_gt_3.normalized.bw)
    Normalized bigwig for input (Input_Thpok.R1.trim.not_blacklist_plus.sorted.mapq_gt_3.normalized.bw)
    Loop through the n peaks and save n snapshots in an output folder.

# Input parameters for your script:
-- n
-- narrowPeak_file
-- treatment_bw_file
-- input_bw_file
-- output_folder

You can download the data from here (https://helix.nih.gov/~CCBR/forSkyler/forSkyler.tar) to your laptop.
You can get this working on your laptop and then we can move it over to biowulf at a later point.

# Other Notes:
==============
Format Information for Narrow Peaks File:

ENCODE narrowPeak: Narrow (or Point-Source) Peaks format

This format is used to provide called peaks of signal enrichment based on pooled, normalized (interpreted) data. It is a BED6+4 format.

1)  chrom - Name of the chromosome (or contig, scaffold, etc.).
2)  chromStart - The starting position of the feature in the chromosome or scaffold. The first base in a chromosome is numbered 0.
3)  chromEnd - The ending position of the feature in the chromosome or scaffold. The chromEnd base is not included in the display of the feature. For example, the first 100 bases of a chromosome are defined aschromStart=0, chromEnd=100, and span the bases numbered 0-99.
4)  name - Name given to a region (preferably unique). Use '.' if no name is assigned.
5)  score - Indicates how dark the peak will be displayed in the browser (0-1000). If all scores were '0' when the data were submitted to the DCC, the DCC assigned scores 1-1000 based on signal value. Ideally the average signalValue per base spread is between 100-1000.
6)  strand - +/- to denote strand or orientation (whenever applicable). Use '.' if no orientation is assigned.
7)  signalValue - Measurement of overall (usually, average) enrichment for the region.
8)  pValue - Measurement of statistical significance (-log10). Use -1 if no pValue is assigned.
9)  qValue - Measurement of statistical significance using false discovery rate (-log10). Use -1 if no qValue is assigned.
10) peak - Point-source called for this peak; 0-based offset from chromStart. Use -1 if no point-source called