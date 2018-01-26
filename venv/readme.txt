########################################
# Requester: Vishal Koparde
# Receiver: Skyler Kuhn
# Received: 01/15/2018
########################################

For our ChIPSeq pipeline, we are trying to implement the following:
    Read in the peaks called by MACS (CHIP_Thpok_Biotin_vs_Input_Thpok_peaks.narrowPeak)
    Sort them by decreasing q-value
    Select the top n (n=50 for now)
    Load the following in IGV:
    Reference genome (in this case, mm10)
    Normalized bigwig for treatment (CHIP_Thpok_Biotin.R1.trim.not_blacklist_plus.sorted.mapq_gt_3.normalized.bw)
    Normalized bigwig for input (Input_Thpok.R1.trim.not_blacklist_plus.sorted.mapq_gt_3.normalized.bw)
    Loop through the n peaks and save n snapshots in an output folder.

Input parameters for your script:
-- n
-- narrowPeak_file
-- treatment_bw_file
-- input_bw_file
-- output_folder

You can download the data from here (https://helix.nih.gov/~CCBR/forSkyler/forSkyler.tar) to your laptop.
You can get this working on your laptop and then we can move it over to biowulf at a later point.


Other Notes:
