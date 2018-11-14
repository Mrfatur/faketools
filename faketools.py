#ss!/bin/bash

# auto mengunduh file <3
# auto menginstall 
# author Mr.Froggy
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
im
#This colour
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

###################################################
# CTRL C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red"[#]> (Ctrl + C ) Detected, Trying To Exit ... "
sleep 1
echo ""
echo -e $yellow"[#]> Thank You For Using My Tools ... "
sleep 1
echo ""
echo -e $white"[#]> froggy Wuzz Here ... "
read enter
exit
}

# Isi $oc :*
echo -e $cyan"   |-----------------  /\           |  /     _______________         ___/    / / / __ \/ __ \/ / ___/ "
echo -e $blue"   |                  /  \          | /     |                              
echo -e $red"    |--------------   /----\         |  \    |                          / / / /_/ / /_/ / (__  ) "                       
echo -e $blue"   |                /      \        |   \   |_______________            /_/  \____/\____/_/____/ 
echo -e $yellow" |               /        \       |    \  |                          
echo -e $red"    |                                        |______________             

echo ""
echo -e $white"         ***********************************************"
echo -e $white"         #                                             #"
echo -e $white"         # $cyan  Toolkit For$red Lazy People$white                   #"
echo -e $white"         # $cyan  V3rluchie Tools Recoded by$red Mr.Froggy$white          #"
echo -e $white"         # $cyan  Follow Me On Github:$red $white            #"
echo -e $white"         # $cyan  My Site:$red https://faketools.tr$white #"
echo -e $white"         # $cyan  Contact Me In:$red faketools.com$white    #"
echo -e $white"         # $cyan  Changelog: $red 23-10-2017   $white                 #"
echo -e $white"         # $cyan  Team: $red Anon Cyber Team$white                    #"
echo -e $white"         #                                             #"
echo -e $white"         ***********************************************"
echo ""
if [ $act = 2 ] || [ $act = 02 ]
then
clear
echo -e $red" Installing D-Tect "
sleep 1
apt-get update && apt-get upgrade
apt-get install git
apt-get install python2
git clone https://github.com/Mrfatur/Vbgu
echo -e $red" T E R I N S T A L L "
fi


if [ $act = 22 ] || [ $act = 22  ]
then
echo " Aku Sange "
sleep 1
echo " mmmpppssss "
sleep 1
echo " aaahhh "
sleep 1
echo " mmmpppsss "
sleep 1
echo " aaahhh "
sleep 1
echo " Bye Sayang :* "
sleep 1
exit
fi
