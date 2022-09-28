#!/bin/bash

# First step is to assign your states with w_assign (or w_ipa)
# and make sure your assign.h5 file is in this directory. Then
# run the first script

python 01_gen_succ_list.py

mv succ_traj 01_succ_list

# Next, run the pattern matching script which will output
# a text file containing each pair and the similarities.

python 02_pattern_match.py

# Next, run the third script to print the pathways that have
# a sequence similarity score greater than 50%.

python 03_discard_pathways.py > 03_discarded.txt

# You will need to gen modify the output of the third script
# so all entries are iter and seg with no space inbetween. For
# example, if it prints out '100 30' delete the space to make
# that line '10030'. Then run the following:

cat 03_discard_pathways.txt | sort | uniq > 03_discard_pathways_uniq.txt

# Now, run the fourth script, which will extract the fundamental
# trajectories.

ln -s ../traj_segs .
ln -s ../common_files .
ln -s ../istates .

python 04_extract_success.py

mv succ_traj 04_succ_traj

# And now run the final script to print the number and ID of
# the reduced, fundamental pathways.

python 05_check_pathways.py
